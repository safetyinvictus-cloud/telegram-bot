import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from flask import Flask
from threading import Thread

TOKEN = os.getenv("8620222015:AAGFcoPd7GdfyQh2rowj8-wpkbnYX9l48Ok")

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot ishlayapti"

def run_web():
    app.run(host="0.0.0.0", port=10000)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ishlayapman 😎")

def run_bot():
    app_bot = ApplicationBuilder().token(TOKEN).build()
    app_bot.add_handler(CommandHandler("start", start))
    app_bot.run_polling()

if name == "__main__":
    Thread(target=run_web).start()
    run_bot()
