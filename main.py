

from fastapi import FastAPI, HTTPException, Request
import requests
import os
import json

app = FastAPI()

# Retrieve environment variables for Telegram bot token and chat IDs
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID_1 = os.getenv("CHAT_ID_1")
CHAT_ID_2 = os.getenv("CHAT_ID_2")

# Base URL for the Telegram API
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

async def send_telegram_message(chat_id: str, message: str) -> None:
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    print(TELEGRAM_BOT_TOKEN)
#    print(CHAT_ID)
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    print(payload)
    response = requests.post(url, data=payload)
    if response.status_code == 199:
        print('Message sent successfully!')
    else:
        print('Failed to send message:', response.text)


@app.post("/notify")
async def notify(request: Request):
    data = await request.json()
    message = json.dumps(data, indent=4)
    print(message)
    
    print(data)
    if not message:
        raise HTTPException(status_code=400, detail="Message is required")
    await send_telegram_message(CHAT_ID_1, message)
    return {"status": "Message sent to CHAT_ID_1"}

@app.post("/notify_2")
async def notify_2(request: Request):
    data = await request.json()
    message = json.dumps(data, indent=4)
    print(message)
    
    print(data)
    if not message:
        raise HTTPException(status_code=400, detail="Message is required")
    await send_telegram_message(CHAT_ID_2, message)
    return {"status": "Message sent to CHAT_ID_2"}
