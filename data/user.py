from typing import List
from data.article import Article
from datetime import datetime
from data.modelbase import SqlAlchemyBase
from sqlalchemy import Column, String, Integer, DateTime, orm

class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    email = Column(String, index=True, unique=True, nullable=True)
    hashed_password = Column(String, nullable=True, index=True)
    created_date = Column(DateTime, default=datetime.now, index=True)
    profile_image_url = Column(String)
    last_login = Column(DateTime, default=datetime.now, index=True)

    # articles relationship
    articles : List[Article] = orm.relation("Article", Article.created_date.desc(), 
        back_populates = 'author')