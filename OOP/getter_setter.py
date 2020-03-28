class Point: 
    WIDTH = 5
    
    def __init__(self, x, y):
        print('Создание экземпляра класса')
        self.x = x 
        self.y = y

    # Геттер
    # Перегрузка метода вызывающегося при чтении свойств
    # object.__getattribute__(self, key) 
    def __getattribute__(self, key): 

        print(f'Чтение свойства с именем {key}')
        print( f'{key} = {object.__getattribute__(self, key)}')
        return object.__getattribute__(self, key)

    # Сеттер
    # Вызывается при записи свойств
    def __setattr__(self, key, value):
        print('Свойство добавлено/изменено')

        if key == 'WIDTH': # Запрещаем менять свойство WIDTH
            raise AttributeError
        else:
            self.__dict__[key] = value # изменяем свойства избегая рекурсии вызовов __setattr__

    # Вызывается если свойства нет
    def __getattr__(self, item):
        print('Обращение к несуществующему свойству')

    # Вызывается при удалении свойства
    def __delattr__(self, item):
        print('Произошло удаление')

pt = Point(0, 0)
# pt.WIDTH = 0
print(pt.WIDTH)
print(pt.WI)
del pt.x



