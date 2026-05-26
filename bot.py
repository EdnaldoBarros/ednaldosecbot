from openai import OpenAI
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from dotenv import load_dotenv
import asyncio
import os

# Carrega o .env
load_dotenv()

# Token
TOKEN = os.getenv("BOT_TOKEN")

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key=OPENAI_API_KEY
)

# Bot
bot = Bot(token=TOKEN)

# Dispatcher
dp = Dispatcher()

# Menu inline
menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="💻 GitHub",
                url="https://github.com/EdnaldoBarros"
            )
        ],
        [
            InlineKeyboardButton(
                text="🔗 LinkedIn",
                url="https://www.linkedin.com/in/ednaldo-barros-da-silva-0209019b"
            )
        ],
        [
            InlineKeyboardButton(
                text="🛡 Cyber Projects",
                callback_data="cyber"
            )
        ]
    ]
)

# Comando /start
@dp.message(Command("start"))
async def start(message: types.Message):

    texto = """
🤖 Welcome to EdnaldoSecBot

🛡 Cyber Defense
💻 FullStack Engineering
🚀 Automation & AI

Choose an option below:
"""

    await message.answer(
        texto,
        reply_markup=menu
    )

# Callback dos botões
@dp.callback_query()
async def callbacks(callback: types.CallbackQuery):

    if callback.data == "cyber":

        await callback.message.answer(
            "🚀 Cybersecurity projects coming soon."
        )

# Inicialização
async def main():

    print("🤖 Bot online...")

    await dp.start_polling(bot)



# Help
@dp.message(Command("help"))
async def help(message: types.Message):

    texto = """🤖 EdnaldoSecBot - Help
    Available Commands 
    /start - Start bot
    /help - Show this help message
    /ping - Sever status
    /about - About project
    """

    await message.answer(texto)

# Ping
@dp.message(Command("ping"))
async def ping(message: types.Message):

    await message.answer(
        "🏓 Pong! bot is online."
    )

# About
@dp.message(Command("about"))
async def about(message: types.Message):

    texto = """
🤖 EdnaldoSecBot

Cyber Defense +  FullStack Engineering + AI

Built by Ednaldo Barros
"""

    await message.answer(texto)

@dp.message(Command("ask"))
async def ask_ai(message: types.Message):

    try:

        resposta = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "user",
                    "content": "Hello"
                }
            ]
        )

        texto = resposta.choices[0].message.content

        await message.answer(texto)

    except Exception as e:

        await message.answer(
            f"❌ Error:\n{e}"
        )

# Execução
if __name__ == "__main__":
    asyncio.run(main())