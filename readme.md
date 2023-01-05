# Speach Bot Telegram

## Project URL [speech_bot_telegram](https://github.com/AntonAntonyuk/speech_bot_telegram)

This bot convert text written in English to Audio file and send it back.

### How to setup and use bot
1. Download code from [speech_bot_telegram](https://github.com/AntonAntonyuk/)
2. Download and install [python3](https://www.python.org/downloads/), in terminal switch to folder with downloaded code 
3. Create virtual environment
```
python3 -m venv venv
```
4. Install requirements
```
pip install -r requirements.txt
```
5. Create folder ***data*** . In this folder will be stored audio files. Files will be deleted after 30 seconds. If need to change this parameter change variable in voice.py in secondes
```
file_age = 30
``` 
6. Create bot in telegram with [botfather](https://t.me/botfather). After Bot creation you will have token to call Telegram API. 
7. Create file ***local_config.ini*** in root folder of your bot project and past token to this file.  
```
[telegram_bot]
token=past_your_token
```
8. run bot in terminal
```
python .\bot.py
```
9. Bot is ready. Send message to the Bot in Telegram.
10. To stop bot use *ctrl + c* (on windows\linux) and *Command + .*  (on Mac)
