import math
def circumference_area_of_circle(radius):
    circumference = round(2 * math.pi * radius,2)
    area = round(math.pi * radius ** 2,2 )
    return circumference, area

circumference,area = circumference_area_of_circle(5)
print(circumference,area)