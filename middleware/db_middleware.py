from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from databases.database_main import Database
from databases.models import DutyLists


class DatabaseMiddleware(BaseMiddleware):
    def __init__(self, session: async_sessionmaker[AsyncSession]):
        self.session = session

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]) -> Any:
        async with self.session() as session:
            db = Database(session=session, duty_lists=DutyLists())
            data['db'] = db
            return await handler(event, data)
