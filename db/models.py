from db import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# --- ЛАБА 8 (Старая БД) ---
class Users(db.Model, UserMixin):
    __tablename__ = 'users_orm' 
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(162), nullable=False)

class Articles(db.Model):
    __tablename__ = 'articles_orm'  
    id = db.Column(db.Integer, primary_key=True)
    login_id = db.Column(db.Integer, db.ForeignKey('users_orm.id'))
    title = db.Column(db.String(50), nullable=False)
    article_text = db.Column(db.Text, nullable=False)
    is_favorite = db.Column(db.Boolean, default=False)
    likes = db.Column(db.Integer, default=0)
    is_public = db.Column(db.Boolean, default=False)

# --- РГЗ (Новая БД) ---
class RgzUser(db.Model):
    __bind_key__ = 'rgz_db'  # ✅ Правильно!
    __tablename__ = 'rgz_users'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(30), unique=True, nullable=False)
    password_hash = db.Column(db.String(162), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class RgzGoods(db.Model):
    __bind_key__ = 'rgz_db'  # ✅ Правильно!
    __tablename__ = 'rgz_goods'
    id = db.Column(db.Integer, primary_key=True)
    article = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, default=0)
