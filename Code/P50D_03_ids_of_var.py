#IDs of variables

x = 100
y = 200
z = 200

print(f"x value is {x} and id is {id(x)}")
print(f"y value is {y} and id is {id(y)}")
print(f"z value is {z} and id is {id(z)}")

print(id(x)==id(y))
print(id(z)==id(y))
