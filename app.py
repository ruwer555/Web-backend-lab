from flask import Flask, url_for, request, redirect, abort, make_response, render_template
import os
from db.models import Users, Articles
from werkzeug.exceptions import HTTPException
import datetime
from db import db
from flask_login import LoginManager
from os import path
from sqlalchemy import or_

from lab8 import lab8
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7
from lab8 import lab8
from lab9 import lab9
from RGZ import rgz

app = Flask(__name__)

# --- Flask-Login ---
login_manager = LoginManager()
login_manager.login_view = 'lab8.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

# --- конфиг БД ---
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'super-secret-key-111')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')

if app.config['DB_TYPE'] == 'postgres':
    db_name = 'vladimir_kopylov_knowledge_base'
    db_user = 'vladimir_kopylov_knowledge_base'
    db_password = '123'
    host_ip = '127.0.0.1'
    host_port = 5432
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        f'postgresql://{db_user}:{db_password}@{host_ip}:{host_port}/{db_name}'
else:
    dir_path = path.dirname(path.realpath(__file__))
    db_path = path.join(dir_path, "vladimir_kopylov_knowledge_base.db")
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

db.init_app(app)


app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'super-secret-key-111')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')

app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)
app.register_blueprint(lab8)
app.register_blueprint(lab9)
app.register_blueprint(rgz)

@app.errorhandler(400)
def bad_request(err):
    return f'''<!doctype html> 
    <html> 
        <head>
            <link rel="stylesheet" href="{ url_for('static', filename='lab1.css') }">
        </head>
        <body> 
            <h1>Ошибка 400 - Плохой запрос<h1> 
            <ul>
                <li><a href="/400">Ошибка 400</a></li>
                <li><a href="/401">Ошибка 401</a></li>
                <li><a href="/402">Ошибка 402</a></li>
                <li><a href="/403">Ошибка 403</a></li>
                <li><a href="/404">Ошибка 404</a></li>
                <li><a href="/405">Ошибка 405</a></li>
                <li><a href="/418">Ошибка 418</a></li>
                <li><a href="/500">Ошибка 500</a></li>
                <li><a href="/lab1">На главную</a></li>
            </ul>
        </body> 
    </html>''', 400

@app.errorhandler(401)
def unauthorized(err):
    return f'''<!doctype html> 
    <html> 
        <head>
            <link rel="stylesheet" href="{ url_for('static', filename='lab1.css') }">
        </head>
        <body> 
            <h1>Ошибка 401 - Неавторизован<h1> 
            <ul>
                <li><a href="/400">Ошибка 400</a></li>
                <li><a href="/401">Ошибка 401</a></li>
                <li><a href="/402">Ошибка 402</a></li>
                <li><a href="/403">Ошибка 403</a></li>
                <li><a href="/404">Ошибка 404</a></li>
                <li><a href="/405">Ошибка 405</a></li>
                <li><a href="/418">Ошибка 418</a></li>
                <li><a href="/500">Ошибка 500</a></li>
                <li><a href="/lab1">На главную</a></li>
            </ul>
        </body> 
    </html>''', 401
    
# Создаем кастомный класс для ошибки 402
class PaymentRequired(HTTPException):
    code = 402
    description = 'Требуется оплата'

# Регистрируем обработчик
@app.errorhandler(PaymentRequired)
def payment_required(err):
    return f'''<!doctype html> 
    <html> 
        <head>
            <link rel="stylesheet" href="{ url_for('static', filename='lab1.css') }">
        </head>
        <body> 
            <h1>Ошибка 402 - Требуется оплата<h1> 
            <ul>
                <li><a href="/400">Ошибка 400</a></li>
                <li><a href="/401">Ошибка 401</a></li>
                <li><a href="/402">Ошибка 402</a></li>
                <li><a href="/403">Ошибка 403</a></li>
                <li><a href="/404">Ошибка 404</a></li>
                <li><a href="/405">Ошибка 405</a></li>
                <li><a href="/418">Ошибка 418</a></li>
                <li><a href="/500">Ошибка 500</a></li>
                <li><a href="/lab1">На главную</a></li>
            </ul>
        </body> 
    </html>''', 402
    
