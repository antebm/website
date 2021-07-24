from datetime import datetime
from sqlalchemy import Column, String, DateTime
from data.modelbase import SqlAlchemyBase

class Article(SqlAlchemyBase):
    __tablename__ = 'articles'

    title = Column(String, primary_key=True)
    author = Column(String, index=True)
    created_date = Column(DateTime, default=datetime.now, index=True)
    updated_date = Column(DateTime, default=datetime.now)
    summary = Column(String, nullable=True)
    article_image_url = Column(String, nullable=True)
    content = Column(String, nullable=False)
    
    #tags

    #comments

    def __repr__(self):
        return '<Article {}>'.format(self.title)