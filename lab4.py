from flask import Blueprint, render_template, request, redirect
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

@lab4.route('/lab4/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('lab4/login.html', authorized=False)
    login = request.form.get('login')
    password = request.form.get('password')
    if login =='alex' and password == '123':
        return render_template('lab4/login.html', login=login, password= password, authorized=True)
    error = 'Неверные логин и/или пароль'
    return render_template('lab4/login.html', error=error, authorized=False)
    
    
    
    
    
    
    
    
    
    
    
    
    