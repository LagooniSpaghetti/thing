from telegram import Bot

bot = Bot(token="8674054335:AAH2kpOJ14Zg7Oq_Z1tqBTthxH4zaevNGmo")

def send_alert_sync():
    bot.send_message(chat_id="-1003725701854", text="Hello World")  # synchronous version

send_alert_sync()