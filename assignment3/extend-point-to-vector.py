#import libs
import math

#Task 5: Extending a Class

#Point class declaration
class Point:
    #constructor
    #x:int - coordinate x
    #y:int - coordinate y
    def __init__(self, x,y):
        try:
            #try to create an object 
            self.x = int(x)
            self.y = int(y)
        except Exception as e:
            print("Coordinates should be numbers!")
            #create an object with defaule coordinates
            self.x = 0
            self.y = 0
        finally:
            #print the result of object creation
            print(f'Created an object - {str(self)}')
    
    #method that compare point with another point
    #other:Point - another point to comapare with
    #return:boolean - result of comparison. By default - False
    def __eq__(self, other):
        try:
            return self.x == other.x and self.y == other.y 
        except Exception as e:
            print("Comparison could be possible only between points!")
            return False
    
    #method to string representation
    def __str__(self):
        return f'Point({self.x},{self.y})'
    
    #method that calculates Euclidian distance between point and another point
    #other:Point - another point
    #return:float - Euclidian distance
    def get_distance_to(self, other):
        try:
            return math.sqrt((self.x-other.x)**2 + (self.y - other.y)**2)
        except Exception as e:
            print("Euclidian distance could be calculated only between points!")


class Vector(Point):
    def __init__(self, x,y):
        super().__init__(x,y)
    
    def __str__(self):
        return f'Vector({self.x},{self.y})'
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)

#check the result

#point initialization
point1 = Point(1,5)
print(str(point1))
point2 = Point("3",1)
point2 = Point("Ad",1)
print(str(point2))
point2 = Point(1,5)
point3 = Point(4,-2)

#points comparisson
print(point1 == point2)
print(point1 == point3)
print(point1 == 1)

#distance calculations
print(point1.get_distance_to(point2))
print(point1.get_distance_to(point3))
print(point1.get_distance_to(1))

#vector initialization
vector1 = Vector(3,-7)
vector2 = Vector("x","y")
vector2 = Vector("-4", 5)

#vector comparison ( inherited method)
print(vector1 == vector2)

#vector addition
print(vector1 + vector2)

