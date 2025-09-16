from flask import Flask, url_for, request, redirect
import datetime
app = Flask(__name__)

@app.errorhandler(404)
def not_found(err):
    return "нет такой страницы", 404

@app.route('/lab1/web')
def web():
    return """<!doctype html> 
    <html> 
        <body> 
            <h1>web-сервер на flask<h1> 
            <a href="/lab1/author">author</a>
        </body> 
    </html>""", 200, {
        'X-Server': 'sample',
        'Content-Type': 'text/plain; charset=utf-8'
    }

@app.route('/lab1/author')
def author():
    name = "Копылов Владимир Вячеславович"
    group = "ФБИ-31"
    faculty = "ФБ"

    return """<!doctype html> 
    <html> 
        <body> 
            <p>Студент: """ + name + """<p>
            <p>Группа: """ + group + """<p> 
            <p>Факультет: """ + faculty + """<p> 
            <a href="/lab1/web">web</a>
        </body> 
    </html>"""

@app.route("/image")
def image():
    path=url_for("static", filename="dub.jpg")

    return """<!doctype html> 
        <html> 
            <body> 
                <h1>Дуб<h1>
                <img src="''' + path + '''">
                <a href="/lab1/author">author</a>
            </body> 
        </html>"""
        
count=0

@app.route('/lab1/counter')
def counter():
    global count
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] += 1
    time = datetime.datetime.today()
    url = request.url
    client_ip = request.remote_addr
    return """<!doctype html> 
    <html> 
        <body> 
            Сколько раз вы сюда заходили: ''' + srt(count) + '''
            <hr>
            Дата и время: ''' + time + ''' <br>
            Запрошенный адрес: ''' + url + ''' <br>
            Ваш IP адрес: ''' + client_ip + '''<br>
        </body> 
    </html>"""
    
@app.route('/lab1/info')
def info():
    return redirect("/author")

@app.route('/counter_clear')
def clear_counter():
    session.pop('counter', None)
    return redirect(url_for('counter'))

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
                <ul>
                    <li><a href="''' + url_for('lab1') + '''">Первая лабораторная</a></li>
                </ul>
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
            
            <a href="''' + url_for('/') + '''" style="background: #3498db; color: white; padding: 12px 24px; border-radius: 5px; text-decoration: none; display: inline-block; margin: 10px;">На главную</a>
        </div>
    </body>
    </html>
    '''
    
    # Роуты для генерации ошибок
@app.route('/lab1/400')
def error_400():
    abort(400)

@app.route('/lab1/401')
def error_401():
    abort(401)

@app.route('/lab1/402')
def error_402():
    abort(402)

@app.route('/lab1/403')
def error_403():
    abort(403)

@app.route('/lab1/405')
def error_405():
    abort(405)

@app.route('/lab1/418')
def error_418():
    abort(418)

# Обработчики ошибок
@app.errorhandler(400)
def bad_request(error):
    return render_template('400.html'), 400

@app.errorhandler(401)
def unauthorized(error):
    return render_template('401.html'), 401

@app.errorhandler(402)
def payment_required(error):
    return render_template('402.html'), 402

@app.errorhandler(403)
def forbidden(error):
    return render_template('403.html'), 403

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return render_template('405.html'), 405

@app.errorhandler(418)
def teapot(error):
    return render_template('418.html'), 418
    
@app.route('/lab1/500')
def error_500():
    # Вызываем ошибку деления на ноль
    result = 1 / 0
    return "Этот код никогда не выполнится"

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500