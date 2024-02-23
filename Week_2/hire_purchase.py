# program to calculate hire purchase
# name : Lesley waweru
# date : 21/02/2024

d = int(input("Enter deposit : "))
t = int(input("Enter time taken in months : "))
mi = int(input("Enter each installment : "))

hpp = (d + (t * mi))
print("The hire purchase price is ",hpp)
