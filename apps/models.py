"""
models.py

"""
from apps import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    #key = 
    content = db.Column(db.Text())
    category = db.Column(db.String(255))
    date_created = db.Column(db.DateTime(), default=db.func.now())

class Process(db.Model):
    id_P = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text())
    #key = 
    A_id = db.Column(db.Integer, db.ForeignKey('article.id'))
    article = db.relationship('Article',
                              backref=db.backref('comments', cascade='all, delete-orphan', lazy='dynamic'))

class Inspire(db.Model):
    id_I = db.Column(db.Integer, primary_key=True)
    #key = 
    A_id = db.Column(db.Integer, db.ForeignKey('article.id'))
    article = db.relationship('Article',
                              backref=db.backref('comments', cascade='all, delete-orphan', lazy='dynamic'))

class Comment(db.Model):
    id_C = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text())
    A_id = db.Column(db.Integer, db.ForeignKey('Article.id'))
    date_created = db.Column(db.DateTime(), default=db.func.now())

#    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))
#    article = db.relationship('Article',
#                              backref=db.backref('comments', cascade='all, delete-orphan', lazy='dynamic'))
