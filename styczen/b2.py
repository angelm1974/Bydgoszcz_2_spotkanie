def blad_1(n):
    try:
        return 1/n
    except (ArithmeticError,ValueError,TypeError):
        print("Niestety mamy błąd")
        
    return None

blad_1("A")