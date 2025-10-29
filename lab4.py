from flask import Blueprint, render_template, request, redirect, session
lab4 = Blueprint("lab4", __name__)

@lab4.route('/lab4/')
def lab():
    return render_template('/lab4/lab4.html')

@lab4.route('/lab4/div-form')
def lab4_div_form():
    return render_template("/lab4/div-form.html", current_page='lab4_div')

@lab4.route('/lab4/mult-form')
def lab4_mult_form():
    return render_template("/lab4/div-form.html", current_page='lab4_mult')

@lab4.route('/lab4/add-form')
def lab4_add_form():
    return render_template("/lab4/div-form.html", current_page='lab4_add')

@lab4.route('/lab4/sub-form')
def lab4_sub_form():
    return render_template("/lab4/div-form.html", current_page='lab4_sub')

@lab4.route('/lab4/expo-form')
def lab4_expo_form():
    return render_template("/lab4/div-form.html", current_page='lab4_expo')

@lab4.route('/lab4/div', methods=['POST'])
def lab4_div():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template("/lab4/div-form.html", current_page='lab4_div',error='Оба поля должны быть заполнены!')
    x1 = int(x1)
    x2 = int(x2)
    if x2 == 0:
        return render_template("/lab4/div-form.html", x1=x1, x2=x2, current_page='lab4_div',error='Деление на ноль невозможно!')
    result = x1 / x2
    return render_template("/lab4/div-form.html", x1=x1, x2=x2, result=result, current_page='lab4_div')


@lab4.route('/lab4/mult', methods=['POST'])
def lab4_mult():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        x1 = int(x1) if x1 else 1
        x2 = int(x2) if x2 else 1
        result = x1 * x2
        return render_template("/lab4/div-form.html", x1=x1, x2=x2, result=result, current_page='lab4_mult')
    x1 = int(x1)
    x2 = int(x2)
    result = x1 * x2
    return render_template("/lab4/div-form.html", x1=x1, x2=x2, result=result,current_page='lab4_mult')

@lab4.route('/lab4/add', methods=['POST'])
def lab4_add():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    
    if x1 == '' or x2 == '':
        x1 = int(x1) if x1 else 0
        x2 = int(x2) if x2 else 0
        result = x1 + x2
        return render_template("/lab4/div-form.html", x1=x1, x2=x2, result=result,current_page='lab4_add')
    x1 = int(x1)
    x2 = int(x2)
    result = x1 + x2
    return render_template("/lab4/div-form.html", x1=x1, x2=x2, result=result,current_page='lab4_add')


@lab4.route('/lab4/sub', methods=['POST'])
def lab4_sub():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template("/lab4/div-form.html", current_page='lab4_div',error='Оба поля должны быть заполнены!')

    x1 = int(x1)
    x2 = int(x2)
    result = x1 - x2
    return render_template("/lab4/div-form.html", x1=x1, x2=x2, result=result,current_page='lab4_sub')
    

@lab4.route('/lab4/expo', methods=['POST'])
def lab4_expo():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template("/lab4/div-form.html", current_page='lab4_div',error='Оба поля должны быть заполнены!')
    x1 = int(x1)
    x2 = int(x2)
    if x1 == 0 and x2 == 0:
        return render_template("/lab4/div-form.html", current_page='lab4_div',error='Оба числа не могут быть равны нулю!')
    result = x1 ** x2
    return render_template("/lab4/div-form.html", x1=x1, x2=x2, result=result,current_page='lab4_expo')
    
    
tree_count = 0
tree_max = 10  

@lab4.route('/lab4/tree', methods=['GET', 'POST'])
def tree():
    global tree_count
    if request.method == "GET":
        return render_template('lab4/tree.html', tree_count=tree_count, tree_max=tree_max)
    
    operation = request.form.get('operation')
    
    if operation == 'cut':
        if tree_count > 0: 
            tree_count -= 1
    elif operation == 'plant':
        if tree_count < tree_max: 
            tree_count += 1
    
    return redirect('/lab4/tree')

users = [
    {'login': 'alex', 'password': '123', 'name': 'Александр Петров', 'gender': 'male'},
    {'login': 'admin', 'password': 'admin', 'name': 'Администратор Системы', 'gender': 'male'},
    {'login': 'maria', 'password': 'password', 'name': 'Мария Иванова', 'gender': 'female'},
    {'login': 'user', 'password': '12345', 'name': 'Иван Сидоров', 'gender': 'male'}
]

