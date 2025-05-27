import os
import tempfile
from flask import Flask, request, Response
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
import pysubs2

# ─── CONFIG ─────────────────────────────────────────────
BOT_TOKEN   = os.environ["BOT_TOKEN"]
# e.g. https://<your-app>.koyeb.app
BASE_URL    = os.environ["WEBHOOK_URL"].rstrip("/")
PORT        = int(os.environ.get("PORT", 8080))
STYLE_NAME  = "TwCEN"

# Your ASS style parameters, matching your Aegisub screenshot
YOUR_STYLE = pysubs2.SSAStyle(
    fontname        = "Tw Cen MT Condensed Extra Bold",
    fontsize        = 36,
    primarycolor    = "&H00FFFFFF",  # white
    secondarycolor  = "&H000000FF",  # red (BGR hex)
    outlinecolor    = "&H00000000",  # black
    backcolor       = "&H00000000",  # shadow color
    bold            = False,
    italic          = False,
    underline       = False,
    strikeout       = False,
    scale_x         = 112,
    scale_y         = 75,
    spacing         = 0,
    angle           = 0,
    borderstyle     = 1,
    outline         = 0,
    shadow          = 0,
    alignment       = 5,   # centered bottom
    margin_l        = 15,
    margin_r        = 15,
    margin_v        = 11,
)

# ─── FLASK SETUP ────────────────────────────────────────
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Subtitle-bot is running!"

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    """Receive update from Telegram, forward to the dispatcher."""
    json_data = request.get_json(force=True)
    update = Update.de_json(json_data, bot_app.bot)
    bot_app.update_queue.put(update)
    return Response("OK", status=200)

# ─── TELEGRAM HANDLERS ──────────────────────────────────
async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Send me an .srt or .vtt file, and I'll return a styled .ass for you!"
    )

async def convert_subs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    doc = update.message.document
    if not doc or not doc.file_name.lower().endswith((".srt", ".vtt")):
        return await update.message.reply_text("❌ Please send a .srt or .vtt file.")

    # download the incoming file to a temp dir
    with tempfile.TemporaryDirectory() as tmp:
        in_path  = os.path.join(tmp, doc.file_name)
        out_path = os.path.splitext(in_path)[0] + ".ass"

        # fetch file from Telegram
        f = await doc.get_file()
        await f.download_to_drive(in_path)

        # load, inject style & resolution, save
        subs = pysubs2.load(in_path)
        subs.styles[STYLE_NAME] = YOUR_STYLE
        subs.info["PlayResX"] = "1920"
        subs.info["PlayResY"] = "1080"
        subs.save(out_path)

        # send result back
        await update.message.reply_document(open(out_path, "rb"))

# ─── DISPATCHER INIT & WEBHOOK SETUP ────────────────────
bot_app = ApplicationBuilder().token(BOT_TOKEN).build()
bot_app.add_handler(CommandHandler("start", start_cmd))
bot_app.add_handler(MessageHandler(filters.Document.ALL, convert_subs))

def set_webhook_and_run():
    webhook_url = f"{BASE_URL}/{BOT_TOKEN}"
    bot_app.bot.set_webhook(webhook_url)
    # start Flask
    app.run(host="0.0.0.0", port=PORT)

if __name__ == "__main__":
    set_webhook_and_run()
