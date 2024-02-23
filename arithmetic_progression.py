# program  to show how to perform arithmetic progression
# date: 20/02/2024
# name : Lesley Waweru

a = int(input("Enter the first term : "))
n = int(input("Enter the number of terms :"))
d = int(input("Enter the common difference :"))

S_n = (n/2)*(2*(a)+(n-1)*d)
print("The sum of the numbers is ",S_n)

nth = a+(n-1)*d
print("The nth term is ",nth)
