_lista = [1, 2, 3, 4, 5]
ix = 0

dzialaj=True
while dzialaj:
    try:
        print(_lista[ix])
        ix+=1
    except IndexError:
        dzialaj=False

print('Zrobione')