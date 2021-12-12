import yaml

from src.LogHelper import Logger


class AppConfig:
    def __init__(self) -> None:
        super().__init__()
        with open("config.yaml", "r", encoding="utf8") as stream:
            config = yaml.safe_load(stream)
            self.from_chats = config['FROM_CHATS']
            self.to_chats = config['TO_CHATS']
            self.session = config['TELEGRAM_SESSION']
            self.api_id = config['API_ID']
            self.api_hash = config['API_HASH']

        Logger.configure()
