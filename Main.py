import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Replace with your own bot token from @BotFather
BOT_TOKEN =

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to AI Boss Bot!\nSend me any prompt and I will generate an image!")

async def generate_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = update.message.text
    await update.message.reply_text("🖼️ Generating image... Please wait...")

    # Craiyon API (No API Key Needed)
    response = requests.post(
        "https://backend.craiyon.com/generate",
        json={"prompt": prompt}
    )
    data = response.json()
    if "images" in data:
        for img in data["images"]:
            img_bytes = bytes(img, 'utf-8')
            await update.message.reply_photo(photo=f"data:image/png;base64,{img}")
    else:
        await update.message.reply_text("❌ Failed to generate image.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, generate_image))
    app.run_polling()
