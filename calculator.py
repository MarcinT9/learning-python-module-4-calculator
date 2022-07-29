import logging
logging.basicConfig(level=logging.DEBUG)

def add(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

choice = input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ')

num1 = float(input('Podaj składnik 1. '))
num2 = float(input('Podaj składnik 2. '))

if choice == '1':
    logging.debug('Dodaję {} i {}'.format(num1, num2))
    print('Wynik to ', add(num1, num2))