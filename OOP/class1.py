class Point:
    # private свойства
    # Экземпляры не видят приватные свойства
    __x = 1
    __y = 1 



    # Метод
    def setCoords(self, x, y): #первым параметром всегда явлется ссылка экземпляр
        self.x = x
        self.y = y

    # private метод
    # - вызываем через класс и только в самом классе 
    # - self не передается (экземпляры не видят приватные свойства / методы)
    def __checkValue(x): 
        if isinstance(x, int) or isinstance(x, float):
            print('Число')
            return
        print('Не число')    
        return 

    def checkNumber(self, number):
        Point.__checkValue(number) # обращаемся к private методу
#########################################################################################################

pt = Point()

# Вызовет ошибку, x ссылается на статическое private свойство
# print(pt.x) 

# Не вызовет ошибку x будет ссылаться на локальную переменную
pt.x = 0
print(pt.x) 

pt.checkNumber(5)


