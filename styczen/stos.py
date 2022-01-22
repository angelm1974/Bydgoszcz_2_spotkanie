class Stack:
    def __init__(self):
        self.__stos_lista = []

    def push(self, val):
        self.__stos_lista.append(val)

    def pop(self):
        val = self.__stos_lista[-1]
        del self.__stos_lista[-1]
        return val


maly_stos = Stack()
inny_stos = Stack()
zabawny_stos = Stack()

maly_stos.push(1)
inny_stos.push(maly_stos.pop() + 1)
zabawny_stos.push(inny_stos.pop() - 2)

print(zabawny_stos.pop())
print(zabawny_stos.pop())
