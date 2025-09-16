from flask import Flask
app = Flask(__name__)

@app.route("/web")
def web():
    return "web-сервер на flask"
                