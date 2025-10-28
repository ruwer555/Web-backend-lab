from flask import Blueprint, render_template, request
lab4 = Blueprint("lab4", __name__)

@lab4.route('/lab4/')
def lab():
    return render_template('/lab4/lab4.html')


@lab4.route('/lab4/div-form')
def lab4_div_form():
    return render_template("/lab4/div-form.html", page_type='form')

@lab4.route('/lab4/div', methods=['POST'])
def lab4_div():
    errors = {}
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x2 == '' or x1 == '':
        return render_template("/lab4/div-form.html", x1=x1, x2=x2, page_type='form', error='Оба поля должны быть заполнены!')
    x1 = int(x1)
    x2 = int(x2)
    if x2 == 0:
        errors['x2'] = 'Деление на ноль невозможно!'  
        return render_template("/lab4/div-form.html", x1=x1, x2=x2, page_type='lab4_div', errors=errors)
    
    result = x1 / x2
    return render_template("/lab4/div-form.html", x1=x1, x2=x2, result=result, page_type='lab4_div', errors={})

    