@lab4.route('/lab4/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        if 'login' in session:
            authorized = True
            user_info = None
            for user in users:
                if user['login'] == session['login']:
                    user_info = user
                    break
            if user_info:
                name = user_info['name']
                gender = user_info['gender']
            else:
                name = session['login']
                gender = ''
            return render_template('lab4/login.html', authorized=authorized, name=name, gender=gender)
        else:
            authorized = False
            return render_template('lab4/login.html', authorized=authorized)
    
    login = request.form.get('login')
    password = request.form.get('password')
    errors = []
    if login == '':
        errors.append('Не введён логин')
    if password == '':
        errors.append('Не введён пароль')
    if errors:
        return render_template('lab4/login.html', errors=errors, authorized=False, login=login)
    
    user_info = None
    for user in users:
        if login == user['login'] and password == user['password']:
            user_info = user
            break
    if user_info:
        session['login'] = login
        return redirect('/lab4/login')
    
    errors = ['Неверные логин и/или пароль']
    return render_template('lab4/login.html', errors=errors, authorized=False, login=login)

@lab4.route('/lab4/logout', methods=['POST'])
def logout():
    session.pop('login', None)
    return redirect('/lab4/login')
    
    
@lab4.route('/lab4/fridge')
def fridge_form():
    return render_template('lab4/fridge.html')

@lab4.route('/lab4/fridge', methods=['POST'])
def fridge():
    temperature = request.form.get('temperature')
    
    if temperature == '':
        return render_template('lab4/fridge.html', error='Ошибка: не задана температура')
    else:
        temp = int(temperature)
    
        if temp < -12:
            return render_template('lab4/fridge.html', error='Не удалось установить температуру — слишком низкое значение')
        elif temp > -1:
            return render_template('lab4/fridge.html', error='Не удалось установить температуру — слишком высокое значение')
        elif -12 <= temp <= -9:
            snowflakes = 3
            message = f'Установлена температура: {temp}°C'
        elif -8 <= temp <= -5:
            snowflakes = 2
            message = f'Установлена температура: {temp}°C'
        elif -4 <= temp <= -1:
            snowflakes = 1
            message = f'Установлена температура: {temp}°C'
        else:
            snowflakes = 0
            message = f'Установлена температура: {temp}°C'
        return render_template('lab4/fridge.html', message=message, snowflakes=snowflakes, temperature=temp)
    
@lab4.route('/lab4/grain')
def grain_form():
    return render_template('lab4/grain.html')

@lab4.route('/lab4/grain', methods=['POST'])
def grain():
    grain_type = request.form.get('grain_type')
    weight = request.form.get('weight')
    
    prices = {
        'barley': 12000,   
        'oats': 8500,      
        'wheat': 9000,     
        'rye': 15000       
    }
    
    grain_names = {
        'barley': 'ячмень',
        'oats': 'овёс', 
        'wheat': 'пшеница',
        'rye': 'рожь'
    }
    
    if grain_type == '':
        return render_template('lab4/grain.html', error='Выберите тип зерна')
    
    if weight == '':
        return render_template('lab4/grain.html', error='Укажите вес заказа')
    
    else:
        weight_val = float(weight)
    
        if weight_val <= 0:
            return render_template('lab4/grain.html', error='Вес должен быть больше 0')
        
        if weight_val > 100:
            return render_template('lab4/grain.html', error='Такого объёма сейчас нет в наличии')
        
        price_per_ton = prices[grain_type]
        total = weight_val * price_per_ton
        
        discount = 0
        if weight_val > 10:
            discount = total * 0.10  
            total -= discount
        
        grain_name = grain_names[grain_type]
        
        return render_template('lab4/grain.html', success=True, grain_name=grain_name, 
                            weight=weight_val, total=total, discount=discount, selected_grain=grain_type)

    
@lab4.route('/lab4/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab4/register.html')
    
    # Получаем данные из формы
    login = request.form.get('login')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')
    name = request.form.get('name')
    gender = request.form.get('gender')
    
    errors = []
    if login == '':
        errors.append('Не введён логин')
    if password == '':
        errors.append('Не введён пароль')
    if confirm_password == '':
        errors.append('Не введено подтверждение пароля')
    if name == '':
        errors.append('Не введено имя')
    if password != confirm_password:
        errors.append('Пароли не совпадают')
    
    if login and any(user['login'] == login for user in users):
        errors.append('Пользователь с таким логином уже существует')
    
    if errors:
        return render_template('lab4/register.html', errors=errors, login=login, name=name, gender=gender)
    
    new_user = {
        'login': login,
        'password': password,
        'name': name,
        'gender': gender
    }
    users.append(new_user)
    
    return render_template('lab4/register.html', success='Регистрация успешна! Теперь вы можете войти.')


@lab4.route('/lab4/users')
def users_list():
    if 'login' not in session:
        return redirect('/lab4/login')
    current_user_login = session['login']
    return render_template('lab4/users.html', users=users, current_user_login=current_user_login)


@lab4.route('/lab4/users/delete', methods=['POST'])
def delete_user():
    if 'login' not in session:
        return redirect('/lab4/login')
    current_user_login = session['login']
    global users
    users = [user for user in users if user['login'] != current_user_login]
    session.pop('login', None)
    return redirect('/lab4/login')


@lab4.route('/lab4/users/edit', methods=['GET', 'POST'])
def edit_user():
    if 'login' not in session:
        return redirect('/lab4/login')
    
    current_user_login = session['login']
    current_user = next((user for user in users if user['login'] == current_user_login), None)
    
    if current_user == '':
        session.pop('login', None)
        return redirect('/lab4/login')
    
    if request.method == 'GET':
        return render_template('lab4/edit_user.html', user=current_user)
    
    login = request.form.get('login')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')
    name = request.form.get('name')
    gender = request.form.get('gender')
    
    errors = []
    
    if not login:
        errors.append('Не введён логин')
    if not name:
        errors.append('Не введено имя')
    
    if login != current_user_login and any(user['login'] == login for user in users):
        errors.append('Пользователь с таким логином уже существует')
    
    if password or confirm_password:
        if password != confirm_password:
            errors.append('Пароли не совпадают')
        if not password:
            errors.append('Не введён пароль')
    
    if errors:
        return render_template('lab4/edit_user.html', user=current_user, errors=errors)
    
    current_user['login'] = login
    current_user['name'] = name
    current_user['gender'] = gender
    
    if password:
        current_user['password'] = password
    
    session['login'] = login
    
    return redirect('/lab4/users')
    
    
    
    
    
    
    
    
    
    
    
    
    