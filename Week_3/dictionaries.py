# dictionaries
# name : Lesley Waweru
# date : 28/02/2024

laptop = {"make":"hpp","color":"grey","weight":"1.2","year":"2022"}

print(laptop["make"])
print(laptop["color"])
print(laptop["year"])

print("\n")

laptop["color"] = "red"
laptop["year"] = "2023"
print(laptop)
 
print("\n")

laptop["size"] = "1200mm x 600mm"
print(laptop)


print("\n")

del laptop ["color"]
print(laptop)

print("\n")

siz_laptop = laptop.copy()
print(siz_laptop)

"""
for key,value in laptop.items():
    print("\n")
    print(key)
    print("\n")
    print(value)
"""
