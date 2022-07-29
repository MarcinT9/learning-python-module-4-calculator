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
    logging.debug(f'Dodaję {num1:.2f} i {num2:.2f}')
    add_result = add(num1, num2)
    print(f'Wynik to {add_result:.2f}')

elif choice == '2':
    logging.debug(f'Odejmuję {num1:.2f} i {num2:.2f}')
    subtraction_result = subtraction(num1, num2)
    print(f'Wynik to {subtraction_result:.2f}')

elif choice == '3':
    logging.debug(f'Mnożę {num1:.2f} i {num2:.2f}')
    multiplication_result = multiplication(num1, num2)
    print(f'Wynik to {multiplication_result:.2f}')

elif choice == '4':
    logging.debug(f'Dzielę {num1:.2f} i {num2:.2f}')
    division_result = division(num1, num2)
    print(f'Wynik to {division_result:.2f}')

elif choice >= '5':
    print('Nie wybrałeś poprawnie działania')
    