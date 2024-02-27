# program to show salary increment
# Waweru Lesley
# 26/02/2024

salary = int(input("Enter salary :"))

if salary < 100000 :
    bonus = salary * 0.3
    total_salary = salary + bonus
    print (total_salary)

elif salary >100000 and salary <150000 :
     bonus = salary * 0.15
     total_salary = salary + bonus
     print (total_salary)

else:
     if salary >150000 :
        bonus = salary * 0.3
        total_salary = salary + bonus
        print (total_salary)
