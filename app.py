from flask import Flask, url_for, request, redirect, abort, make_response
from werkzeug.exceptions import HTTPException
import datetime
app = Flask(__name__)

@app.errorhandler(400)
def bad_request(err):
    return '''<!doctype html> 
    <html> 
        <head>
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
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
    return '''<!doctype html> 
    <html> 
        <head>
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
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
    return '''<!doctype html> 
    <html> 
        <head>
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
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
    return '''<!doctype html> 
    <html> 
        <head>
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
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

@app.errorhandler(404)
def not_found(err):
    path_erorr = url_for("static", filename="error.webp")
    return '''<!doctype html> 
    <html> 
        <head>
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        </head>
        <body> 
            <h1>Ошибка 404 - Не найдено<h1> 
            <img src="''' + path_erorr + '''">
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
    </html>''', 404
    
@app.errorhandler(405)
def method_not_allowed(err):
    return '''<!doctype html> 
    <html> 
        <head>
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
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
    return '''<!doctype html> 
    <html> 
        <head>
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
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
    return '''<!doctype html> 
    <html> 
        <head>
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
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

@app.route('/lab1/web')
def web():
    return '''<!doctype html> 
    <html> 
        <head>
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        </head>
        <body> 
            <h1>web-сервер на flask<h1> 
            <div>
                <a href="/lab1">На главную</a>
            </div>
        </body> 
    </html>''', 200, #{
        #'X-Server': 'sample',
        #'Content-Type': 'text/plain; charset=utf-8'
    #}

@app.route('/lab1/author')
def author():
    name = "Копылов Владимир Вячеславович"
    group = "ФБИ-31"
    faculty = "ФБ"

    return '''<!doctype html> 
        <html> 
            <head>
                <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
            </head>
            <body> 
                <p>Студент: ''' + name + '''<p>
                <p>Группа: ''' + group + '''<p> 
                <p>Факультет: ''' + faculty + '''<p> 
                <div>
                    <a href="/lab1">На главную</a>
                </div>
            </body> 
        </html>'''

@app.route('/lab1/image')
def image():
    path = url_for("static", filename="Dub.jpg")
    html_image = '''<!doctype html> 
        <html> 
            <head>
                <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
            </head>
            <body> 
                <h1>Дуб<h1>
                <img src="''' + path + '''">
                <div>
                    <a href="/lab1">На главную</a>
                </div>
            </body> 
        </html>'''
    response = make_response(html_image)
    response.headers['Content-Language'] = 'ru'
    return response
       
count=0

@app.route('/lab1/clear_counter')
def clear_counter():
    global count
    count = -1
    return redirect("/lab1/counter")
        
@app.route('/lab1/counter')
def counter():
    global count
    count += 1
    time = datetime.datetime.today()
    url = request.url
    client_ip = request.remote_addr
    return '''<!doctype html> 
    <html> 
        <head>
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        </head>
        <body> 
            Сколько раз вы сюда заходили: ''' + str(count) + '''
            <hr>
            Дата и время: ''' + str(time) + ''' <br>
            Запрошенный адрес: ''' + str(url) + ''' <br>
            Ваш IP адрес: ''' + str(client_ip) + '''<br>
        </body> 
        <ul>
            <a href="/lab1/clear_counter">Очищение счетчика</a>
            <a href="/lab1">На главную</a>
        </ul>
    </html>'''
    
@app.route('/lab1/info')
def info():
    return redirect("/lab1/author")

@app.route('/')
@app.route('/index')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</h1>
            </div>
            
            <div class="menu">
                <ol>
                    <li><a href="''' + url_for('lab1') + '''">Первая лабораторная</a></li>
                    <li><a href="''' + url_for('lab1') + '''">Вторая лабораторная</a></li>
                    <li><a href="''' + url_for('lab1') + '''">Третья лабораторная</a></li>
                    <li><a href="''' + url_for('lab1') + '''">Четвертая лабораторная</a></li>
                    <li><a href="''' + url_for('lab1') + '''">Пятая лабораторная</a></li>
                </ol>
            </div>
            
            <div class="footer">
                <p>Копылов Владимир Вячеславовович, группа ФБИ-31, 3 курс, 2025 год</p>
            </div>
        </div>
    </body>
    </html>
    '''
@app.route('/lab1')
def lab1():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Лабораторная 1</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Лабораторная работа 1</h1>
            </div>
            
            <div style="background: white; padding: 20px; border-radius: 10px; margin: 20px 0;">
                <p>Flask — фреймворк для создания веб-приложений на языке
                программирования Python, использующий набор инструментов
                Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
                называемых микрофреймворков — минималистичных каркасов
                веб-приложений, сознательно предоставляющих лишь самые базовые возможности.</p>
            </div>
            <hr>
            <h2>Все роуты</h2>
            <ul>
                <li><a href="/index">Курс</a></li>
                <li><a href="400">Ошибки</a></li>
                <li><a href="/lab1/author">Автор</a></li>
                <li><a href="/lab1/image">Картинка</a></li>
                <li><a href="/lab1/web">WEB</a></li>
                <li><a href="/lab1/counter">Счетчик</a></li>
            </ul>
        </div>
    </body>
    </html>
    '''
@app.route('/lab2/a')
def a():
    return "без слэша"

@app.route('/lab2/a/')
def a2():
    return "со слэшем"


    
    
    
    
    
    
    