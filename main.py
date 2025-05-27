import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import pysubs2
from styles import ASS_STYLE, RESOLUTION

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Load environment
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    logger.error("BOT_TOKEN not found. Please set it in your .env file.")
    exit(1)


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hi! Send me an SRT or VTT subtitle file and I'll return a styled ASS version of it."
    )


def handle_subtitle_file(update: Update, context: CallbackContext):
    doc = update.message.document
    fname = doc.file_name
    ext = fname.split('.')[-1].lower()
    if ext not in ("srt", "vtt"):
        update.message.reply_text("🚫 Unsupported format. Please send an .srt or .vtt file.")
        return

    # Create temp dir
    os.makedirs("downloads", exist_ok=True)
    in_path = os.path.join("downloads", fname)
    out_path = os.path.join("downloads", f"{os.path.splitext(fname)[0]}.ass")

    # Download file
    doc.get_file().download(in_path)
    logger.info(f"Downloaded {fname} to {in_path}")

    # Load and convert
    subs = pysubs2.load(in_path, encoding="utf-8")
    # Set resolution
    subs.info["PlayResX"], subs.info["PlayResY"] = RESOLUTION
    # Clear existing styles, add ours
    subs.styles.clear()
    subs.styles[ASS_STYLE.name] = ASS_STYLE
    # Apply style to each line
    for line in subs:
        line.style = ASS_STYLE.name

    # Save ASS
    subs.save(out_path)
    logger.info(f"Saved ASS -> {out_path}")

    # Send back
    update.message.reply_document(document=open(out_path, 'rb'))


def error_handler(update: object, context: CallbackContext):
    logger.error(msg="Exception while handling an update:", exc_info=context.error)


def main():
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.document, handle_subtitle_file))
    dp.add_error_handler(error_handler)

    updater.start_polling()
    logger.info("Bot started. Waiting for files...")
    updater.idle()


if __name__ == '__main__':
    main()
