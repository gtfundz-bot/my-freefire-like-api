import httpx
from flask import request
from app.generator import create_guest_account

TOKEN = "8952195204:AAG-PHHJQNxjp9I91ibgGYQAAKoSmk7UPjM"

@app.route(f"/{TOKEN}", methods=["POST"])
def telegram_webhook():
    update = request.get_json()
    if "message" in update and "text" in update["message"]:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"]["text"]
        
        if text.startswith("/start"):
            msg = "👋 Welcome! Send your Free Fire UID number directly to this chat to receive likes."
        elif text.isdigit():
            uid = text
            msg = f"⏳ Processing request... Creating guest account tokens and sending likes to UID: {uid}"
            
            # Triggers your automated profile generator logic
            account = create_guest_account()
            if account:
                msg = f"✅ Success! Generated Bot UID: {account['uid']}. Likes have been queued for Player ID {uid}."
            else:
                msg = "❌ Server error occurred while connecting to Garena auth servers. Please try again."
        else:
            msg = "⚠️ Invalid format. Please send a numeric Player UID only (e.g., 13219792011)."

        # Sends the response back to your Telegram app chat window
        httpx.post(f"https://telegram.org{TOKEN}/sendMessage", json={"chat_id": chat_id, "text": msg})
    return "OK", 200
     CONFIG = {
     "EUROPE": "europe_config.json",
    "IND": "ind_config.json",
    "BR": "br_config.json",

}
