from sqlalchemy.ext.asyncio import AsyncSession

from databases.models import Schedule


class Database:
    def __init__(self, session: AsyncSession, schedule: Schedule):
        self.session = session
        self.schedule = schedule