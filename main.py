#!/usr/bin/env python3
import os
import tempfile
import logging

from flask import Flask, request, abort
from dotenv import load_dotenv
import pysubs2

from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Dispatcher,
    MessageHandler,
    Filters,
    CommandHandler,
    CallbackQueryHandler,
)

from styles import STYLES  # <-- your theme registry

# Load env – Koyeb injects BOT_TOKEN & WEBHOOK_URL
load_dotenv()
BOT_TOKEN   = os.environ.get("BOT_TOKEN")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")
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

# ─── In-memory store of each chat's chosen theme ──────────────────
user_selected_theme = {}  # defaults to "Pikasub" if never set

# ─── /setting command to pick your theme ─────────────────────────
def settings_command(update, context):
    keyboard = [
        [InlineKeyboardButton(name, callback_data=f"set_theme|{name}")]
        for name in STYLES.keys()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Choose a subtitle style:", reply_markup=reply_markup)

# ─── Callback when a theme button is pressed ────────────────────
def theme_callback(update, context):
    query = update.callback_query
    query.answer()
    _, theme_name = query.data.split("|", 1)

    if theme_name not in STYLES:
        query.edit_message_text("❌ Unknown style.")
        return

    chat_id = query.message.chat_id
    user_selected_theme[chat_id] = theme_name
    query.edit_message_text(f"✅ Style set to *{theme_name}*", parse_mode="Markdown")

def handle_document(update, context):
    doc      = update.message.document
    filename = doc.file_name
    ext      = os.path.splitext(filename)[1].lower()

    if ext not in (".srt", ".vtt"):
        return update.message.reply_text("🚫 Please send a .srt or .vtt file.")

    in_path = out_path = None
    try:
        # Download incoming file
        with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp_in:
            in_path = tmp_in.name
        bot.getFile(doc.file_id).download(custom_path=in_path)

        # Load subtitles
        subs = pysubs2.load(in_path)

        # Force 1920×1080 resolution
        subs.info["PlayResX"] = "1920"
        subs.info["PlayResY"] = "1080"

        # Figure out which theme this chat has chosen
        chat_id = update.message.chat_id
        theme   = user_selected_theme.get(chat_id, "Pikasub")
        styles  = STYLES.get(theme, [])

        # Register each style under its .name
        for style in styles:
            subs.styles[style.name] = style

        # ─── Theme‐specific logic ─────────────────────────────────────
        if theme == "Pikasub":
            # 1) Prepend your “site” event (0→5min)
            site_tag = r"{\fad(4000,3000)\fn@Arial Unicode MS\fs31.733"\
                       r"\c&H00FFFFFF&\alpha&H99&\b1\a1\fscy60}"
            start_ms = 0
            end_ms   = 5 * 60 * 1000
            site_event = pysubs2.SSAEvent(
                start=start_ms,
                end=end_ms,
                style="site",
                text=site_tag + "PikaSub.com"
            )
            subs.events.insert(0, site_event)

            # 2) Apply Default to the rest
            for line in subs.events[1:]:
                line.style = "Default"

        elif theme == "Shrouding The Heavens":
            # 1) Insert Telegram event from 0 → first subtitle start
            if subs.events:
                first_start = subs.events[0].start
            else:
                first_start = 0
            telegram_event = pysubs2.SSAEvent(
                start=0,
                end=first_start,
                style=styles[0].name,
                text="Telegram :- Facky_Hindi_Donghua"
            )
            subs.events.insert(0, telegram_event)

            # 2) Apply the Shrouding style to every other line
            for line in subs.events[1:]:
                line.style = styles[0].name

        else:
            # Fallback for any future styles: just apply the first style
            for line in subs.events:
                line.style = styles[0].name

        # ─── Now apply semi-transparent tag to *all* lines ────────────
        alpha_tag = r"{\4a&H96&}"
        for line in subs.events:
            line.text = alpha_tag + line.text

        # Save out to .ass
        with tempfile.NamedTemporaryFile(delete=False, suffix=".ass") as tmp_out:
            out_path = tmp_out.name
        subs.save(out_path)

        # Reply with converted file
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

# ─── Register handlers ─────────────────────────────────────────────
dp.add_handler(CommandHandler("setting", settings_command))
dp.add_handler(CallbackQueryHandler(theme_callback, pattern=r"^set_theme\|"))
dp.add_handler(MessageHandler(Filters.document, handle_document))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
