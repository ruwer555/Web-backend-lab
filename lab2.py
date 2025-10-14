from flask import Blueprint, url_for, request, redirect, abort, render_template
lab2 = Blueprint("lab2", __name__)


@lab2.route('/lab2/a')
def a():
    return "без слэша"

@lab2.route('/lab2/a/')
def a2():
    return "со слэшем"

flowers_list = [
    {'name': 'Роза', 'price': 150},
    {'name': 'Тюльпан', 'price': 80},
    {'name': 'Ромашка', 'price': 50},
    {'name': 'Орхидея', 'price': 300},
    {'name': 'Лилия', 'price': 120}
]

@lab2.route("/lab2/flowers/<int:flower_id>")
def flowers_id(flower_id):
    if flower_id >= len(flowers_list):
        abort(404)
    else:
        return render_template('flowers.html', page_type = 'flowers_id', flower_id=flower_id, flowers_list=flowers_list)
        
@lab2.route("/flowers_full/")
def flowers_full():
    return render_template('flowers.html', page_type = 'flowers_full', flowers_list=flowers_list)

@lab2.route("/flowers_clear/")
def flowers_clear():
        global flowers_list
        flowers_list = []
        return redirect("/flowers_full/")
          
@lab2.route("/lab2/add_flower/")
def flower_empty():
    return render_template('flowers.html', page_type = 'flower_empty', flowers_list=flowers_list), 400  

@lab2.route("/lab2/flowers/")
def flower_id_empty():
    return render_template('flowers.html', page_type = 'flower_base_add', flowers_list=flowers_list)
   
@lab2.route("/lab2/flower_base_add_id/")
def flower_base_add_id():
    if flowers_list:
        last_flower = flowers_list[-1]
        return redirect(f"/lab2/flowers/{len(flowers_list)-1}")        
    else:
        return redirect("/flowers_full/") 
    
@lab2.route("/lab2/add_flower/<name>")
def add_flowers(name):
        flowers_list.append(name)
        return render_template('flowers.html', page_type = 'add_flowers', flowers_list=flowers_list, name=name)
        
@lab2.route("/lab2/delete_flower/<int:flower_id>")
def delete_flower(flower_id):
    global flowers_list
    if flower_id >= len(flowers_list):
        abort(404)
    flowers_list.pop(flower_id)
    return redirect("/flowers_full/")

@lab2.route("/lab2/delete_flower/")
def delete_flower_empty():
    return render_template('flowers.html', page_type = 'delete_flower_empty', flowers_list=flowers_list)


@lab2.route("/lab2/add_flower_with_price", methods=['POST'])
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



@lab2.route("/lab2/calc/")
def calc_empty():
    return redirect("/lab2/calc/1/1")

@lab2.route("/lab2/calc/<int:first>")
def calc_second_empty(first):
    return redirect(f"/lab2/calc/{first}/1")

@lab2.route("/lab2/example/")
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
     
@lab2.route("/lab2/calc/<int:first>/<int:second>")
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

@lab2.route("/lab2/")
def lab():
    return render_template('lab2.html')
    
@lab2.route("/lab2/filters")
def filters():
    phrase = 'O <b>сколько</b> <u>нам</u> <i>открытий</i> чудных...'
    return render_template('filters.html', phrase = phrase) 

@lab2.route("/lab2/book/")
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

@lab2.route("/lab2/images/")
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