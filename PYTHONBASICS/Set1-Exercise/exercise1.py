#a list with 5 items (names of people) and write a python program to output the 2nd item.
people = ["Alice", "Bob", "Charlie", "David", "Eva"]
print("Second item:", people[1])

#changing the value of the first item Alice to a new value Alex
people[0] = "Alex"
print("Updated list:", people)

#adding a sixth item to the list
people.append("Frank")
print("List with sixth item:", people)

#adding “Bathel” as the 3rd item in your list
people.insert(2, "Bathel") 
print("List after inserting Bathel:", people)

#removing the 4th item from the list
people.pop(3) 
print("List after removing 4th item:", people)

#Using negative indexing to print the last item in the list
print("Last item:", people[-1])

#new list with 7 items and use a range of indexes to print the 3rd, 4th and 5th items
new_list = ["One", "Two", "Three", "Four", "Five", "Six", "Seven"]
print("3rd to 5th items:", new_list[2:5])

#list of countries and a copy 
countries = ["Uganda", "Kenya", "Tanzania", "Rwanda"]
countries_copy = countries.copy()
print("Original:", countries)
print("Copy:", countries_copy)

#loop through the list of countries
for country in countries:
    print("Country:", country)

#a list of animal names in descending and ascending order.
animals = ["Zebra", "Elephant", "Giraffe", "Antelope", "Lion"]
animals.sort()
print("Ascending order:", animals)

animals.sort(reverse=True)
print("Descending order:", animals)

#only animal names with the letter ‘a’ in them
for animal in animals:
    if 'a' in animal.lower():
        print("Animal with 'a':", animal)

#two lists, one containing your first names and the other your second names
first_names = ["John", "Jane", "James"]
second_names = ["Doe", "Smith", "Brown"]
full_names = first_names + second_names
print("Combined list:", full_names)

