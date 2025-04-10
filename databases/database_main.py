from sqlalchemy.ext.asyncio import AsyncSession

from databases.models import DutyLists


class Database:
    def __init__(self, session: AsyncSession, duty_lists: DutyLists):
        self.session = session
        self.duty_lists = duty_lists
