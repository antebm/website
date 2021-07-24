from datetime import datetime
from data.modelbase import SqlAlchemyBase
from sqlalchemy import Column, String, Integer, DateTime

class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    email = Column(String, index=True, unique=True, nullable=True)
    hashed_password = Column(String, nullable=True, index=True)
    created_date = Column(DateTime, default=datetime.now, index=True)
    profile_image_url = Column(String)
    last_login = Column(DateTime, default=datetime.now, index=True)