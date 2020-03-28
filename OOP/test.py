class Point:
    x = 0

    def __init__(self, x):
        self.x = x

    @staticmethod
    def printStaticX(self):
        print(self)


pt = Point(2)
print(pt.x)
pt.printStaticX(1)