@app.errorhandler(403)
def forbidden(err):
    return f'''<!doctype html> 
    <html> 
        <head>
            <link rel="stylesheet" href="{ url_for('static', filename='lab1.css') }">
        </head>
        <body> 
            <h1>Ошибка 403 - Запрещено<h1> 
            <ul>
                <li><a href="/400">Ошибка 400</a></li>
                <li><a href="/401">Ошибка 401</a></li>
                <li><a href="/402">Ошибка 402</a></li>
                <li><a href="/403">Ошибка 403</a></li>
                <li><a href="/404">Ошибка 404</a></li>
                <li><a href="/405">Ошибка 405</a></li>
                <li><a href="/418">Ошибка 418</a></li>
                <li><a href="/500">Ошибка 500</a></li>
                <li><a href="/lab1">На главную</a></li>
            </ul>
        </body> 
    </html>''', 403

access_logs = []

@app.errorhandler(404)
def not_found(err):
    global access_logs
    client_ip = request.remote_addr
    access_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    requested_url = request.url
    user_agent = request.headers.get('User-Agent', 'Неизвестный')
    log_entry = {
        'ip': client_ip,
        'time': access_time,
        'url': requested_url,
        'user_agent': user_agent
    }
    access_logs.append(log_entry)
    path_error = url_for("static", filename="lab1/error.webp")
    if len(access_logs) > 5:
        access_logs.pop(0)
    return f'''<!doctype html> 
    <html> 
        <head>
            <link rel="stylesheet" href="{url_for('static', filename='lab1/lab1.css')}">
        </head>
        <body> 
            <h1>Ошибка 404 - Не найдено</h1> 
            <img src="{path_error}">
            <div>
                <h3>Информация о текущем запросе:</h3>
                <p>IP-адрес: {client_ip}</p>
                <p>Время доступа: {access_time}</p>
                <p>Запрошенный URL:{requested_url}</p>
                <p>Браузер: {user_agent[:80]}...</p>
                <h3>Журнал доступа (последние {len(access_logs)} записей):</h3>
                    {"".join([f"<p><b>Время</b> - {log['time']} <b>IP пользовтеля</b> - {log['ip']} <b>Путь</b> - {log['url']}</p>" for log in reversed(access_logs)])}
            </div>
            
            <ul>
                <li><a href="/">На главную страницу</a></li>
                <li><a href="/lab1">К лабораторной 1</a></li>
                <li><a href="/400">Ошибка 400</a></li>
                <li><a href="/401">Ошибка 401</a></li>
                <li><a href="/402">Ошибка 402</a></li>
                <li><a href="/403">Ошибка 403</a></li>
                <li><a href="/405">Ошибка 405</a></li>
                <li><a href="/418">Ошибка 418</a></li>
                <li><a href="/500">Ошибка 500</a></li>
            </ul>
        </body> 
    </html>''', 404
    
@app.errorhandler(405)
def method_not_allowed(err):
    return f'''<!doctype html> 
    <html> 
        <head>
            <link rel="stylesheet" href="{ url_for('static', filename='lab1.css') }">
        </head>
        <body> 
            <h1>Ошибка 405 - Метод не разрешен<h1> 
            <ul>
                <li><a href="/400">Ошибка 400</a></li>
                <li><a href="/401">Ошибка 401</a></li>
                <li><a href="/402">Ошибка 402</a></li>
                <li><a href="/403">Ошибка 403</a></li>
                <li><a href="/404">Ошибка 404</a></li>
                <li><a href="/405">Ошибка 405</a></li>
                <li><a href="/418">Ошибка 418</a></li>
                <li><a href="/500">Ошибка 500</a></li>
                <li><a href="/lab1">На главную</a></li>
            </ul>
        </body> 
    </html>''', 405
    
