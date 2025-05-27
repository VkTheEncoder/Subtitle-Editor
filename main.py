#!/usr/bin/env python3
import os
import tempfile
import logging

from flask import Flask, request, abort
from dotenv import load_dotenv
import pysubs2
from telegram import Bot, Update
from telegram.utils.request import Request
from telegram.ext import Dispatcher, MessageHandler, Filters

from styles import DefaultStyle

# load .env locally; on Koyeb your real env-vars are injected automatically
load_dotenv()

BOT_TOKEN   = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
PORT        = int(os.getenv("PORT", 8080))

if not BOT_TOKEN or not WEBHOOK_URL:
    raise RuntimeError("⚠️ BOT_TOKEN and WEBHOOK_URL must be set as environment variables")

# Flask + Telegram setup
app = Flask(__name__)
bot = Bot(token=BOT_TOKEN, request=Request(con_pool_size=8))
dp  = Dispatcher(bot, None, workers=0)
logging.basicConfig(level=logging.INFO)

# register webhook immediately (works under any WSGI or __main__)
bot.set_webhook(WEBHOOK_URL)

@app.route("/", methods=["GET"])
def health():
    return "OK", 200

@app.route("/webhook", methods=["POST"])
def webhook():
    if not request.is_json:
        abort(400)
    update = Update.de_json(request.get_json(force=True), bot)
    dp.process_update(update)
    return "", 200

def handle_document(update: Update, context=None):
    doc      = update.message.document
    filename = doc.file_name
    ext      = os.path.splitext(filename)[1].lower()

    if ext not in (".srt", ".vtt"):
        return update.message.reply_text("🚫 Send me a .srt or .vtt file, please.")

    in_path = out_path = None
    try:
        # download into a unique temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp_in:
            in_path = tmp_in.name
        bot.getFile(doc.file_id).download(custom_path=in_path)

        # load subtitles
        subs = pysubs2.load(in_path)

        # ─── set video resolution ────────────────────────────────
        subs.info["PlayResX"] = "1920"
        subs.info["PlayResY"] = "1080"

        # ─── register & apply your Default style ─────────────────
        subs.styles["Default"] = DefaultStyle
        for line in subs:
            line.style = "Default"

        subs.resolve_overlaps()

        # save out to another temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".ass") as tmp_out:
            out_path = tmp_out.name
        subs.save(out_path)

        # reply with your styled .ass
        with open(out_path, "rb") as f:
            reply_name = os.path.splitext(filename)[0] + ".ass"
            update.message.reply_document(f, filename=reply_name)

    except Exception:
        logging.exception("Conversion failed")
        update.message.reply_text("❌ Oops—something went wrong. Try again?")
    finally:
        # cleanup
        for p in (in_path, out_path):
            if p and os.path.exists(p):
                try: os.remove(p)
                except: pass

# register the handler
dp.add_handler(MessageHandler(Filters.document, handle_document))

if __name__ == "__main__":
    # for local testing only; on Koyeb it’s served by Flask automatically
    app.run(host="0.0.0.0", port=PORT)
