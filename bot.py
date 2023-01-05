import configparser
from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler, 
    Filters
    )
from voice import text_to_file

## read the configuration file
config = configparser.ConfigParser()
config.read('local_config.ini')
TOKEN = config['telegram_bot']['token']

def hello(update, context):
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def help_handler(update, context):
    help_text = """Please send message in english to the chat and I will translate it to the audio"""
    update.message.reply_text(help_text)

def reply(update, context):
    file_name = text_to_file(update.message.text)
    #update.message.reply_text("Your text: " + update.message.text) # can reply your text back
    update.message.reply_voice(voice=open(file_name, "rb"))


updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler("hello", hello))
updater.dispatcher.add_handler(CommandHandler("help", help_handler))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))

updater.start_polling()
updater.idle()