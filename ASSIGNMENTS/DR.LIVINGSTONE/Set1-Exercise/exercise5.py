#print the value of the shoe size and adding this dictionary to your .py file
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

print("Shoe size is:", Shoes["size"])

#Assigning a new value
Shoes["brand"] = "Adidas"
print("Updated brand:", Shoes["brand"])

#adding a key/value pair "type”: "sneakers" to the dictionary
Shoes["type"] = "sneakers"
print("Updated dictionary:", Shoes)

#return a list of all the keys in the dictionary 
keys_list = list(Shoes.keys())
print("Keys:", keys_list)

#return a list of all the values in the dictionary
values_list = list(Shoes.values())
print("Values:", values_list)

#6.	Check if the key “size” exists 
if "size" in Shoes:
    print("Key 'size' exists.")
else:
    print("Key 'size' does not exist.")

#loop through the dictionary 
for key, value in Shoes.items():
    print(f"{key}: {value}")

#remove “color” from the dictionary.
Shoes.pop("color")
print("After removing color:", Shoes)

#empty the dictionary 
Shoes.clear()
print("Emptied dictionary:", Shoes)

#make a copy of  the dictionary 
student = {
    "name": "Alice",
    "age": 21,
    "course": "Public Administration"
}

student_copy = student.copy()
print("Original:", student)
print("Copy:", student_copy)

#nested dictionaries
family = {
    "child1": {
        "name": "Sam",
        "age": 10
    },
    "child2": {
        "name": "Lily",
        "age": 8
    }
}

print("Nested dictionary:", family)

