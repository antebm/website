from datetime import datetime
from sqlalchemy import Column, String, DateTime, Integer, orm
from sqlalchemy.sql.schema import ForeignKey
from data.modelbase import SqlAlchemyBase

class Article(SqlAlchemyBase):
    __tablename__ = 'articles'

    title = Column(String, primary_key=True)
    created_date = Column(DateTime, default=datetime.now, index=True)
    updated_date = Column(DateTime, default=datetime.now)
    summary = Column(String, nullable=True)
    article_image_url = Column(String, nullable=True)
    content = Column(String, nullable=False)
    
    # author relationship
    author_id = Column(Integer, ForeignKey("users.id"))
    author = orm.relation("User")

    #tags

    #comments
    #comments = orm.relationship("Comment", order_by=Comment.created_date.ascending())

    def __repr__(self):
        return '<Article {}>'.format(self.title)