string='x'

try:
    while True:
        string=string+string
        print(len(string))
except MemoryError:
    print("Koniec Pamięci")
        