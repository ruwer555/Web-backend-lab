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
    
    
    
    
    
    
    
    
    
    
    
    
    