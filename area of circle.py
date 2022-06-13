import math

r = float(input('Enter the radius of the circle :'))
area = math.pi * r * r

print("Area of the circle is : %.16f" %area)

filename = input("Enter Filename: ")
f = filename.split(".")   #split-dividing the linento two

print ("Extension of the file is : " + f[-1])
