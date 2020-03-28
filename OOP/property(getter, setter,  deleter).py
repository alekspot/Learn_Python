class Point:
    # Конструктор
    def __init__(self, x = 0, y = 0):
        print('Создание экземпляра класса')
        self.__x = x
        self.__y = y

    # Геттер для свойства coordX
    def __getCoordX(self):
        print('Чтение свойства coordX')
        return self.__x

    # Сеттер для свойства coordX
    # - можно добавлять различные проверки при записи
    def __setCoordX(self, x):
        print('Запись свойства coordX')
        return self.__x

    def __delCoordX(self):
        print('Удаление свойства coordX')
    # Создаем свойство и указываем функции вызывающиеся при чтении и записи
    coordX = property(__getCoordX, __setCoordX)
    
pt = Point(1, 2)
pt.coordX = 100