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
    add_result = add(num1, num2)
    print(f'Wynik to {add_result:.2f}')

elif choice == '2':
    logging.debug('Odejmuję {} i {}'.format(num1, num2))
    subtraction_result = subtraction(num1, num2)
    print(f'Wynik to {subtraction_result:.2f}')

elif choice == '3':
    logging.debug('Mnożę {} i {}'.format(num1, num2))
    multiplication_result = multiplication(num1, num2)
    print(f'Wynik to {multiplication_result:.2f}')

elif choice == '4':
    logging.debug('Dzielę {} i {}'.format(num1, num2))
    division_result = division(num1, num2)
    print(f'Wynik to {division_result:.2f}')

else:
    logging.error('Niewłaściwa wartość')