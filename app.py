from flask import Flask, url_for, request, redirect, abort, make_response, render_template
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
    path_error = url_for("static", filename="error.webp")
    if len(access_logs) > 5:
        access_logs.pop(0)
    return f'''<!doctype html> 
    <html> 
        <head>
            <link rel="stylesheet" href="{url_for('static', filename='lab1.css')}">
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
    
@app.route('/lab1/info')
def info():
    return redirect("/lab1/author")

@app.route('/')
@app.route('/index')
def index():
    return f'''
    <!DOCTYPE html>
    <html>
        <head>
            <title>НГТУ, ФБ, Лабораторные работы</title>
            <link rel="stylesheet" href="{url_for('static', filename='lab1.css')}">
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</h1>
                </div>
                
                <div class="menu">
                    <ol>
                        <li><a href="''' + url_for('lab1') + '''">Первая лабораторная</a></li>
                        <li><a href="''' + url_for('lab2') + '''">Вторая лабораторная</a></li>
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
@app.route('/lab1/')
def lab1():
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
@app.route('/lab2/a')
def a():
    return "без слэша"

@app.route('/lab2/a/')
def a2():
    return "со слэшем"

flowers_list = [
    {'name': 'Роза', 'price': 150},
    {'name': 'Тюльпан', 'price': 80},
    {'name': 'Ромашка', 'price': 50},
    {'name': 'Орхидея', 'price': 300},
    {'name': 'Лилия', 'price': 120}
]

@app.route("/lab2/flowers/<int:flower_id>")
def flowers_id(flower_id):
    if flower_id >= len(flowers_list):
        abort(404)
    else:
        return render_template('flowers.html', page_type = 'flowers_id', flower_id=flower_id, flowers_list=flowers_list)
        
@app.route("/flowers_full/")
def flowers_full():
    return render_template('flowers.html', page_type = 'flowers_full', flowers_list=flowers_list)

@app.route("/flowers_clear/")
def flowers_clear():
        global flowers_list
        flowers_list = []
        return redirect("/flowers_full/")
          
@app.route("/lab2/add_flower/")
def flower_empty():
    return render_template('flowers.html', page_type = 'flower_empty', flowers_list=flowers_list), 400  

@app.route("/lab2/flowers/")
def flower_id_empty():
    return render_template('flowers.html', page_type = 'flower_base_add', flowers_list=flowers_list)
   
@app.route("/lab2/flower_base_add_id/")
def flower_base_add_id():
    if flowers_list:
        last_flower = flowers_list[-1]
        return redirect(f"/lab2/flowers/{len(flowers_list)-1}")        
    else:
        return redirect("/flowers_full/") 
    
@app.route("/lab2/add_flower/<name>")
def add_flowers(name):
        flowers_list.append(name)
        return render_template('flowers.html', page_type = 'add_flowers', flowers_list=flowers_list, name=name)
        
@app.route("/lab2/delete_flower/<int:flower_id>")
def delete_flower(flower_id):
    global flowers_list
    if flower_id >= len(flowers_list):
        abort(404)
    flowers_list.pop(flower_id)
    return redirect("/flowers_full/")

@app.route("/lab2/delete_flower/")
def delete_flower_empty():
    return render_template('flowers.html', page_type = 'delete_flower_empty', flowers_list=flowers_list)


@app.route("/lab2/add_flower_with_price", methods=['POST'])
def add_flower_with_price():
    global flowers_list
    name = request.form.get('flower_name')
    price = request.form.get('flower_price', 0)
    
    if name:
        flowers_list.append({
            'name': name,
            'price': int(price) if price else 0
        })
    return redirect("/flowers_full")



@app.route("/lab2/calc/")
def calc_empty():
    return redirect("/lab2/calc/1/1")

@app.route("/lab2/calc/<int:first>")
def calc_second_empty(first):
    return redirect(f"/lab2/calc/{first}/1")

@app.route("/lab2/example/")
def example():
    name = 'Копылов Владимир'
    num_lab = '2'
    group = 'ФБИ-31'
    kurs = '3'
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 200},
        {'name': 'апельсины', 'price': 300},
        {'name': 'мандарины', 'price': 400},
        {'name': 'манго', 'price': 500}
    ]
    return render_template('example.html', name=name, num_lab=num_lab, group=group, kurs=kurs, fruits=fruits)
     
@app.route("/lab2/calc/<int:first>/<int:second>")
def flowers(first, second):
    a = first
    b = second
    return f'''
        <!DOCTYPE html>
        <html>
            <head>
                <link rel="stylesheet" href="{url_for('static', filename='main.css')}">
            </head>
            <body>
                <h1>Калькулятор</h1>
                <ul>
                    <li>{a} + {b} = {a + b}<br></li>
                    <li>{a} * {b} = {a * b}<br></li>
                    <li>{a} - {b} = {a - b}<br></li>
                    <li>{a} / {b} = {a / b}<br></li>
                    <li>{a}<sup>{b}</sup> = {a ** b}<br></li>
                    <a href="/lab2/">Главная</a>
                </ul>
            </body>
        </html>
        '''

