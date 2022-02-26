from telegram.ext import CommandHandler, Updater
import handlers

# load bot token
with open('token.ini', 'r') as file:
    BOT_TOKEN = file.read()

# create bot
updater = Updater(token=BOT_TOKEN, use_context=True)

updater.dispatcher.add_handler(
    CommandHandler('start', handlers.start)
)

# start bot
updater.start_polling()
print('Bot Started')