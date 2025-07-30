
import telebot
from telebot import types
import os

# It's recommended to load the token from environment variables
# for better security. For example:
# TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
# If you do this, make sure to set the environment variable in your system.
# এখানে আপনার নতুন টোকেন বসান
TOKEN = "7557122198:AAH4i4uGez08TA2cLqcbnG_MOoqV8nlfOz8"
bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

# Remove webhook, it conflicts with polling
bot.delete_webhook()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Handles the /start command and sends a welcome message."""
    text = """
<b>🔔 সকল TikTok সেলিব্রিটিদের ভাইরাল ভিডিও সবার আগে দেখতে চান?</b>

👉 তাহলে নিচের চ্যানেল ও গ্রুপগুলোতে <b>এখনই জয়েন করুন</b> এবং সবার আগে এক্সক্লুসিভ ভিডিও লিংক পেতে থাকুন:

⏳ <b>সময় নষ্ট না করে এখনই জয়েন করুন এবং ভাইরাল জগতে প্রবেশ করুন!</b>
    """
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("📌 Channel ", url="https://t.me/+vJ_xDonMR91mMjRl")
    btn2 = types.InlineKeyboardButton("💬 Group ", url="https://t.me/+saMgMeq1TP85NTc1")
    btn3 = types.InlineKeyboardButton("▶️ Viral Video Link", url="https://t.me/viralvideosu_bot/Watch")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.message_handler(commands=['help'])
def send_help(message):
    """Handles the /help command and sends a help message."""
    help_text = (
        "<b>Bot Help</b>\n\n"
        "Here are the available commands:\n"
        "/start - Shows the welcome message with channel links.\n"
        "/help - Shows this help message.\n\n"
        "Any other message will be echoed back to you."
    )
    bot.send_message(message.chat.id, help_text)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    """Echoes back all other text messages."""
    bot.reply_to(message, message.text)


print("Bot is running...")
bot.infinity_polling()
