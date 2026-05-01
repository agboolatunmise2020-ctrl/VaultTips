import os
import random
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Replace with your actual token or use environment variables
TOKEN = os.getenv("8647346985:AAHxlUFBY4WiYlTWuVrpVX8mRG2M911PsR8")

QUOTES = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. – Winston Churchill",
    "Hardships often prepare ordinary people for an extraordinary destiny. – C.S. Lewis",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Your time is limited, so don't waste it living someone else's life. – Steve Jobs"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kb = [["/inspire"]]
    reply_markup = ReplyKeyboardMarkup(kb, resize_keyboard=True)
    await update.message.reply_text(
        "Welcome to Vault Access! Click the button below for your daily motivation.",
        reply_markup=reply_markup
    )

async def inspire(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quote = random.choice(QUOTES)
    await update.message.reply_text(f"✨ {quote}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("inspire", inspire))
    print("Bot is running...")
    app.run_polling()
