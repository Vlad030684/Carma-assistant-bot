from flask import Flask, request
import telegram
import os

TOKEN = os.environ.get("BOT_TOKEN")
BOT_USERNAME = os.environ.get("BOT_USERNAME") or "carma_auto_bot"
BASE_URL = f"https://{BOT_USERNAME}.onrender.com"

bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

@app.route(f"/webhook/{TOKEN}", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    message = update.message.text.lower()

    if "продать" in message:
        bot.send_message(chat_id=chat_id, text="Отлично! Отправьте, пожалуйста, информацию об автомобиле: марка, модель, год, пробег, состояние и ваши ожидания по цене.")
    else:
        bot.send_message(chat_id=chat_id, text="Привет! Я — Carma Assistant. Напишите 'хочу продать машину' или задайте вопрос по авто.")

    return "ok"

@app.route("/")
def index():
    return "Carma bot is running."

if __name__ == "__main__":
    app.run(debug=True)
