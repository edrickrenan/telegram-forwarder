import sys

from pyrogram import Client

from src.LogHelper import Logger


def is_int(value) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False


class TelegramClient:

    def __init__(self, app: Client) -> None:
        super().__init__()
        self.app = app

    def get_formatted_chats(self, chats):
        formatted_chats = []
        for chat in chats:
            try:
                if is_int(chat):
                    formatted_chats.append(int(chat))
                else:
                    formatted_chats.append(self.__get_chat_id(chat))
            except Exception as e:
                Logger.error(e)
                sys.exit(1)
        return formatted_chats

    def __get_chat_id(self, chat) -> int:
        if chat.startswith("@"):
            return self.app.get_chat(chat.replace("@", "")).id
        elif chat.startswith("https://t.me/c/") or chat.startswith(
                "https://telegram.org/c/") or chat.startswith("https://telegram.dog/c/"):
            chat_id = chat.split("/")[4]
            if is_int(chat_id):
                chat_id = "-100" + str(chat_id)
                return int(chat_id)
            else:
                return self.app.get_chat(chat_id).id
