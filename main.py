from fastapi import FastAPI, Request
import requests
import os
import json
# from dotenv import load_dotenv
# load_dotenv()

app = FastAPI()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")  # Your Telegram chat ID

@app.post("/notify")
async def notify(request: Request):
    data = await request.json()
    # message = data.get("message", "No message provided")
    # print(messagel)
    message = json.dumps(data, indent=4)
    print(message)
    
    print(data)
    send_telegram_message(message)
    return {"status": "success"}

def send_telegram_message(message: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    print(TELEGRAM_TOKEN)
    print(CHAT_ID)
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    print(payload)
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print('Message sent successfully!')
    else:
        print('Failed to send message:', response.text)