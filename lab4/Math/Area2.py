from math import tan,pi
def Polygon(num_of_sides,len_of_side):
    Area = (len_of_side ** 2 * num_of_sides) / 4 * tan(pi / num_of_sides)
    return Area

print(Polygon(4,25))

