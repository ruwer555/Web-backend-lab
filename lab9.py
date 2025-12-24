from flask import Blueprint, render_template, request, jsonify, redirect
import random

lab9 = Blueprint('lab9', __name__)

opened_boxes = {}
positions = {}

gifts = [
    {"text": "Держи ракету!", "img": "lab9/1.webp"},
    {"text": "Ну, посмотрим что это за аппарат?", "img": "lab9/2.webp"},
    {"text": "Уф, что за пушка бомба!", "img": "lab9/3.webp"},
    {"text": "Лучшее что могло выпасть!", "img": "lab9/4.webp"},
    {"text": "Суда, теперь есть на чем поиграть!", "img": "lab9/5.webp"},
    {"text": "Без комментариев.", "img": "lab9/6.webp"},
    {"text": "О да! Теперь буду тащить!", "img": "lab9/7.webp"},
    {"text": "О да, один барабан и в ангар!", "img": "lab9/8.webp"},
    {"text": "Хах, ну хоть где-то он выпал!", "img": "lab9/9.webp"},
    {"text": "Держи, открой еще бро!", "img": "lab9/10.webp"},
]

# заранее заготовленные, разнесённые координаты
BASE_COORDS = [
    "top:10%; left:10%",
    "top:10%; left:40%",
    "top:10%; left:70%",
    "top:35%; left:10%",
    "top:35%; left:40%",
    "top:35%; left:70%",
    "top:60%; left:10%",
    "top:60%; left:40%",
    "top:60%; left:70%",
    "top:45%; left:55%",
]


@lab9.route('/lab9/')
def lab():
    client_ip = request.remote_addr

    if client_ip not in opened_boxes:
        opened_boxes[client_ip] = []

    opened = opened_boxes[client_ip]

    # для каждого IP просто перемешиваем уже готовый набор позиций
    if client_ip not in positions:
        coords = BASE_COORDS[:]      # копия
        random.shuffle(coords)
        positions[client_ip] = coords

    remaining = 10 - len(opened)

    return render_template(
        'lab9/lab9.html',
        opened=opened,
        remaining=remaining,
        coords=positions[client_ip]
    )


@lab9.route('/lab9/open_box', methods=['POST'])
def open_box():
    data = request.get_json()
    box_id = data.get('box_id')

    if box_id is None or not (0 <= box_id < len(gifts)):
        return jsonify({'error': 'Неверный номер коробки'})

    client_ip = request.remote_addr

    if client_ip not in opened_boxes:
        opened_boxes[client_ip] = []

    opened = opened_boxes[client_ip]

    if len(opened) >= 3:
        return jsonify({'error': 'Можно открыть только 3 коробки'})

    if box_id in opened:
        return jsonify({'error': 'Эта коробка уже открыта'})

    opened.append(box_id)

    gift = gifts[box_id]
    remaining = 10 - len(opened)

    return jsonify({
        'success': True,
        'gift_text': gift['text'],
        'gift_img': gift['img'],
        'remaining': remaining
    })


@lab9.route('/lab9/reset')
def reset():
    client_ip = request.remote_addr
    opened_boxes[client_ip] = []
    if client_ip in positions:
        del positions[client_ip]
    return redirect('/lab9/')
