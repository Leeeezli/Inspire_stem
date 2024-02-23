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

# convert to uppercase

print(city)
print("\n") # prints to a new line
print(city.upper())


name = "LESLEY"
print(name)
print("\n")
print(name.lower()) # converts strings to lower case

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


# replacing a character

fruit = "orangeoooo"

print(fruit.replace("o","Y"))


subject = "Pysical,Sciences"

print(subject.split(":"))

age = 18
height = 1.2
print("I am {0} years old and {1} meters tall " .format(age,height))
