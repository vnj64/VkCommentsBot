from datetime import datetime

from sqlalchemy import Column, String, BigInteger, select, insert, update
from sqlalchemy.orm import sessionmaker

from db.db_base import Base


class User(Base):
    __tablename__ = 'users'
    telegram_id = Column(BigInteger, primary_key=True)
    username = Column(String(length=100))
    fullname = Column(String(length=100))
    reg_date = Column(String)

    @classmethod
    async def get_user(cls, session_maker: sessionmaker, telegram_id: int) -> 'User':
        async with session_maker() as db_session:
            sql = select(cls).where(cls.telegram_id == telegram_id)
            request = await db_session.execute(sql)
            user: cls = request.scalar()
        return user

    @classmethod
    async def add_user(cls,
                       session_maker: sessionmaker,
                       telegram_id: int,
                       fullname: str,
                       date: datetime,
                       username: str = None
                       ) -> 'User':
        async with session_maker() as db_session:
            reg_date = date.strftime('%d.%m.%Y')
            sql = insert(cls).values(
                telegram_id=telegram_id,
                fullname=fullname,
                username=username,
                reg_date=reg_date
            ).returning('*')

            result = await db_session.execute(sql)
            await db_session.commit()
            return result.first()

    @classmethod
    async def update_username_fullname(cls, telegram_id: int, session_maker: sessionmaker, username: str,
                                       fullname: str) -> 'User':
        async with session_maker() as db_session:
            extra_context = {'username': username, 'fullname': fullname}
            sql = update(cls).where(cls.telegram_id == telegram_id).values(extra_context)
            result = await db_session.execute(sql)
            await db_session.commit()
            return result
