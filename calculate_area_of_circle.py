# This fucntion can calculate the area of a circle

def circle_area(radius):
    pi = 3.14
    area = pi * radius
    return f'The are of the circle is {area:.2f}'

print(circle_area(5))
print(circle_area(10))
