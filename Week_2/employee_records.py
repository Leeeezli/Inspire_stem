# program to show employee records
# name : Lesley Waweru
# date : 21/02/2024

name = input("Enter employee name : ")
age = input("Age : ")
salary = float(input("Salary : "))
bonus = float(input("Bonus : "))

inc = 130/100
new_salary = salary * inc
print("The new salary is ",new_salary)

dec = 5000
new_bonus = bonus - dec
print("The new bonus is ",new_bonus)
