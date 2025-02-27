import telegram
from telegram.ext import Updater, MessageHandler, Filters
import logging

def main():
    updater = Updater(token='7638284687:AAEGZOBwubJvuMz7Z_CvdB_4HkwPQZE0XfQ', use_context=True)
    dispatcher = updater.dispatcher
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)
    updater.start_polling()
    updater.idle()

def echo(update, context):
    reply_message = update.message.text.upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=reply_message)

if __name__ == '__main__':
    main()
