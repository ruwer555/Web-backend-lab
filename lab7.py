from flask import Blueprint, request, render_template, abort
lab7 = Blueprint("lab7", __name__)

@lab7.route('/lab7/')
def lab():
    return render_template('/lab7/lab7.html')

films = [
    {
        "title": "The Shawshank Redemption",
        "title_ru": "Побег из Шоушенка",
        "year": "1994",
        "description": "Два заключенных заводят дружбу, находя утешение и искупление через сострадание и надежду.",
    },
    {
        "title": "The Godfather",
        "title_ru": "Крестный отец",
        "year": "1972",
        "description": "Стареющий патриарх организованной преступной династии передает контроль над своим подпольным империей своему неохотному сыну.",
    },
    {
        "title": "The Dark Knight",
        "title_ru": "Темный рыцарь",
        "year": "2008",
        "description": "Когда Джокер сеет хаос в Готэме, Бэтмен должен противостоять одному из самых больших психологических испытаний.",
    },
    {
        "title": "Pulp Fiction",
        "title_ru": "Криминальное чтиво",
        "year": "1994",
        "description": "Жизни двух наемных убийц, боксера, гангстера и его жены переплетаются в четырех историях о насилии и искуплении.",
    },
    {
        "title": "Forrest Gump",
        "title_ru": "Форрест Гамп",
        "year": "1994",
        "description": "История жизни Форреста Гампа, добродушного человека с низким IQ, который невольно оказывается участником ключевых исторических событий.",
    },
    {
        "title": "Inception",
        "title_ru": "Начало",
        "year": "2010",
        "description": "Вор, который крадет корпоративные секреты через использование технологии общих снов, получает задание подселить идею в подсознание человека.",
    }
]

@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    return films

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_films_id(id):
    if 0 > id or id >= len(films):
        abort(404)
    return films[id]

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_films(id):
    if 0 > id or id >= len(films):
        abort(404)
    del films[id]
    return '', 204

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_films(id):
    if id < 0 or id >= len(films):  # ← ДОБАВЬ ПРОВЕРКУ И ЗДЕСЬ!
        abort(404)
    film = request.get_json()
    films[id] = film
    return films[id]






