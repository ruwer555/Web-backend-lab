from flask import Blueprint, render_template, request, session, redirect, current_app
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
from os import path

lab5 = Blueprint("lab5", __name__)

@lab5.route('/lab5/')
def lab():
    conn, cur = db_connect()
    
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT articles.*, users.login as author FROM articles JOIN users ON articles.user_id = users.id WHERE is_public=true ORDER BY is_favorite DESC, id DESC")
    else:
        cur.execute("SELECT articles.*, users.login as author FROM articles JOIN users ON articles.user_id = users.id WHERE is_public=1 ORDER BY is_favorite DESC, id DESC")
    
    public_articles = cur.fetchall()
    db_close(conn, cur)
    
    return render_template('/lab5/lab5.html', login=session.get('login'), public_articles=public_articles)

def db_connect():
    if current_app.config['DB_TYPE'] == 'postgres':
        conn = psycopg2.connect(
            host='127.0.0.1',
            port="5432",
            database='vladimir_kopylov_knowledge_base',
            user='vladimir_kopylov_knowledge_base',
            password='111'
        )
        cur = conn.cursor(cursor_factory=RealDictCursor)
    else:
        dir_path = path.dirname(path.realpath(__file__))
        db_path = path.join(dir_path, "database.db")
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
    return conn, cur

def db_close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()

