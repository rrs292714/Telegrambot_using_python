from asyncore import dispatcher
from cgitb import text
from telegram import *
from telegram.ext import *

bot= Bot("Your api key")
#print(bot.get_me())
updater=Updater("Your api key",use_context=True)

dispatcher=updater.dispatcher

def play_music(update=Update,context=CallbackContext):
   bot.send_message(
    chat_id=update.effective_chat.id,
    text="https://youtu.be/6RrEQJNZwPQ",
   )

start_value=CommandHandler('play',play_music)

print(bot.get_me())

dispatcher.add_handler(start_value)
updater.start_polling()