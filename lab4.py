from flask import Blueprint, render_template, request
lab4 = Blueprint('lab4',__name__)


@lab4.route("/lab4/")
def lab():
    return render_template('lab4.html')

@lab4.route('/lab4/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'alex' and password == '123':
        return render_template('success.html', username=username)

    if not username and not password:
        error = 'Введите логин и пароль'
        return render_template('login.html', error=error, username=username, password=password)
    elif not username:
        error = 'Не введен логин'
        return render_template('login.html', error=error, username=username, password=password)
    elif not password:
        error = 'Не введен пароль'
        return render_template('login.html', error=error, username=username, password=password)
    else:
        error = "Неверные логин и/или пароль"
        return render_template("login.html", error=error, username=username, password=password)
    
@lab4.route("/lab4/fridge", methods = ['GET', 'POST'])
def fridge():
    if request.method == 'GET':
        return render_template('fridge.html')

    temp = request.form.get('temp')
    if not temp:
        error = 'ошибка: не задана температура'
        return render_template('fridge.html', error=error, temp=temp)
    elif (int(temp) < -12):
        error = 'не удалось установить температуру — слишком низкое значение'
        return render_template('fridge.html', error=error, temp=temp)
    elif (int(temp) > -1):
        error = 'не удалось установить температуру — слишком высокое значение'
        return render_template('fridge.html', error=error, temp=temp)

    elif (int(temp) >= -12 and int(temp) <= -9):
        error = f'Установлена температура: {temp}°С ❄️❄️❄️'
        return render_template('temp.html', error=error, temp=temp)
    elif (int(temp) >= -8 and int(temp) <= -5):
        error = f'Установлена температура: {temp}°С ❄️❄️'
        return render_template('temp.html', error=error, temp=temp)    
    elif (int(temp) >= -4 and int(temp) <= -1):
        error = f'Установлена температура: {temp}°С ❄️'
        return render_template('temp.html', error=error, temp=temp)    


@lab4.route("/lab4/seed", methods = ['GET', 'POST'])
def seed():
    price = 0
    if request.method == 'GET':
        return render_template('seed.html')
    seed = request.form.get('seed')
    weight = request.form.get('weight')

    if seed == 'ячмень':
        price = 12000
    elif seed == 'пшеница':
        price = 8500
    elif seed == 'овёс':
        price = 8700   
    else:
        price = 14000  

    if not weight :
        error = 'Введите вес'
        return render_template('seed.html', error=error, weight=weight, price=price)

    else:
        weight=int(weight)
        if weight > 50 and weight < 500 and weight == 500:
            error='Применена скидка 10% за большой объем'
            price = (price * weight) * 0.9
            return render_template('receipt.html', price=price, error=error, weight=weight)
        elif weight > 500:
            error='Такого объёма сейчас нет в наличии'
            return render_template('seed.html', price=price, error=error, weight=weight)
        elif weight < 0 or weight == 0:
            error='Неверное значение веса'
            return render_template('seed.html', price=price, error=error, weight=weight)
        else:
            error=''
            price = price * weight
            return render_template('receipt.html', price=price, error=error, weight=weight)
      

@lab4.route("/lab4/cookies", methods = ['GET', 'POST'])
def cookies():
    if request.method == 'GET':
        return render_template('cookies.html')
    
    color = request.form.get('color')
    if color is not None:
        headers = {
            'Set-Cookie': 'color=' + color + '; path=/',
            'Location': '/lab4/cookies'
        }
        return '', 303, headers
    else:
        # Handle the case when no color is selected
        return 'Please select a color.', 400