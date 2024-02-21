# program  to show how to perform geometric progression
# date: 20/02/2024
# name : Lesley Waweru

a = float(input("Enter the value of a : "))
n = float(input("Enter the value of n  :"))
r = float(input("Enter the value of r :"))

S_n = (a*(r**n-1)/(r-1))
print("The sum of the numbers is ",S_n)

nth = a*r**(n-1)
print("The nth term is ",nth)
