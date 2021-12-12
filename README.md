# Telegram Message Forwarder
A python app which forwards Telegram messages from channels, groups or chats to other channels, groups or chats automatically.

### Configuration
To use this app you will need to copy or rename `config.yaml.sample` to `config.yaml` and populate the following variables:
- `API_ID` - You can create one on [https://my.telegram.org](https://my.telegram.org)
- `API_HASH` - You can create one on [https://my.telegram.org](https://my.telegram.org)
- `TELEGRAM_SESSION` - Can be generated using the `generate_session.py` script
- `FROM_CHATS` - The chat ids from which messages will be forwarded
- `TO_CHATS` - The chat ids that will receive the forwarded messages

### Installing Requirements
Install the required Python Modules in your machine.
```
pip3 install -r requirements.txt
```
### Running the app
With python3.9 or later.
```
python3 main.py
```