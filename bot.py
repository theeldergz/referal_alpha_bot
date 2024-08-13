import os
import asyncio
import logging
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv, find_dotenv

from handlers import message_routes


# Запуск бота
async def main():
    load_dotenv(find_dotenv())
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_routers(message_routes.router)
    # Альтернативный вариант регистрации роутеров по одному на строку
    # dp.include_router(questions.router)
    # dp.include_router(different_types.router)

    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
