from sqlalchemy import Column, String, DateTime
from data.modelbase import SqlAlchemyBase

class Article(SqlAlchemyBase):
    __tablename__ = 'articles'

    title = Column(String, primary_key=True)
    author = Column(String)
    created_date = Column(DateTime)
    updated_date = Column(DateTime)
    summary = Column(String)
    content = Column(String)
    
    #tags

    #comments

    def __repr__(self):
        return '<Article {}>'.format(self.title)