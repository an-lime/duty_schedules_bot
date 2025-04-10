import uuid

from sqlalchemy import String, select
from sqlalchemy.dialects.postgresql import ARRAY, insert
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column

from databases.base import Base


class DutyLists(Base):
    __tablename__ = 'duty_lists'
    id: Mapped[str] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    admins: Mapped[list[str]] = mapped_column(ARRAY(String), nullable=False)
    duty_persons: Mapped[dict] = mapped_column(JSONB(none_as_null=True), nullable=False)

    async def get_duty_list_for_current_admin(self, id_admin: str, session: AsyncSession):
        statement = select(
            DutyLists.id,
            DutyLists.title,
            DutyLists.duty_persons
        ).where(
            DutyLists.admins.contains([id_admin])
        )
        result = await session.execute(statement)
        return result.all()

    async def add_pair(self, data: dict[str:], session: AsyncSession):
        unique_id = str(uuid.uuid4())
        statement = insert(DutyLists).values(
            id=unique_id, title=data['title'],
            admins=[str(data['admins'])], duty_persons=data['pairs'])
        await session.execute(statement)
        await session.commit()
