class Point:

# Статическое свойство класса доступно всем экземплярам
    count = 0 

    # Конструктор
    # Создает локальные свойства экземплярам
    def __init__(self, x = 0, y = 0):
        print('Создание экземпляра класса')
        self.x = x
        self.y = y
    
pt = Point(1,1)

print(pt.count)