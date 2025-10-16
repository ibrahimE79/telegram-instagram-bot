echo "" > downloader_bot.py
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import requests

# 🧾 توکن ربات دانلود را اینجا قرار بده
BOT_TOKEN = "8499048158:AAEL3GphtVvEN-ebAq5a4vSbOX0Ru72eXTY"

# 🧩 آیدی عددی گروه ها
GROUP_1_ID = 1003009862668
GROUP_2_ID = 1002964524418

# 🖇 دکمه تایید عضویت
def get_membership_keyboard():
    keyboard = [
        [InlineKeyboardButton("✅ عضو شدم", callback_data='check_membership')]
    ]
    return InlineKeyboardMarkup(keyboard)

# بررسی عضویت
async def check_membership(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user = query.from_user

    chat_member1 = await context.bot.get_chat_member(GROUP_1_ID, user.id)
    chat_member2 = await context.bot.get_chat_member(GROUP_2_ID, user.id)

    if chat_member1.status in ["member", "administrator", "creator"] and chat_member2.status in ["member", "administrator", "creator"]:
        await query.answer("✅ عضویت تایید شد. می‌توانید لینک اینستاگرام را ارسال کنید.")
        # اینجا می‌تونی حالت آماده دریافت لینک را فعال کنی
    else:
        await query.answer("❌ ابتدا باید در هر دو گروه عضو شوید.")

# دستور start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام! قبل از دانلود پست یا ریلز اینستاگرام، ابتدا باید در گروه‌ها عضو شوید.",
        reply_markup=get_membership_keyboard()
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(check_membership, pattern="check_membership"))

if __name__ == "__main__":
    print("👀 Downloader bot is running...")
    app.run_polling()

