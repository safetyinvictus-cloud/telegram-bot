import os
import asyncio
from flask import Flask
from threading import Thread

# ===== FLASK (Render uchun alive) =====
app = Flask(__name__)

@app.route('/')
def home():
    return "I am alive"

def run():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

Thread(target=run).start()

# ===== TELEGRAM BOT =====
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8620222015:AAGFcoPd7GdfyQh2rowj8-wpkbnYX9l48Ok"  # 👉 shu joyga token qo‘y

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot ishlayapti 🚀")

async def main():
    app_bot = ApplicationBuilder().token(TOKEN).build()
    app_bot.add_handler(CommandHandler("start", start))
    await app_bot.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
