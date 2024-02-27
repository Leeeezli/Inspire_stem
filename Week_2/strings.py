# strings in python
# date : 22/02/2024
# name : Lesley Waweru

city = "nairobi"

print(city[0]) # n
print(city[1]) # a
print(city[2]) # i
print(city[3]) # r
print(city[4]) # o
print(city[5]) # b
print(city[6]) # i

# converts to uppercase

print(city)
print("\n") # prints to a new line
print(city.upper())

print("\n")

# converts to lower case
name = "LESLEY"
print(name)
print("\n")
print(name.lower()) 

print("\n")

town = "    Naivasha   "
print(town)
print("\t") # prints new tab
print(town.strip())
print("\n")
# add two strings

f_name = "Lesley"
s_name = "Waweru"

full_name = f_name  +  s_name

print(full_name )

print("\n")

# replacing a character

fruit = "orangeoooo"

print(fruit.replace("o","Y"))

print("\n")
subject = "Pysical,Sciences"

print(subject.split(":"))

print("\n")

age = 18
height = 1.2
print("I am {0} years old and {1} meters tall " .format(age,height))

print("\n")

# printing a string - %s
activity = "dancing"
print("My hobby is %s" %(activity))

print("\n ")

# printing a floating point - %f
height = 1.23
print("My height is %5.3f" %(height))

print("\n")

 # printing an integer - %d
age = 32
print("My age is %d" %(age))

print("\n")

# printing a character - %c

# len name = length of the name
name = "Waweru Lesley"
print(len(name))

print("\n")

print(f"My full name is {name}")

print("\n")

school = "Engineering"
course = "Electrical"

print("I am studying {course} in the school of {school}".format(course = "Medicine",school = "Human Sciences"))
