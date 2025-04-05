from sqlalchemy import Select
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
