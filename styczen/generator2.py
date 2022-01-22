class Generator_z_Listy:
    def __init__(self,nn):
        self.__n=nn
        self.__i=-1
        self.__lista=['majonez','oliwki', 'kiełbasa', 'sok','kotlet']

   
    def __iter__(self):
        return self
    
    def __next__(self):
        self.__i+=1
        if self.__i>len(self.__lista)-1 or self.__i>self.__n:
            raise StopIteration
        return self.__lista[self.__i]
        
for i in Generator_z_Listy(2):
    print(i) 

