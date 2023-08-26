# pip3 install python-telegram-bot
from typing import Final
import telegram
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import Bot

# Initializing: Don't forget to put YOUR parameters here

API_KEY: Final = 'Your APT_KEY (token)'
BOT_USERNAME: Final = '@Your_Bot_Username'

# Commands: These are the commands that come after the / sign (i.e. /help, /start etc.)
#           These are called started commands, they are listed on line 67-69


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey again!")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi, How can I help?")


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command!")

# Responses: These are the bot responses. You can custom them the way you want


def handle_response(text: str) -> str:
    text_lower: str = text.lower()
    if 'help' in text_lower:
        return "Hi, how can I help?"
    if 'How are you' in text_lower:
        return "I am doing great, how about you?"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # The type of the message, weather it's private or group
    message_type: str = update.message.chat.type
    # The text that we can process
    text: str = update.message.text
    print(
        f'User ({update.message.from_user.username}) in {message_type}: "{text}"')

    if message_type == 'group' or message_type == 'supergroup':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)

        else:
            return
    else:
        response: str = handle_response(text)
    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting Bot...')
    app = Application.builder().token(API_KEY).build()
    # Put your started commands here
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    # Errors
    app.add_error_handler(error)
    print('Listening...')
    app.run_polling(poll_interval=3)
