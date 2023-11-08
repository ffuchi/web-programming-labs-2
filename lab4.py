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
        return render_template('fridge.html', error=error, temp=temp)
    elif (int(temp) >= -8 and int(temp) <= -5):
        error = f'Установлена температура: {temp}°С ❄️❄️'
        return render_template('fridge.html', error=error, temp=temp)    
    elif (int(temp) >= -4 and int(temp) <= -1):
        error = f'Установлена температура: {temp}°С ❄️'
        return render_template('fridge.html', error=error, temp=temp)    