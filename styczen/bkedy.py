
try:
    pierwsza=int(input("Podaj pierwszą liczbę"))
    druga=int(input("Podaj DRUGA liczbę"))
    print(pierwsza/druga)
except ArithmeticError:
    print("Pamiętaj cholero nie dziel przez 0")
except ZeroDivisionError:
    print("UWAGA cholero nie dziel przez 0")
except ValueError:
    print("Podałeś nieprawidłową wartość, być może literę!!!!!")
except:
    print("wystąpił nieznany błądz powodu nieznanego błędu!!!")
print("koniec działąnia")    