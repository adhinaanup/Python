# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
class circle:
    def __init__(self,radius):
        area=3.14*radius*radius
        per=2*3.14*radius
        print('Area of the circle : ',area)
        print('Perimeter of te circle : ',per)

c=circle(2)