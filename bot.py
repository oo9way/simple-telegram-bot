import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

REPLY_KEYBOARDS = [
    ['Andijan'], ['Fergana'], ['Namangan'], ['Tashkent'], ['Sirdaryo'], ['Jizzakh'],
    ['Samarkand'], ['Qashqadaryo'], ['Surkhandarya'], ['Navoiy'], ['Bukhara'], ['Khorezm'],
    ['Karakalpakstan']
]


def start(update: Update, context: CallbackContext) -> int:
    """Starts the conversation and asks the user about their gender."""

    update.message.reply_text(
        'Weather Forecast',
        reply_markup=ReplyKeyboardMarkup(
            REPLY_KEYBOARDS
        ),
    )


def get_weather(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("6545930354:AAHhY_eh2rqs_mSrcFg60TWUoKCtohc9lFY")

    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, get_weather))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
