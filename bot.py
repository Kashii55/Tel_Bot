from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7876240812:AAHuWDVg2ZHFUeF8XiMw6ZXLo4_NX09y7-A"
# TOKEN = "7745588636:AAG1mw1zLByYCimVYUBRzbaLShk7plFnEHs"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    # Print the chat ID to your console
    print(f"Chat ID: {chat_id}")

    # (Optional) You can send a confirmation back to the user if you like:
    # await update.message.reply_text(f"Your chat ID is {chat_id}")

if __name__ == "__main__":
    
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot secsummary_bot is running...")
    app.run_polling()
