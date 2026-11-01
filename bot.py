import os
import telebot

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, "Ami Online! 24h Hosting e cholche 🔥")

@bot.message_handler(func=lambda m: True)
def echo(m):
    bot.reply_to(m, m.text)

print("Bot chalu holo...")
bot.infinity_polling()
