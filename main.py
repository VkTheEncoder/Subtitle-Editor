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
    CommandHandler,
    CallbackQueryHandler,
    Filters,
)

from styles import STYLES  # <-- import the themes registry

# ─── In-memory store of each chat’s selected theme ─────────────────
# Keys are chat_id (int), values are one of STYLES.keys()
user_selected_theme = {}

# Load env – BOT_TOKEN, WEBHOOK_URL, PORT, etc.
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
PORT = int(os.getenv("PORT", "5000"))

bot = Bot(token=BOT_TOKEN)
app = Flask(__name__)
dispatcher = Dispatcher(bot, None, workers=0, use_context=True)

# ─── /setting command ──────────────────────────────────────────────
def settings_command(update, context):
    """Show a button for each available theme."""
    keyboard = [
        [InlineKeyboardButton(name, callback_data=f"set_theme|{name}")]
        for name in STYLES.keys()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Choose a subtitle style:", reply_markup=reply_markup)

# ─── Callback when a theme button is tapped ───────────────────────
def theme_callback(update, context):
    query = update.callback_query
    query.answer()
    data = query.data  # e.g. "set_theme|Pikasub"
    _, theme_name = data.split("|", 1)

    if theme_name not in STYLES:
        query.edit_message_text("❌ Unknown style.")
        return

    chat_id = query.message.chat_id
    user_selected_theme[chat_id] = theme_name
    query.edit_message_text(f"✅ Style set to *{theme_name}*", parse_mode="Markdown")

# ─── Modified document handler ────────────────────────────────────
def handle_document(update, context):
    chat_id = update.message.chat_id
    in_doc = update.message.document
    # download incoming file
    in_path = tempfile.mktemp(suffix=os.path.splitext(in_doc.file_name)[1])
    out_path = tempfile.mktemp(suffix=".ass")

    in_doc.get_file().download(in_path)

    # Which theme to apply? Default to first in STYLES:
    theme_name = user_selected_theme.get(chat_id, next(iter(STYLES)))
    styles_to_apply = STYLES[theme_name]

    try:
        subs = pysubs2.load(in_path)
        # apply each style in the chosen theme:
        for style in styles_to_apply:
            for line in subs:
                line.style = style.name  # assign by name
            subs.styles[style.name] = style

        # If you have theme-specific quirks—e.g. only Pikasub adds an extra line:
        if theme_name == "Pikasub":
            for idx, line in enumerate(subs):
                subs.insert(idx + 1, pysubs2.SSAEvent(
                    start=line.start + 10, end=line.end + 10,
                    text="Your extra Pikasub line", style=styles_to_apply[0].name
                ))

        subs.save(out_path)

        with open(out_path, "rb") as f:
            reply_name = f"{os.path.splitext(in_doc.file_name)[0]}_{theme_name}.ass"
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
dispatcher.add_handler(CommandHandler("setting", settings_command))
dispatcher.add_handler(CallbackQueryHandler(theme_callback, pattern=r"^set_theme\|"))
dispatcher.add_handler(MessageHandler(Filters.document, handle_document))

# ─── Flask webhook endpoint ────────────────────────────────────────
@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "OK"

if __name__ == "__main__":
    # set your webhook somewhere, then run
    app.run(host="0.0.0.0", port=PORT)
