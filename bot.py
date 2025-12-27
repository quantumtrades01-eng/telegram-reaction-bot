import asyncio
import random
import os
from telegram import Update, ReactionTypeEmoji
from telegram.ext import ApplicationBuilder, ContextTypes, ChannelPostHandler

# Read bot token from Render environment variable
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable is not set")

# Emojis to react with
EMOJIS = ["❤️", "🔥", "🚀", "😄"]

async def react_to_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.channel_post
    if not message:
        return

    # Random delay to look natural
    await asyncio.sleep(random.randint(2, 8))

    reactions = [ReactionTypeEmoji(emoji=e) for e in EMOJIS]

    await context.bot.set_message_reaction(
        chat_id=message.chat_id,
        message_id=message.message_id,
        reaction=reactions
    )

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(ChannelPostHandler(react_to_post))
    print("🤖 Reaction Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
