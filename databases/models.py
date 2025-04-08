from sqlalchemy import Select, insert, update
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column

from databases.base import Base


class Schedule(Base):
    __tablename__ = 'schedule'
    id: Mapped[int] = mapped_column(primary_key=True)
    id_chat: Mapped[str] = mapped_column(nullable=False)
    duty_persons: Mapped[dict] = mapped_column(JSONB(none_as_null=True), nullable=False)

    async def get_all_duty_persons(self, id_chat: str, session: AsyncSession):
        statement = Select(Schedule.duty_persons).where(Schedule.id_chat == id_chat)
        result = await session.execute(statement)
        return result.scalars().all()

    async def add_pair(self, id_chat: str, pairs: dict[int: str], session: AsyncSession):
        if not await self.get_all_duty_persons(id_chat, session):
            statement = insert(Schedule).values(id_chat=id_chat, duty_persons=pairs)
        else:
            statement = update(Schedule).values(id_chat=id_chat, duty_persons=pairs)
        await session.execute(statement)
        await session.commit()
