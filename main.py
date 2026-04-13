from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

from flask import Flask
from threading import Thread

TOKEN = "8620222015:AAGFcoPd7GdfyQh2rowj8-wpkbnYX9l48Ok"
PASSWORD = "2019"

allowed_users = set()
media = []


# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id in allowed_users:
        await update.message.reply_text("Xush kelibsiz 😎")
    else:
        await update.message.reply_text("Parolni yoz:")


# PAROL
async def check_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id in allowed_users:
        return

    if update.message.text == PASSWORD:
        allowed_users.add(user_id)
        await update.message.reply_text("Kirish mumkin ✅")
    else:
        await update.message.reply_text("Parol xato ❌")


# MEDIA SAQLASH
async def save_media(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in allowed_users:
        return

    msg = update.message

    if msg.photo:
        media.append(("photo", msg.photo[-1].file_id))

    elif msg.video:
        media.append(("video", msg.video.file_id))

    elif msg.audio:
        media.append(("audio", msg.audio.file_id))

    elif msg.document:
        media.append(("file", msg.document.file_id))

    await msg.reply_text("Saqlandi ✅")


# MEDIA KO‘RISH (OBSHIY)
async def get_media(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in allowed_users:
        return

    if not media:
        await update.message.reply_text("Hech narsa yo‘q 😅")
        return

    for mtype, fid in media:
        if mtype == "photo":
            await update.message.reply_photo(fid)
        elif mtype == "video":
            await update.message.reply_video(fid)
        elif mtype == "audio":
            await update.message.reply_audio(fid)
        elif mtype == "file":
            await update.message.reply_document(fid)


# FLASK (24/7 uchun)
app_web = Flask("")


@app_web.route("/")
def home():
    return "Bot ishlayapti"


def run():
    app_web.run(host="0.0.0.0", port=8000)


def keep_alive():
    t = Thread(target=run)
    t.start()


# APP
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("media", get_media))
app.add_handler(MessageHandler(filters.TEXT, check_password))
app.add_handler(MessageHandler(filters.ALL, save_media))

keep_alive()
app.run_polling()
from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "I am alive"

def run():
    app.run(host='0.0.0.0', port=10000)

Thread(target=run).start()