@lab5.route('/lab5/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('/lab5/register.html')
    
    login = request.form.get('login')
    password = request.form.get('password')
    name = request.form.get('name')
    
    if not (login and password):
        return render_template('/lab5/register.html', error='Заполните все обязательные поля')
    
    conn, cur = db_connect()
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT login FROM users WHERE login=%s;", (login,))
    else:
        cur.execute("SELECT login FROM users WHERE login=?", (login,))
    
    if cur.fetchone():
        db_close(conn, cur)
        return render_template('/lab5/register.html', error="Такой пользователь уже существует")
    
    password_hash = generate_password_hash(password)
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("INSERT INTO users (login, password, name) VALUES (%s, %s, %s);", (login, password_hash, name))
    else:
        cur.execute("INSERT INTO users (login, password, name) VALUES (?, ?, ?);", (login, password_hash, name))
    
    db_close(conn, cur)
    return redirect('/lab5/login')

@lab5.route('/lab5/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('/lab5/login.html')
    
    login = request.form.get('login')
    password = request.form.get('password')
    
    if not (login and password):
        return render_template('lab5/login.html', error='Заполните все поля')
    
    conn, cur = db_connect()
    
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT login, password FROM users WHERE login=%s", (login,))
    else:
        cur.execute("SELECT login, password FROM users WHERE login=?", (login,))
    
    user = cur.fetchone()
    db_close(conn, cur)
    
    if not user:
        return render_template('/lab5/login.html', error='Логин и/или пароль неверны')
    
    if not check_password_hash(user['password'], password):
        return render_template('/lab5/login.html', error='Логин и/или пароль неверны')
    
    session['login'] = login
    return redirect('/lab5/')

@lab5.route('/lab5/logout')
def logout():
    session.pop('login', None)
    return redirect('/lab5/')

@lab5.route('/lab5/create', methods=['GET', 'POST'])
def create():
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')

    if request.method == 'GET':
        return render_template('/lab5/create_article.html')
    
    title = request.form.get('title')
    article_text = request.form.get('article_text')
    is_public = request.form.get('is_public')
    is_favorite = request.form.get('is_favorite')
    
    if not (title and article_text):
        return render_template('/lab5/create_article.html', error='Заполните название и текст статьи')
    
    conn, cur = db_connect()
    
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT id FROM users WHERE login=%s;", (login,))
    else:
        cur.execute("SELECT id FROM users WHERE login=?;", (login,))
    
    user_id = cur.fetchone()["id"]
    
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("INSERT INTO articles(user_id, title, article_text, is_public, is_favorite) VALUES (%s, %s, %s, %s, %s);", 
                   (user_id, title, article_text, bool(is_public), bool(is_favorite)))
    else:
        cur.execute("INSERT INTO articles(user_id, title, article_text, is_public, is_favorite) VALUES (?, ?, ?, ?, ?);", 
                   (user_id, title, article_text, 1 if is_public else 0, 1 if is_favorite else 0))
    
    db_close(conn, cur)
    return redirect('/lab5/list')

@lab5.route('/lab5/list')
def list_articles():
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')
    
    conn, cur = db_connect()
    
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT id FROM users WHERE login=%s;", (login,))
    else:
        cur.execute("SELECT id FROM users WHERE login=?;", (login,))
    
    user_id = cur.fetchone()["id"]
    
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT * FROM articles WHERE user_id=%s ORDER BY is_favorite DESC, id DESC;", (user_id,))
    else:
        cur.execute("SELECT * FROM articles WHERE user_id=? ORDER BY is_favorite DESC, id DESC;", (user_id,))
    
    articles = cur.fetchall()
    db_close(conn, cur)
    
    return render_template('/lab5/articles.html', articles=articles, login=login)

@lab5.route('/lab5/edit/<int:article_id>', methods=['GET', 'POST'])
def edit_article(article_id):
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')
    
    conn, cur = db_connect()
    
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT a.* FROM articles a JOIN users u ON a.user_id = u.id WHERE a.id=%s AND u.login=%s;", 
                   (article_id, login))
    else:
        cur.execute("SELECT a.* FROM articles a JOIN users u ON a.user_id = u.id WHERE a.id=? AND u.login=?;", 
                   (article_id, login))
    
    article = cur.fetchone()
    
    if not article:
        db_close(conn, cur)
        return redirect('/lab5/list')
    
    if request.method == 'GET':
        db_close(conn, cur)
        return render_template('/lab5/edit_article.html', article=article)
    
    title = request.form.get('title')
    article_text = request.form.get('article_text')
    is_public = request.form.get('is_public')
    is_favorite = request.form.get('is_favorite')
    
    if not (title and article_text):
        db_close(conn, cur)
        return render_template('/lab5/edit_article.html', article=article, error='Заполните название и текст статьи')
    
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("UPDATE articles SET title=%s, article_text=%s, is_public=%s, is_favorite=%s WHERE id=%s;", 
                   (title, article_text, bool(is_public), bool(is_favorite), article_id))
    else:
        cur.execute("UPDATE articles SET title=?, article_text=?, is_public=?, is_favorite=? WHERE id=?;", 
                   (title, article_text, 1 if is_public else 0, 1 if is_favorite else 0, article_id))
    
    db_close(conn, cur)
    return redirect('/lab5/list')

@lab5.route('/lab5/delete/<int:article_id>')
def delete_article(article_id):
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')
    
    conn, cur = db_connect()
    
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("DELETE FROM articles WHERE id=%s AND user_id=(SELECT id FROM users WHERE login=%s);", 
                   (article_id, login))
    else:
        cur.execute("DELETE FROM articles WHERE id=? AND user_id=(SELECT id FROM users WHERE login=?);", 
                   (article_id, login))
    
    db_close(conn, cur)
    return redirect('/lab5/list')

@lab5.route('/lab5/users')
def users():
    conn, cur = db_connect()
    
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT login, name FROM users ORDER BY login;")
    else:
        cur.execute("SELECT login, name FROM users ORDER BY login;")
    
    users = cur.fetchall()
    db_close(conn, cur)
    
    return render_template('/lab5/users.html', users=users)

@lab5.route('/lab5/profile', methods=['GET', 'POST'])
def profile():
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')
    
    conn, cur = db_connect()
    
    if request.method == 'GET':
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute("SELECT name FROM users WHERE login=%s;", (login,))
        else:
            cur.execute("SELECT name FROM users WHERE login=?;", (login,))
        
        user = cur.fetchone()
        db_close(conn, cur)
        return render_template('/lab5/profile.html', user=user, login=login)
    
    name = request.form.get('name')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')
    
    if password and password != confirm_password:
        return render_template('/lab5/profile.html', error='Пароли не совпадают', user={'name': name}, login=login)
    
    if current_app.config['DB_TYPE'] == 'postgres':
        if password:
            password_hash = generate_password_hash(password)
            cur.execute("UPDATE users SET name=%s, password=%s WHERE login=%s;", (name, password_hash, login))
        else:
            cur.execute("UPDATE users SET name=%s WHERE login=%s;", (name, login))
    else:
        if password:
            password_hash = generate_password_hash(password)
            cur.execute("UPDATE users SET name=?, password=? WHERE login=?;", (name, password_hash, login))
        else:
            cur.execute("UPDATE users SET name=? WHERE login=?;", (name, login))
    
    db_close(conn, cur)
    return redirect('/lab5/profile')