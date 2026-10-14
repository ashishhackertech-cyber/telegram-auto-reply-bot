import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(level=logging.INFO)

# Cloud ke environment variable se token uthayega
BOT_TOKEN = os.getenv("8965802203:AAE3Ttoz7Ie7ed-9mTKSGOHlA6hgGEAOK1w")

ADMIN_IDS = [8940352048]

SERIES_DB = {
    "primordial god": {
        "name": "Primordial God",
        "photo": "https://telegra.ph/file/default_image.jpg",
        "caption": "🔥 All episodes available!\nJoin: https://t.me/primordial_channel"
    }
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot active hai! Group me series ka naam likho.")

async def reply_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text.lower()
    for key, data in SERIES_DB.items():
        if key in text:
            msg = f"🎬 **Series:** {data['name']}\n\n{data['caption']}"
            try:
                await update.message.reply_photo(photo=data['photo'], caption=msg, parse_mode="Markdown")
            except Exception:
                await update.message.reply_text(msg, parse_mode="Markdown")
            break

def main():
    if not BOT_TOKEN:
        print("Error: BOT_TOKEN nahi mila!")
        return

    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), reply_handler))
    print(">>> BOT READY HAI CLOUD PAR! <<<")
    app.run_polling()

if __name__ == "__main__":
    main()
