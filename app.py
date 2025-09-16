from flask import Flask, url_for, request, redirect
import datetime
app = Flask(__name__)

@app.route("/web")
def web():
    return """<!doctype html> 
    <html> 
        <body> 
            <h1>web-сервер на flask<h1> 
            <a href="/author">author</a>
        </body> 
    </html>"""

@app.route("/author")
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
            <a href="/web">web</a>
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
                <a href="/author">author</a>
            </body> 
        </html>"""