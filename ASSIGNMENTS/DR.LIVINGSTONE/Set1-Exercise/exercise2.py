#favorite phone brand.
x = ("samsung", "iphone", "tecno", "redmi")
print("My favorite phone brand is:",
x[0])  

#negative indexing to print the 2nd last item in your tuple. 
print("Second last item:", x[-2])

#update iphone to itel
x_list = list(x)
x_list[1] = "itel"
x = tuple(x_list)
print("Updated tuple:", x)

#add Huawei
x = x + ("Huawei",)
print("Tuple after adding Huawei:", x)

#loop through 
for phone in x:
    print("Phone brand:", phone)

#delete the first item 
x_list = list(x)
x_list.pop(0)
x = tuple(x_list)
print("Tuple after removing first item:", x)

#tuple() constructor, create a tuple of the cities in Uganda
cities = tuple(["Kampala", "Gulu", "Mbarara", "Jinja", "Arua"])
print("Ugandan cities tuple:", cities)

#unpack your tuple
city1, city2, city3, city4, city5 = cities
print(city1, city2, city3, city4, city5)

#range of indexes to print the 2nd, 3rd and 4th cities 
print("Selected cities:", cities[1:4])

#two tuples, one containing your first names and the other your second names. Join the two tuples.
first_names = ("John", "Jane", "James")
second_names = ("Doe", "Smith", "Brown")
full_names = first_names + second_names
print("Full names tuple:", full_names)


#tuple of colors and multiply it by 3.
colors = ("Red", "Green", "Blue")
colors_multiplied = colors * 3
print("Colors multiplied by 3:", colors_multiplied)

#number of times 8 appears 
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print("Number of times 8 appears:", thistuple.count(8))


