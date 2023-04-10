from sqlalchemy import Column, Integer, BigInteger, select, insert, String
from sqlalchemy.orm import sessionmaker

from db.db_base import Base


class Post(Base):
    __tablename__ = 'post_info'
    id = Column(Integer, primary_key=True, autoincrement=True)
    telegram_id = Column(BigInteger)
    owner_id = Column(String)
    post_id = Column(String)

    @classmethod
    async def get_post_info(cls, session_maker: sessionmaker, telegram_id: int):
        async with session_maker() as db_session:
            sql = select(cls.owner_id, cls.post_id).where(cls.telegram_id == telegram_id)
            request = await db_session.execute(sql)
            post_info: cls = request.all()
        return post_info

    @classmethod
    async def add_post_info(cls,
                            session_maker: sessionmaker,
                            telegram_id: int,
                            owner_id: str,
                            post_id: str):
        async with session_maker() as db_session:
            sql = insert(cls).values(
                telegram_id=telegram_id,
                owner_id=owner_id,
                post_id=post_id,
            ).returning('*')

            result = await db_session.execute(sql)
            await db_session.commit()
            return result.first()