@app.errorhandler(418)
def teapot(err):
    return f'''<!doctype html> 
    <html> 
        <head>
            <link rel="stylesheet" href="{ url_for('static', filename='lab1.css') }">
        </head>
        <body> 
            <h1>Ошибка 418 - Я чайник!<h1> 
            <ul>
                <li><a href="/400">Ошибка 400</a></li>
                <li><a href="/401">Ошибка 401</a></li>
                <li><a href="/402">Ошибка 402</a></li>
                <li><a href="/403">Ошибка 403</a></li>
                <li><a href="/404">Ошибка 404</a></li>
                <li><a href="/405">Ошибка 405</a></li>
                <li><a href="/418">Ошибка 418</a></li>
                <li><a href="/500">Ошибка 500</a></li>
                <li><a href="/lab1">На главную</a></li>
            </ul>
        </body> 
    </html>''', 418
    
@app.errorhandler(500)
def internal_server_error(err):
    return f'''<!doctype html> 
    <html> 
        <head>
            <link rel="stylesheet" href="{url_for('static', filename='lab1.css')}">
        </head>
        <body> 
            <h1>Ошибка 500 - Внутренняя ошибка сервера<h1> 
            <ul>
                <li><a href="/400">Ошибка 400</a></li>
                <li><a href="/401">Ошибка 401</a></li>
                <li><a href="/402">Ошибка 402</a></li>
                <li><a href="/403">Ошибка 403</a></li>
                <li><a href="/404">Ошибка 404</a></li>
                <li><a href="/405">Ошибка 405</a></li>
                <li><a href="/418">Ошибка 418</a></li>
                <li><a href="/500">Ошибка 500</a></li>
                <li><a href="/lab1">На главную</a></li>
            </ul>
        </body> 
    </html>''', 500

# Маршруты для вызова ошибок
@app.route('/400')
def trigger_400():
    abort(400)

@app.route('/401')
def trigger_401():
    abort(401)

@app.route('/402')
def trigger_402():
    raise PaymentRequired()

@app.route('/403')
def trigger_403():
    abort(403)

@app.route('/404')
def trigger_404():
    abort(404)

@app.route('/405')
def trigger_405():
    abort(405)

@app.route('/418')
def trigger_418():
    abort(418)
    
@app.route('/500')
def trigger_500():
    # Вызываем реальную ошибку 500 через деление на ноль
    result = 10 / 0
    return f'Результат: {result}'

@app.route('/')
@app.route('/index')
def index():
    return f'''
    <!DOCTYPE html>
    <html>
        <head>
            <title>НГТУ, ФБ, Лабораторные работы</title>
            <link rel="stylesheet" href="{url_for('static', filename='lab1/lab1.css')}">
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</h1>
                </div>
                
                <div class="menu">
                    <ol>
                        <li><a href="{ url_for('lab1.lab') }">Первая лабораторная</a></li>
                        <li><a href="{ url_for('lab2.lab') }">Вторая лабораторная</a></li>
                        <li><a href="{ url_for('lab3.lab') }">Третья лабораторная</a></li>
                        <li><a href="{ url_for('lab4.lab') }">Четвертая лабораторная</a></li>
                        <li><a href="{ url_for('lab5.lab') }">Пятая лабораторная</a></li>
                        <li><a href="{ url_for('lab6.lab') }">Шестая лабораторная</a></li>
                        <li><a href="{ url_for('lab7.lab') }">Седьмая лабораторная</a></li>
                        <li><a href="{ url_for('lab8.lab') }">Восьмая лабораторная</a></li>
                        <li><a href="{ url_for('lab9.lab') }">Девятая лабораторная</a></li>
                        <li><a href="{ url_for('lab9.lab') }">Расчетно-графическое задание</a></li>
                    </ol>
                </div>
                
                <div class="footer">
                    <p>Копылов Владимир Вячеславовович, группа ФБИ-31, 3 курс, 2025 год</p>
                </div>
            </div>
        </body>
    </html>
    '''
    
    