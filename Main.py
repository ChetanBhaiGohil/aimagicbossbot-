import openai
import telebot

# 🔐 તમારું Telegram BotFather ટોકન અહીં નાખો
TELEGRAM_TOKEN = 7722984877: AAERODEAy FF4u4QxevjchMptVS 1to1mUhw0
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# 🔐 તમારું OpenAI API Key અહીં નાખો
openai.api_key = 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

@bot.message_handler(commands=['start'])
def welcome(msg):
    bot.reply_to(msg, "👋 स्वागत है Boss! તમે કઈ Image ઈચ્છો છો? બસ Prompt મોકલો!")

@bot.message_handler(func=lambda message: True)
def generate_image(message):
    prompt = message.text
    try:
        response = openai.Image.create(prompt=prompt, n=1, size="512x512")
        image_url = response['data'][0]['url']
        bot.send_photo(message.chat.id, image_url)
    except Exception as e:
        bot.reply_to(message, f"❌ Error:\n{str(e)}")

bot.polling()
