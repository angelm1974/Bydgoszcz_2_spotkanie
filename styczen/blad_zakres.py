v=0
def czytaj_int(prompt, min, max):
    ok=False
    while not ok:
        try:
            wartosc=int(input(prompt))
            ok=True
        except ValueError:
            print("Błędna wartość na wejściu")
        if ok:
            ok=wartosc >= min and wartosc <= max
        if not ok:
            print("Błąd Wartość spoza zakresu",min, "a",max)
            wartosc=czytaj_int("Wprowadź wartość spomiędzy zakresu -10 a 10", -10,10)
        return wartosc
v=czytaj_int("Wprowadź wartość spomiędzy zakresu -10 a 10", -10,10)

print("Wybrany numer to: ",v)
