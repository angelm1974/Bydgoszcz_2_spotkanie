def fun(n):
    for i in range(n):
        yield i
    


def potega_2(n):
    potega=1
    for i in range(n):
        yield potega 
        potega *= 2
        
# for a in potega_2(8):

# x=[a for a in potega_2(5)]
# print(x)

for i in range(20):
    if i in potega_2(4):
      print(i)  
