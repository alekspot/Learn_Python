class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __str__(self): # отвечает за вывод объекта
        return f"({self.x}, {self.y})"

#print( issubclass(Point, object))

# Наследование
class Prop:
    def __init__(self, sp: Point, ep: Point):
        print("Вызов конструктора класса Prop")
        # protected свойства
        # оговаривается что доступ к ним может быть только внутри класса или в наследуемом классе
        # не слудет их вызывать извне классов(напрямую через экземпляр), чтобы случайным образом их не переопределить
        self._sp = sp

        # Приватные свойства создаются с префиксом класса _Prop
        self.__ep = ep 
    def getSp():
        return self.__sp

class Line(Prop):
    def drowLine(self):
        print(f"Линия: {self.__sp}, {self.__ep}")

class Rect(Prop):
    def __init__(self, *args ): # Переопределение конструктора
        print("Вызов конструктора класса Rect")
        super().__init__(*args) # Вызов базового конструктора

    def drowRect(self):
        print(f"Прямоугольник: {self.__sp}, {self.__ep}")


rect = Rect(Point(5,10), Point(5,10))
#rect.drowRect()

print(rect.__dict__)