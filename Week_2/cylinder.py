# program to solve the volume of a cylinder
# date: 20/02/2024
# name : Lesley Waweru

r = int(input("Enter the radius of the cylinder :"))
h = int(input("Enter the height of the cylinder :"))
pi = 22/7

v = pi*r**2*h
print("The volume of the cylinder is ",v)

a = (2*pi*r**2)+(pi*2*r*h)
print("The surface area of the cylinder is ",a)
