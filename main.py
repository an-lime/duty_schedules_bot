import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config_data.config import BotConfig, load_config
from handlers.main_commands_handler import router_standard_command
from handlers.other_handler import router_other_command
from keyboards.main_menu_keyboard import set_main_menu
from lexicon.main_lexicon import MAIN_BOT_LEXICON
from middleware.db_middleware import DatabaseMiddleware

logging.basicConfig(level=logging.INFO,
                    format='%(filename)s: [%(funcName)s] %(lineno)d #%(levelname)-8s '
                           '[%(asctime)s] - %(name)s - %(message)s')

logger = logging.getLogger(__name__)


async def main():
    logger.info('Bot started...')

    config: BotConfig = load_config()
    engine = create_async_engine(url=config.Database.url)
    session = async_sessionmaker(bind=engine, expire_on_commit=False)

    storage = MemoryStorage()

    bot: Bot = Bot(token=config.Bot.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
    await bot.set_my_description(MAIN_BOT_LEXICON['bot_description'])
    await bot.set_my_short_description(MAIN_BOT_LEXICON['bot_short_description'])
    await set_main_menu(bot)

    dp: Dispatcher = Dispatcher(storage=storage)

    dp.include_router(router_standard_command)
    dp.include_router(router_other_command)

    dp.update.middleware(DatabaseMiddleware(session=session))

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
