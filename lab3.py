from flask import Blueprint, render_template, request
lab3 = Blueprint('lab3',__name__)


@lab3.route("/lab3/")
def lab():
    return render_template('lab3.html')


@lab3.route("/lab3/forml")
def forml():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'

    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'

    sex = request.args.get('sex')
    return render_template('form1.html', user=user, age=age, sex=sex, errors=errors)


@lab3.route("/lab3/order")
def order():
    return render_template('order.html')

@lab3.route("/lab3/pay")
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
       price = 80
    else:
       price = 70  

    if request.args.get('milk') == 'on':
       price += 30
    if request.args.get('sugar') == 'on':
       price += 10

    return render_template('pay.html', price = price)    


@lab3.route('/lab3/success')
def success():
        return render_template('thx.html')


@lab3.route("/lab3/ticketPay")
def ticketPay():
    errors = {}
    user1 = request.args.get('user1')
    if user1 == '':
        errors['user1'] = 'Заполните поле!'
    user2 = request.args.get('user2')
    if user2 == '':
        errors['user2'] = 'Заполните поле!'
    user3 = request.args.get('user3')
    if user3 == '':
        errors['user3'] = 'Заполните поле!'
    typeTicket = request.args.get('typeTicket')
    typeShelf = request.args.get('typeShelf')
    luggage = request.args.get('luggage')
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
    departurePoint = request.args.get('departurePoint')
    if departurePoint == '':
        errors['departurePoint'] = 'Заполните поле!'
    destination = request.args.get('destination')
    if destination == '':
        errors['destination'] = 'Заполните поле!'
    date = request.args.get('date')

    return render_template('ticketPay.html', user1=user1, user2=user2, user3=user3,
                            typeTicket=typeTicket, typeShelf=typeShelf, luggage=luggage,
                            age=age, departurePoint=departurePoint, destination=destination,
                            date=date, errors=errors)

@lab3.route('/lab3/ticket')
def ticket():
    user1 = request.args.get('user1')
    user2 = request.args.get('user2')
    user3 = request.args.get('user3')
    typeTicket = request.args.get('typeTicket')
    typeShelf = request.args.get('typeShelf')
    luggage = request.args.get('luggage')
    age = request.args.get('age')
    departurePoint = request.args.get('departurePoint')
    destination = request.args.get('destination')
    date = request.args.get('date')
    return render_template('ticket.html', user1=user1, user2=user2, user3=user3,
                            typeTicket=typeTicket, typeShelf=typeShelf, luggage=luggage,
                            age=age, departurePoint=departurePoint, destination=destination,
                            date=date)