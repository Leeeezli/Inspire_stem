# program to solve the quadratic equation
# date: 20/02/2024
# name : Lesley Waweru
import math

a = float(input("Enter coefficient of first term : "))
b = float(input("Enter coefficient of second term : "))
c = float(input("Enter the constant term :"))


d = (b **2) - 4 * a * c

x_1 =(-b + math.sqrt(d)) / 2 * a

x_2 =(-b - math.sqrt(d)) / 2 * a

print("solution for the quadratic equation is : ",x_1)
print("solution for the quadratic equation is : ",x_2)
