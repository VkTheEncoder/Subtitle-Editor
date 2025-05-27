#!/usr/bin/env python3
import os
import tempfile
import logging

from flask import Flask, request, abort
from dotenv import load_dotenv
import pysubs2

from telegram import Bot, Update
from telegram.ext import Dispatcher, MessageHandler, Filters

from styles import DefaultStyle, SiteStyle

# Load env – Koyeb injects BOT_TOKEN & WEBHOOK_URL
load_dotenv()
BOT_TOKEN   = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
PORT        = int(os.getenv("PORT", 8080))

if not BOT_TOKEN or not WEBHOOK_URL:
    raise RuntimeError("BOT_TOKEN & WEBHOOK_URL must be set as env vars")

# Flask + Bot setup
app = Flask(__name__)
bot = Bot(token=BOT_TOKEN)
dp  = Dispatcher(bot, None, workers=0, use_context=True)
logging.basicConfig(level=logging.INFO)

# Register webhook
bot.set_webhook(WEBHOOK_URL)

@app.route("/", methods=["GET"])
def health():
    return "OK", 200

@app.route("/webhook", methods=["POST"])
def webhook():
    if not request.is_json:
        abort(400)
    upd = Update.de_json(request.get_json(force=True), bot)
    dp.process_update(upd)
    return "", 200

def handle_document(update, context):
    doc      = update.message.document
    filename = doc.file_name
    ext      = os.path.splitext(filename)[1].lower()

    if ext not in (".srt", ".vtt"):
        return update.message.reply_text("🚫 Please send a .srt or .vtt file.")

    in_path = out_path = None
    try:
        # Download
        with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp_in:
            in_path = tmp_in.name
        bot.getFile(doc.file_id).download(custom_path=in_path)

        # Load
        subs = pysubs2.load(in_path)

        # Set resolution
        subs.info["PlayResX"] = "1920"
        subs.info["PlayResY"] = "1080"

        # Register styles
        subs.styles["Default"] = DefaultStyle
        subs.styles["site"]    = SiteStyle

        # 1) Prepend your “site” event from 0 → 5 min
        site_tag = r"{\fad(4000,3000)\fn@Arial Unicode MS\fs31.733\c&H00FFFFFF&\alpha&H99&\b1\a1\fscy60}"
        # start/end in milliseconds:
        start_ms = 0
        end_ms   = 5 * 60 * 1000
        site_event = pysubs2.SSAEvent(
            start=start_ms,
            end=end_ms,
            style="site",
            text=site_tag + "HindiSubbing.com"
        )
        subs.events.insert(0, site_event)

        # 2) Apply Default to all existing lines + semi-transparent shadow override
        alpha_tag = r"{\4a&H96&}"
        for line in subs.events[1:]:  # skip the first site_event
            line.style = "Default"
            line.text  = alpha_tag + line.text

        # Save out
        with tempfile.NamedTemporaryFile(delete=False, suffix=".ass") as tmp_out:
            out_path = tmp_out.name
        subs.save(out_path)

        # Reply
        with open(out_path, "rb") as f:
            reply_name = os.path.splitext(filename)[0] + ".ass"
            update.message.reply_document(f, filename=reply_name)

    except Exception:
        logging.exception("Conversion failed")
        update.message.reply_text("❌ Conversion error—please try again.")
    finally:
        for p in (in_path, out_path):
            if p and os.path.exists(p):
                try: os.remove(p)
                except: pass

dp.add_handler(MessageHandler(Filters.document, handle_document))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
