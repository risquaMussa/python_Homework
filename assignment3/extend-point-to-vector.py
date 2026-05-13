#Task 5: Extending a Class
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):

        return self.x == other.x and self.y == other.y

    def distance_to(self, other):

        return math.sqrt(
            (other.x - self.x) ** 2 +
            (other.y - self.y) ** 2
        )
    
    
    
point = Point(3, 4)
print(point)

class Vector(Point):
    def __str__(self):

        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):

        return Vector(
            self.x + other.x,
            self.y + other.y
        )
        
point1 = Point(1, 2)
point2 = Point(1, 2)
point3 = Point(4, 6)

print(point1)

print(point1 == point2)   
print(point1.distance_to(point3))
vector1 = Vector(1, 2)
vector2 = Vector(3, 4)
print(vector1)
print(vector1 + vector2)    