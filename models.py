from app import db
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import ForeignKey


class Press(db.Model):
    __tablename__ = 'press'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    tag_line = db.Column(db.String())
    link = db.Column(db.String())

    def __init__(self, title, tag_line, link):
        self.title = title
        self.tag_line = tag_line
        self.link = link

    def __repr__(self):
        return '<id {}>'.format(self.id)

class Photo(db.Model):
    __tablename__ = 'photos'

    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(ForeignKey("press.id"), nullable=False)#db.relationship("Press", foreign_keys="Press.id")
    # article_id = db.Column(db.Integer)
    url = db.Column(db.String())

    def __init__(self, article_id, url):
        self.article_id = article_id
        self.url = url

    def __repr__(self):
        return '<id {}>'.format(self.id)