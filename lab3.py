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
    resp.delete_cookie('color')
    resp.delete_cookie('background')
    resp.delete_cookie('font_size')
    resp.delete_cookie('font_family')
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
    
    resp = make_response(render_template('lab3/pay.html', price=price))
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
    font_family = request.args.get('font_family') 
    
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

    return render_template('lab3/settings.html', color=current_color,
                                                background=current_background, 
                                                font_size=current_font_size, 
                                                font_family=current_font_family)


@lab3.route('/lab3/ticket')
def form_ticket():
    errors = {}
    base_price = 0
    ticket_type = ''
    fio = request.args.get('fio')
    shelf = request.args.get('shelf')
    linen = request.args.get('linen')
    baggage = request.args.get('baggage')
    age = request.args.get('age')
    departure = request.args.get('departure')
    destination = request.args.get('destination')
    date = request.args.get('date')
    insurance = request.args.get('insurance')
    if fio == '':
        errors['fio'] = 'Заполните ФИО'
    if shelf == '':
        errors['shelf'] = 'Выберите полку'
    if linen == '':
        errors['linen'] = 'Укажите наличие белья'
    if baggage == '':
        errors['baggage'] = 'Укажите наличие багажа'
    if age == '':
        errors['age'] = 'Заполните возраст'
    if age is not None:  
        if age.strip() == '':  
            errors['age'] = "Заполните возраст"
        elif int(age) < 1 or int(age) > 120:
            errors['age'] = "Возраст должен быть от 1 до 120 лет"
    if departure == '':
        errors['departure'] = 'Заполните пункт выезда'
    if destination == '':
        errors['destination'] = 'Заполните пункт назначения'
    if date == '':
        errors['date'] = 'Выберите дату поездки'
    if insurance == '':
        errors['insurance'] = 'Укажите наличие страховки'
    if not errors and age is not None and age.strip() != '':
        base_price = 700 if int(age) < 18 else 1000
        ticket_type = "Детский билет" if base_price == 700 else "Взрослый билет"
    else:
        return render_template('lab3/form_ticket.html', errors=errors,
                         fio=fio,
                         shelf=shelf,
                         linen=linen,
                         baggage=baggage,
                         departure=departure,
                         destination=destination,
                         date=date,
                         base_price=base_price,
                         ticket_type=ticket_type,
                         insurance=insurance)

    additional_services = []
    
    if shelf in ['lower', 'lower_side']:
        base_price += 100
        additional_services.append("+100 руб. (выбранная полка)")
    
    if linen == 'yes':
        base_price += 75
        additional_services.append("+75 руб. (бельё)")
    
    if baggage == 'yes':
        base_price += 250
        additional_services.append("+250 руб. (багаж)")
    
    if insurance == 'yes':
        base_price += 150
        additional_services.append("+150 руб. (страховка)")
    
    return render_template('lab3/form_ticket.html',
                         errors=errors,
                         fio=fio,
                         shelf=shelf,
                         linen=linen,
                         baggage=baggage,
                         age=age,
                         departure=departure,
                         destination=destination,
                         date=date,
                         base_price=base_price,
                         ticket_type=ticket_type,
                         insurance=insurance,
                         additional_services=additional_services)


    
    
    







    
    
    