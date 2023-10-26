# Byte object
x = b"23"
y = x.decode()
z1 = y.encode("utf-8")
z2 = y.encode("ascii")


print(x)
print(type(x))

print(y)
print(type(y))

print(z1)
print(type(z1))

print(z2)
print(type(z2))
