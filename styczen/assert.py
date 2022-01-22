import math
try:
    x=input("Wpisz składnik: ")
    assert x.lower()not in ['ananas', 'majonez','anchoies']

    print("Pizza ma fajny składnik", x)


except (ArithmeticError,ValueError,TypeError):
        print("Niestety mamy błąd")
except AssertionError:
    print('Nie taki składnik do pizzy')