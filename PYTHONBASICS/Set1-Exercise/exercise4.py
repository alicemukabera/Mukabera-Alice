#to concatenate the two variables.
age = 25
message = "My age is " + str(age)
print(message)

#removing spaces 
# to only remove leading and trailing spaces, use .strip() instead.
txt = "      Hello,       Uganda!       "
clean_txt = txt.replace(" ", "")
print("Without spaces:", clean_txt)

#converting to uppercase
txt = "      Hello,       Uganda!       "
print("Uppercase:", txt.upper())

#replace character ‘U’ with ‘V’ 
txt = "      Hello,       Uganda!       "
new_txt = txt.replace("U", "V")
print("After replacement:", new_txt)

#return a range of characters in specific positions
y = "I am proudly Ugandan"
print("2nd to 4th characters:", y[1:4])

#correct code of"x = “All “Data Scientists” are cool!” 
x = "All \"Data Scientists\" are cool!"
print(x)
#or
x = "All \"Data Scientists\" are cool!"
print(x)


