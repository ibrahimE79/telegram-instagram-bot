echo "" > membership_bot.py

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

BOT_TOKEN = "8292271135:AAG6QmZQGeXBW5UNs3XPXZdv1bazQe_e5KU"
GROUP_1_ID = -1003009862668  # گروه تجاری
GROUP_2_ID = -1002964524418  # گروه آشپزی

def start(update: Update, context: CallbackContext):
    update.message.reply_text("سلام! عضویت شما در گروه‌ها بررسی می‌شود...")

def verify_membership(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    bot = context.bot
    member1 = bot.get_chat_member(GROUP_1_ID, user_id)
    member2 = bot.get_chat_member(GROUP_2_ID, user_id)

    if member1.status != "left" and member2.status != "left":
        update.message.reply_text("✅ شما عضو هر دو گروه هستید.")
    else:
        update.message.reply_text("❌ شما عضو هر دو گروه نیستید.")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("verify", verify_membership))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

BOT_TOKEN = "8292271135:AAG6QmZQGeXBW5UNs3XPXZdv1bazQe_e5KU"
GROUP_ID_1 = "-1003009862668"
GROUP_ID_2 = "-1002964524418"
