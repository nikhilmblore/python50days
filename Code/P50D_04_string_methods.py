# String methods
# --------------------------------------------
# strip()
# replace()
# Split()
# format()
# --------------------------------------------

# strip()
tempString = "   this is strip method     "
print(tempString.strip())
print(tempString) 

# replace()
tempString = "This is replace method"
print(tempString.replace("me","aa"))
print(tempString)

# split()
tempString = "This is split method"
print(tempString.split())
print(tempString.split("i"))
print(tempString)

# format
tempString = "My name is {} {}"
print(tempString.format("nikhil", "raju"))
print(tempString) #prints unformatted string

# find()
tempString = "Bangalore"
print(tempString.find("a"))

# isdigit(), #isalpha()
tempString = "Bangalore"
tempString2 = "23424"
tempString3 = "abc123"
print(tempString.isalpha())

print(tempString2.isdigit())
print(tempString3.isdigit())

# isdigit vs isnumeric
print(tempString2.isnumeric())
print(tempString3.isnumeric())



