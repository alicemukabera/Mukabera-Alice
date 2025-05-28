#set() constructor to create a set of 3 of your favorite beverages.
beverages = set(["Coffee", "Tea", "Juice"])
print("Beverages set:", beverages)

#add 2 more items to the beverages set.
beverages.update(["Water", "Smoothie"])
print("Updated beverages set:", beverages)

#Check if microwave is present in the set.
mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("Microwave is present in the set.")
else:
    print("Microwave is not in the set.")

#to remove “kettle” from the set above.
mySet.remove("kettle")
print("Set after removing kettle:", mySet)

#loop
for item in mySet:
    print("Item:", item)

#a set of 4 items and a list of two items.  
#adds elements in the list to elements in the set.
mySet = {"Fan", "Fridge", "Toaster", "Blender"}
myList = ["Oven", "Cooker"]

mySet.update(myList)
print("Combined set:", mySet)

#two sets, one containing your ages and the other your first names. Join the two sets.
ages = {18, 21, 25}
first_names = {"Alice", "Bob", "Charlie"}

combined_set = ages.union(first_names)
print("Joined set:", combined_set)


