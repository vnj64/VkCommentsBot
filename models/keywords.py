from sqlalchemy import BigInteger, Column, String, select, insert, Integer
from sqlalchemy.orm import sessionmaker

from db.db_base import Base


class Keyword(Base):
    __tablename__ = 'keywords'
    id = Column(Integer, primary_key=True, autoincrement=True)
    telegram_id = Column(BigInteger)
    keyword = Column(String(length=100), unique=True)

    @classmethod
    async def get_keyword(cls, session_maker: sessionmaker, telegram_id: int):
        async with session_maker() as db_session:
            sql = select(cls.keyword).where(cls.telegram_id == telegram_id)
            request = await db_session.execute(sql)
            keyword: cls = request.all()
        return keyword

    @classmethod
    async def add_keyword(cls,
                          session_maker: sessionmaker,
                          telegram_id: int,
                          keyword: str):

        async with session_maker() as db_session:
            sql = insert(cls).values(
                telegram_id=telegram_id,
                keyword=keyword
            ).returning('*')

            result = await db_session.execute(sql)
            await db_session.commit()
            return result.first()
