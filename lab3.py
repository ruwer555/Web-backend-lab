from flask import Blueprint, render_template, redirect, url_for, request, make_response
lab3 = Blueprint("lab3", __name__)

@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name') or 'Неизвестный'
    age = request.cookies.get('age') or 'Не указано'
    name_color = request.cookies.get('name_color')
    return render_template('/lab3/lab3.html', name=name, age=age, name_color=name_color)


@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20', max_age=5)
    resp.set_cookie('name_color', 'magenta')
    return resp


@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp


@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    age = request.args.get('age')
    sex = request.args.get('sex')
    return render_template('/lab3/form1.html', user=user, age=age, sex=sex, errors=errors)


@lab3.route('/lab3/order')
def order():
    return render_template('/lab3/order.html')


@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'coffee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70
    
    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10
    
    # Создаем response с шаблоном
    resp = make_response(render_template('lab3/pay.html', price=price))
    # Устанавливаем куки
    resp.set_cookie('price', str(price))
    return resp


@lab3.route('/lab3/success')
def success():
    price = request.cookies.get('price', 0)
    return render_template('lab3/success.html', price=int(price))


@lab3.route('/lab3/settings')
def settings():
    color = request.args.get('color')
    background = request.args.get('background')
    font_size = request.args.get('font_size')
    font_family = request.args.get('font_family')  # исправлено: было font_size
    
    # Получаем текущие значения из куки
    current_color = request.cookies.get('color')
    current_background = request.cookies.get('background')
    current_font_size = request.cookies.get('font_size')
    current_font_family = request.cookies.get('font_family')
    
    if color or background or font_size or font_family:
        resp = make_response(redirect('/lab3/settings'))
        if color:
            resp.set_cookie('color', color)
        if background:
            resp.set_cookie('background', background)
        if font_size:
            resp.set_cookie('font_size', font_size)
        if font_family:
            resp.set_cookie('font_family', font_family)
        return resp
    
    # Рендерим шаблон с текущими значениями
    return render_template('lab3/settings.html', color=current_color, background=current_background, font_size=current_font_size, font_family=current_font_family)




    
    
    
    







    
    
    