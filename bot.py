import telebot
import instaloader

# -------------------
# CONFIGURATION
# -------------------
BOT_TOKEN = "ENTER YOUR BOT TOKEN"
CHANNEL_USERNAME = "@lifeonbots"
bot = telebot.TeleBot(BOT_TOKEN)
# -------------------

# Instaloader instance
L = instaloader.Instaloader()

# Welcome message on /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = f"""
IG tool working 
➡️ Also join our channel: {CHANNEL_USERNAME}

Send Insta username 
(Ex: @the_aadarshtiwari)
"""
    bot.reply_to(message, welcome_text)

# Fetch Instagram profile
def get_instagram_profile(username):
    username = username.strip().lstrip("@")
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        full_name = profile.full_name or "N/A"
        bio = profile.biography or "N/A"
        followers = profile.followers
        following = profile.followees
        posts = profile.mediacount

        return f"""
📸 Instagram Profile Info

👤 Name / नाम: {full_name}
🔗 Username / यूज़रनेम: @{username}
📝 Bio / बायो: {bio}
👥 Followers / फॉलोअर्स: {followers}
👤 Following / फॉलोइंग: {following}
📷 Posts / पोस्ट्स: {posts}

➡️ Also join our channel: {CHANNEL_USERNAME}
"""
    except Exception as e:
        return f"❌ Profile not found / प्रोफाइल नहीं मिली.\nError: {str(e)}"

# Handle messages (username input)
@bot.message_handler(func=lambda m: True)
def handle_message(message):
    username = message.text.strip()
    if username.startswith("/start"):
        return  # already handled
    if username == "":
        bot.reply_to(message, "❌ Please send a valid Instagram username / सही यूज़रनेम भेजें।")
        return

    bot.reply_to(message, "⏳ Fetching profile info... / जानकारी ला रहे हैं...")
    info = get_instagram_profile(username)
    bot.reply_to(message, info)

print("🤖 Instagram Profile Info Bot is running...")
bot.infinity_polling()
