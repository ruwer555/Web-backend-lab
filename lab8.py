from flask import Blueprint, render_template, request, redirect
from db import db
from sqlalchemy import or_
from db.models import Users, Articles
from flask_login import login_user, login_required, current_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

lab8 = Blueprint('lab8', __name__)


@lab8.route('/lab8/')
def lab():
    username = current_user.login if current_user.is_authenticated else 'anonymous'
    return render_template('lab8/lab8.html', username=username)


# --------- РЕГИСТРАЦИЯ ---------

@lab8.route('/lab8/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab8/register.html')

    login_form = request.form.get('login', '').strip()
    password_form = request.form.get('password', '').strip()

    errors = {}

    if not login_form:
        errors['login'] = 'Логин не должен быть пустым'
    if not password_form:
        errors['password'] = 'Пароль не должен быть пустым'

    if not errors:
        login_exists = Users.query.filter_by(login=login_form).first()
        if login_exists:
            errors['login'] = 'Такой пользователь уже существует'

    if errors:
        return render_template('lab8/register.html',
                               errors=errors,
                               login=login_form)

    password_hash = generate_password_hash(password_form)
    new_user = Users(login=login_form, password=password_hash)
    db.session.add(new_user)
    db.session.commit()

    # авто‑логин после регистрации
    login_user(new_user, remember=False)

    return redirect('/lab8/')


# --------- ЛОГИН ---------

@lab8.route('/lab8/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('lab8/login.html')

    login_form = request.form.get('login', '').strip()
    password_form = request.form.get('password', '').strip()
    remember = request.form.get('remember') == 'on'

    errors = {}
    if not login_form:
        errors['login'] = 'Введите логин'
    if not password_form:
        errors['password'] = 'Введите пароль'

    if errors:
        return render_template('lab8/login.html',
                               errors=errors,
                               login=login_form)

    user = Users.query.filter_by(login=login_form).first()

    if user and check_password_hash(user.password, password_form):
        login_user(user, remember=remember)
        return redirect('/lab8/')

    return render_template('lab8/login.html',
                           error='Ошибка входа: логин и/или пароль неверны',
                           login=login_form)


# --------- ЛОГАУТ ---------

@lab8.route('/lab8/logout')
@login_required
def logout():
    logout_user()
    return redirect('/lab8/')


# --------- СПИСОК СТАТЕЙ ---------

@lab8.route('/lab8/articles')
@login_required
def articles_list():
    articles = Articles.query.all()
    return render_template('lab8/articles.html', articles=articles)


# --------- СОЗДАНИЕ СТАТЬИ ---------

@lab8.route('/lab8/create', methods=['GET', 'POST'])
@login_required
def create_article():
    if request.method == 'GET':
        return render_template('lab8/create.html')

    title = request.form.get('title', '').strip()
    text = request.form.get('text', '').strip()
    is_public = request.form.get('is_public') == 'on'

    errors = {}
    if not title:
        errors['title'] = 'Введите заголовок'
    if not text:
        errors['text'] = 'Введите текст статьи'

    if errors:
        return render_template('lab8/create.html',
                               errors=errors,
                               title=title,
                               text=text,
                               is_public=is_public)

    new_article = Articles(
        login_id=current_user.id,
        title=title,
        article_text=text,
        is_public=is_public,
        likes=0,
        is_favorite=False
    )
    db.session.add(new_article)
    db.session.commit()

    return redirect('/lab8/articles')


# --------- РЕДАКТИРОВАНИЕ СТАТЬИ ---------

@lab8.route('/lab8/edit/<int:article_id>', methods=['GET', 'POST'])
@login_required
def edit_article(article_id):
    article = Articles.query.get_or_404(article_id)

    if article.login_id != current_user.id:
        return 'Можно редактировать только свои статьи', 403

    if request.method == 'GET':
        return render_template('lab8/edit.html', article=article)

    title = request.form.get('title', '').strip()
    text = request.form.get('text', '').strip()
    is_public = request.form.get('is_public') == 'on'

    if not title or not text:
        error = 'Заполните все поля'
        return render_template('lab8/edit.html',
                               article=article,
                               error=error)

    article.title = title
    article.article_text = text
    article.is_public = is_public
    db.session.commit()

    return redirect('/lab8/articles')


# --------- УДАЛЕНИЕ СТАТЬИ ---------

@lab8.route('/lab8/delete/<int:article_id>')
@login_required
def delete_article(article_id):
    article = Articles.query.get_or_404(article_id)

    if article.login_id != current_user.id:
        return 'Можно удалять только свои статьи', 403

    db.session.delete(article)
    db.session.commit()
    return redirect('/lab8/articles')

@lab8.route('/lab8/public')
def public_articles():
    # только статьи, у которых is_public = True
    articles = Articles.query.filter_by(is_public=True).all()
    return render_template('lab8/articles.html', articles=articles)


@lab8.route('/lab8/search', methods=['GET', 'POST'])
@login_required
def search_articles():
    query_text = request.form.get('q', '').strip()
    results = []

    if request.method == 'POST' and query_text:
        pattern = f"%{query_text}%"

        results = Articles.query.filter(
            or_(
                # свои статьи
                Articles.login_id == current_user.id,
                # или публичные чужие
                Articles.is_public == True
            ),
            or_(
                Articles.title.ilike(pattern),
                Articles.article_text.ilike(pattern)
            )
        ).all()

    return render_template('lab8/search.html',
                           q=query_text,
                           results=results)
