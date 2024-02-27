#  if_else program
# date : 26/02/2024
# name : Lesley Waweru

age = 25
if age > 18 : 
    print("You are allowed to drive")

print("\n")

salary = 45000
if salary > 30000 and salary < 50000 :
    new_salary = salary * 0.1 + salary
    print(new_salary)

print("\n")

home_county = "Nyeri"

if home_county ==  "Nyeri" or home_county == "Kisii" :
    print("You get a bursary")

print("\n")

grade = 90

if grade >= 84 and grade <= 90 :
    print("You win  calculator")
elif grade >=50 and grade <= 83 :
    print("You win a mathematical set")
else :
    print("You get nothing !")
