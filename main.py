import sys
import os
from pyrogram import Client, filters

from src.AppConfig import AppConfig
from src.LogHelper import Logger
from src.telegram_client import TelegramClient

app_config = AppConfig()
app = Client(name="telegram_forwarder", session_string=app_config.session, api_id=app_config.api_id, api_hash=app_config.api_hash)
telegram_client = TelegramClient(app)

from_chats = telegram_client.get_formatted_chats(app_config.from_chats)
Logger.info(f"From chats - {from_chats}")
to_chats = telegram_client.get_formatted_chats(app_config.to_chats)
Logger.info(f"To chats - {to_chats}")


@app.on_message(filters.chat(from_chats) & filters.incoming)
def run(client, message):
    Logger.info(f"Message Incoming - from {message.sender_chat.title}")
    try:
        for chat in to_chats:
            Logger.info(message)
            if not message.chat.has_protected_content:
                message.forward(chat)
            else:
                app.send_message(chat_id=chat, text=message.text)
    except Exception as e:
        Logger.error(e)

app.run()
