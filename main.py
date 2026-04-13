from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "I am alive"

def run():
    app.run(host='0.0.0.0', port=10000)

# Flaskni alohida threadda ishga tushuramiz
Thread(target=run).start()

# ===== BOT QISMI =====
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "TOKENINGNI_SHU_YERGA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot ishlayapti")

app_bot = ApplicationBuilder().token(TOKEN).build()
app_bot.add_handler(CommandHandler("start", start))

app_bot.run_polling()
