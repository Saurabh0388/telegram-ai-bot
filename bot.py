import os
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from telegram import Update
from ai_replies import get_ai_reply

BOT_TOKEN = os.getenv("BOT_TOKEN")
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    message = update.message.text
    reply = get_ai_reply(message, user_id)
    await update.message.reply_text(reply)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
