class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def show(self):
        print(self.x,self.y)
    def move(self, x, y):
        self.x+=x
        self.y+=y
    def dist(self, c):
        dx=self.x - c.x
        dy=self.y - c.y
        return (dx ** 2 + dy ** 2) ** (0.5)
p1 = Point(8, 4)
p2 = Point(5, 9)
p1.show()
p2.show()
p1.move(1,3)
p1.show()
print(p1.dist(p2))