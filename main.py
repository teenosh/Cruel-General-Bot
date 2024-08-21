from token import AWAIT
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, Application

TOKEN: Final = 'token <3'
BOT_USERNAME: Final = '@Cruel_General_Bot'

# commands

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Nice day to do some exercises, isn`t it? 20 push-ups right now and you are done... fro now at least.')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am a Chief General bot of AITU Computer Science group,with no mercy to anyone.')

async def special_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Special command')

# responses

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'Добро утро' in processed:
        return 'Доброе утро!'

    if 'Changan' in processed:
        return 'Чанган лох!'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.username}) in {message_type}: {text}')

    if message_type == 'group':
        if 'Разрешите обратиться' in text:
            new_text: str = text.replace('Разрешите обратиться', '').strip()
            response = handle_response(new_text)
        else:
            return
    else:
        response = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('startt', start_command))
    app.add_handler(CommandHandler('helpls', help_command))
    app.add_handler(CommandHandler('special', special_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Error
    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=3)
