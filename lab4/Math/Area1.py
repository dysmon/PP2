# Write a Python program to calculate the area of a trapezoid.

def trapezoid(height,base1,base2):
    area = (base1 + base2)/2 * height
    return area

print(trapezoid(5,5,6))
