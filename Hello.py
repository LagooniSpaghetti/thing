from fastapi import FastAPI
from telegram import Bot
import asyncio

app = FastAPI()
BOT_TOKEN = "8674054335:AAH2kpOJ14Zg7Oq_Z1tqBTthxH4zaevNGmo"
CHAT_ID = "-1003725701854"

# Your original async function
async def send_alert_with_map():
    bot = Bot(token=BOT_TOKEN)
    message = "<b>Hello World</b> ⚠️\n"
    await bot.send_message(
        chat_id=CHAT_ID,
        text=message,
        parse_mode="HTML"
    )

# FastAPI endpoint
@app.get("/")
async def trigger_bot():
    await send_alert_with_map()
    return {"status": "Message sent"}
    