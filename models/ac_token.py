from db.db_base import Base

from sqlalchemy import BigInteger, Column, String, select, insert, Integer, delete, and_
from sqlalchemy.orm import sessionmaker


class Token(Base):
    __tablename__ = 'encoded_token'
    id = Column(Integer, primary_key=True, autoincrement=True)
    telegram_id = Column(BigInteger)
    token = Column(String)

    @classmethod
    async def get_token(cls, session_maker: sessionmaker, telegram_id: int):
        async with session_maker() as db_session:
            sql = select(cls.token).where(cls.telegram_id == telegram_id)
            request = await db_session.execute(sql)
            token: cls = request.all()
        return token

    @classmethod
    async def add_token(cls,
                        session_maker: sessionmaker,
                        telegram_id: int,
                        token: str):
        async with session_maker() as db_session:
            sql = insert(cls).values(
                telegram_id=telegram_id,
                token=token
            ).returning('*')

            result = await db_session.execute(sql)
            await db_session.commit()
            return result.first()

    @classmethod
    async def delete_token(cls,
                           session_maker: sessionmaker,
                           telegram_id: int,):
        async with session_maker() as db_session:
            sql = delete(cls.id).where(and_(cls.telegram_id == telegram_id))
            result = await db_session.execute(sql)
            await db_session.commit()
            return result