@app.route("/lab2/")
def lab2():
    return render_template('lab2.html')
    
@app.route("/lab2/filters")
def filters():
    phrase = 'O <b>сколько</b> <u>нам</u> <i>открытий</i> чудных...'
    return render_template('filters.html', phrase = phrase) 

@app.route("/lab2/book/")
def book():
    book = [
    {
        'author': 'Трумен Капоте',
        'title': 'Завтрак у Тиффани',
        'genre': 'Роман',
        'pages': 100
    },
    {
        'author': 'Анна Гавальда',
        'title': '35 кило надежды',
        'genre': 'Повесть',
        'pages': 200
    },
    {
        'author': 'Джером Д. Сэлинджер',
        'title': 'Над пропастью во ржи',
        'genre': 'Роман',
        'pages': 300
    },
    {
        'author': 'Эрнест Хемингуэй',
        'title': 'Старик и море',
        'genre': 'Повесть',
        'pages': 400
    },
    {
        'author': 'Франко Арминио',
        'title': 'Открытки с того света',
        'genre': 'Поэзия',
        'pages': 500
    },
    {
        'author': 'Агата Кристи',
        'title': '10 негритят',
        'genre': 'Детектив',
        'pages': 600
    },
    {
        'author': 'Алессандро Барикко',
        'title': '1900. Легенда о пианисте',
        'genre': 'Повесть',
        'pages': 700
    },
    {
        'author': 'Фрэнсис Скотт Фицджеральд',
        'title': 'Великий Гэтсби',
        'genre': 'Роман',
        'pages': 800
    },
    {
        'author': 'Жоржи Амаду',
        'title': 'Мёртвое море',
        'genre': 'Роман',
        'pages': 900
    },
    {
        'author': 'А. Сент-Экзюпери',
        'title': 'Маленький принц',
        'genre': 'Философская сказка',
        'pages': 1000
    }
    
]
    return render_template('book.html', book = book) 

@app.route("/lab2/images/")
def images():
    images_20 = [
        {
            'id': 1,
            'name': 'Калбаса',
            'image': 'image/sticker1.webp',
            'description': 'Я маленький бутербродик',
        },
        {
            'id': 2,
            'name': 'Пицца',
            'image': 'image/sticker2.webp',
            'description': 'Пицца с холопеньями',
        },
        {
            'id': 3,
            'name': 'Гриб',
            'image': 'image/sticker3.webp',
            'description': 'А я гриб',
        },
        {
            'id': 4,
            'name': 'Ананасини',
            'image': 'image/sticker4.webp',
            'description': 'Орунгутини ананасини',
        },
        {
            'id': 5,
            'name': 'Одна сосиска два теста',
            'image': 'image/sticker5.webp',
            'description': 'Упаф',
        },
        {
            'id': 6,
            'name': 'яблоко',
            'image': 'image/sticker6.webp',
            'description': 'Первый брат',
        },
        {
            'id': 7,
            'name': 'Зеленое яблоко',
            'image': 'image/sticker7.webp',
            'description': 'Второй брат',
        },
        {
            'id': 8,
            'name': 'Бананини',
            'image': 'image/sticker8.webp',
            'description': 'Обезьянини бананини',
        },
        {
            'id': 9,
            'name': 'Нагетс',
            'image': 'image/sticker9.webp',
            'description': 'Нагетс и ростикс',
        },
        {
            'id': 10,
            'name': 'Бургер',
            'image': 'image/sticker10.webp',
            'description': 'Бургер из бургер кинга',
        },
        {
            'id': 11,
            'name': 'Голубика',
            'image': 'image/sticker11.webp',
            'description': 'Голубика не клубника',
        },
        {
            'id': 12,
            'name': 'Клубника',
            'image': 'image/sticker12.webp',
            'description': 'Клубника не голубика',
        },
        {
            'id': 13,
            'name': 'Апельсинчик',
            'image': 'image/sticker13.webp',
            'description': 'Ровный пацанчик',
        },
        {
            'id': 14,
            'name': 'Краб лейз',
            'image': 'image/sticker14.webp',
            'description': 'Спасти 10 детей или...',
        },
        {
            'id': 15,
            'name': 'Пельмень',
            'image': 'image/sticker15.webp',
            'description': 'Что может быть лучше теста с мясом',
        },
        {
            'id': 16,
            'name': 'Варенник',
            'image': 'image/sticker16.webp',
            'description': 'Что может быть лучше теста с вишней',
        },
        {
            'id': 17,
            'name': 'Арбуз',
            'image': 'image/sticker17.webp',
            'description': 'Красный, сочный, дорогой бери, не пожалеешь',
        },
        {
            'id': 18,
            'name': 'кокос',
            'image': 'image/sticker18.webp',
            'description': 'Атдихаю',
        },
        {
            'id': 19,
            'name': 'Шиш с маслом',
            'image': 'image/sticker19.webp',
            'description': 'Сектор шиш с маслом',
        },
        {
            'id': 20,
            'name': 'Балтика',
            'image': 'image/sticker20.webp',
            'description': 'Нулевка',
        }
        
    ]
    return render_template('images.html', images_20 = images_20) 