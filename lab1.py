import datetime
from flask import Blueprint, url_for, request, redirect, make_response
lab1 = Blueprint("lab1", __name__)


@lab1.route('/lab1/web')
def web():
    return f'''<!doctype html> 
    <html> 
        <head>
            <link rel="stylesheet" href="{url_for('static', filename='lab1.css')}">
        </head>
        <body> 
            <h1>web-сервер на flask</h1> 
            <div>
                <a href="/lab1">На главную</a>
            </div>
        </body> 
    </html>''', 200, #{
        #'X-Server': 'sample',
        #'Content-Type': 'text/plain; charset=utf-8'
    #}


@lab1.route('/lab1/author')
def author():
    name = "Копылов Владимир Вячеславович"
    group = "ФБИ-31"
    faculty = "ФБ"

    return f'''<!doctype html> 
        <html> 
            <head>
                <link rel="stylesheet" href="{url_for('static', filename='lab1.css')}">
            </head>
            <body> 
                <p>Студент: {name}</p>
                <p>Группа: {group}</p> 
                <p>Факультет: {faculty}</p> 
                <div>
                    <a href="/lab1">На главную</a>
                </div>
            </body> 
        </html>'''


@lab1.route('/lab1/image')
def image():
    path = url_for("static", filename="Dub.jpg")
    html_image = f'''<!doctype html> 
        <html> 
            <head>
                <link rel="stylesheet" href="{url_for('static', filename='lab1.css')}">
            </head>
            <body> 
                <h1>Дуб</h1>
                <img src="{path}">
                <div>
                    <a href="/lab1">На главную</a>
                </div>
            </body> 
        </html>'''
    response = make_response(html_image)
    response.headers['Content-Language'] = 'ru'
    return response
      
       
count=0


@lab1.route('/lab1/clear_counter')
def clear_counter():
    global count
    count = -1
    return redirect("/lab1/counter")
     
        
@lab1.route('/lab1/counter')
def counter():
    global count
    count += 1
    time = datetime.datetime.today()
    url = request.url
    client_ip = request.remote_addr
    return f'''<!doctype html> 
    <html> 
        <head>
            <link rel="stylesheet" href="{url_for('static', filename='lab1.css')}">
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
    
    
@lab1.route('/lab1/info')
def info():
    return redirect("/lab1/author")
    
    
@lab1.route('/lab1/')
def lab():
    return f'''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Лабораторная 1</title>
            <link rel="stylesheet" href="{url_for('static', filename='lab1.css')}">
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