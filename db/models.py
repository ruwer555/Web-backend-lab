from db import db
from flask_login import UserMixin


class Users(db.Model, UserMixin):
    __tablename__ = 'users_orm'  

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(162), nullable=False)


class Articles(db.Model):
    __tablename__ = 'articles_orm'  # другое имя таблицы

    id = db.Column(db.Integer, primary_key=True)
    login_id = db.Column(db.Integer, db.ForeignKey('users_orm.id'))
    title = db.Column(db.String(50), nullable=False)
    article_text = db.Column(db.Text, nullable=False)
    is_favorite = db.Column(db.Boolean, default=False)
    likes = db.Column(db.Integer, default=0)
    is_public = db.Column(db.Boolean, default=False)
