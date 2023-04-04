from db.db_base import Base


class Keyword(Base):
    __tablename__ = 'keywords'
    user_id =