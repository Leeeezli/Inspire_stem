# lists
# name : Lesley Waweru
# date : 27/02/2024


friends = ["Elias","Jane","Re","Knight","Dave"]

for friend in friends:
    print(friend)

print("\n")

# to copy one list into another
enemies = friends[:] 
print(enemies)

print("\n")

#slice the list ie get part of the list
fruits = ("Guava","Mango","Lime","Strawberry","Pinapple")

print(fruits[0:3])

print("\n")

squares = [] #initialises an empty list

for x in range(0,11):
    squares.append(x**2)
    print(squares)
