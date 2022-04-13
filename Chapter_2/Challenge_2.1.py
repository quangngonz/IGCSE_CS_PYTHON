import math

diameter = float(input("Enter the diameter of the sphere: "))

def calculate_volume(diameter):
    return 4/3 * math.pi * (diameter/2)**3

print("The volume of the sphere is: ", calculate_volume(diameter), "m3")
