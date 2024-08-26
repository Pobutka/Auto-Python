import math

def square(side):
    area = side ** 2
    
    if not side.is_integer():
        return math.ceil(area)
    
    return area

side_length = 4.3  
area = square(side_length)

print(f"Площадь квадрата со стороной {side_length} равна {area}")