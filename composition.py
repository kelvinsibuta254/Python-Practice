#composition is combining classes together to form systems

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Shape:
    def __init__(self, points):
        self.points = points

triangle = Shape(
    [
        Point(0, 0),
        Point(5, 5),
        Point(2, 4)
    ]
)

bottom_left = Point(0, 0)
bottom_right = Point(10, 0)
top_left = Point(0, 10)
top_right = Point(10, 10)

square = Shape([bottom_left, bottom_right, top_left, top_right])
print(square)

square.points