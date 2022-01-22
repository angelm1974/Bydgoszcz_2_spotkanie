def blad_1(n):
    raise ValueError

try:
    blad_1("A")
except (ArithmeticError,ValueError,TypeError):
        print("Niestety mamy błąd")
        
print("koniec")
