

a = 300
b = 300

print(id(a))
print(id(b))

c = a is b
d = a
print(c)
print(a == b)
print(d == a)

a = [5, 4, 3, 2, 1]
b = [1, 2, 3, 4, 5]

b = a

print(a)

a.sort()

print(b)

b = [6, 7, 8, 9, 10]

print(a, b)

print(id(a))
print(id(b))

str(input())
