class Point:

    # Конструктор
    # Создает локальные свойства экземплярам
    def __init__(self, x = 0, y = 0):
        print('Создание экземпляра класса')
        self.x = x
        self.y = y

    # Деструктор
    def __del__(self):
        print('Удаление экземпляра класса')




#################################################################


pt = Point()
print(pt.__dict__)

pt.setCoords(5,10)
# ===
Point.setCoords(pt, 5, 10) # Указывает на экземпляр

print(pt.__dict__)