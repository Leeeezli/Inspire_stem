# block of code running together as a unit
# name : Lesley Waweru
# date : 29/02/2024

# user defined functions
# built in functions


# to define a function
def print_name():
    print("My name is Lesley Waweru")


# calling the function
print_name()

print("\n")

def print_details(Name , Age , Id , Gender):
    print("I am {0} , {1} , years old . My id number is {2} and my gender is {3}".format(Name , Age , Id , Gender))
    
print_details("Lesley", "18" , "11942919" , "Female")
print_details("Wes", "19" , "11942952" , "Male")

print("\n")

def sum_nums(x,y):
    return x + y

z = sum_nums(10,20)
print(z)

print("\n")

def prod_nums(x,y):
    return x * y

print(prod_nums(2,5))

print("\n")

def print_odds(first_number,last_number):
    for i in range(first_number,last_number,2):
        print(i)

print_odds(1,15)
