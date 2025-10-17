echo "" > downloader_bot.py
It looks like this message is in Persian
import os
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# ===================== تنظیمات =====================
TOKEN = os.getenv("8499048158:AAEL3GphtVvEN-ebAq5a4vSb0X0Ru72eXTY ")  # توکن ربات دانلود
API1_KEY = os.getenv(" eb7ae308c3mshbfbe772ba10c139p14a8dcjsnb858b563daf1")
API1_HOST = "instagram120.p.rapidapi.com"
API2_KEY = os.getenv(" b89b7fea3dmshed191c6121e2cc1p144933jsne66555b96eca' \")
API2_HOST = " instagram120.p.rapidapi.com"

MEMBERSHIP_CHECK_URL = "https://your-membership-bot-url.onrender.com/check"  # آدرس وب‌هوک ربات عضویت
# ====================================================

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "سلام 👋 لینک پست یا ریلز اینستاگرام را بفرست تا برایت دانلود کنم.\n"
        "⚠️ قبل از دانلود، عضویت شما در دو گروه بررسی می‌شود."
    )

def check_membership(user_id):
    """ارتباط با ربات بررسی عضویت"""
    try:
        res = requests.get(f"{MEMBERSHIP_CHECK_URL}?user_id={user_id}", timeout=5)
        data = res.json()
        return data.get("is_member", False)
    except Exception as e:
        print("Membership check error:", e)
        return False

def download_instagram(url):
    """تلاش برای دانلود با دو API مختلف"""
    try:
        headers1 = {
            "X-RapidAPI-Key": API1_KEY,
            "X-RapidAPI-Host": API1_HOST
        }
        r1 = requests.get(f"https://{API1_HOST}/api/instagram/post", headers=headers1, params={"url": url})
        if r1.status_code == 200:
            data = r1.json()
            return data.get("media") or data.get("download_url")
    except:
        pass

    try:
        headers2 = {
            "X-RapidAPI-Key": API2_KEY,
            "X-RapidAPI-Host": API2_HOST
        }
        r2 = requests.get(f"https://{API2_HOST}/api/instagram/post", headers=headers2, params={"url": url})
        if r2.status_code == 200:
            data = r2.json()
            return data.get("media") or data.get("download_url")
    except:
        pass

    return None

def handle_message(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    if not check_membership(user_id):
        update.message.reply_text("❌ شما هنوز عضو هر دو گروه نیستید. لطفاً ابتدا عضو شوید.")
        return

    url = update.message.text.strip()
    update.message.reply_text("🔄 در حال پردازش لینک...")
    link = download_instagram(url)
    if link:
        update.message.reply_text(f"✅ لینک دانلود آماده است:\n{link}")
    else:
        update.message.reply_text("⚠️ خطا در دانلود. لطفاً دوباره تلاش کنید.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

TOKEN = "8499048158:AAEL3GphtVvEN-ebAq5a4vSb0X0Ru72eXTY "
API1_KEY = " eb7ae308c3mshbfbe772ba10c139p14a8dcjsnb858b563daf1"
API1_HOST = "مقدارinstagram120.p.rapidapi.com"
API2_KEY = " b89b7fea3dmshed191c6121e2cc1p144933jsne66555b96eca' \"
API2_HOST = "instagram120.p.rapidapi.com"

