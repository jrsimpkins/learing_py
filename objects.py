print("objects:")

name = "Matt"

first = name

print(id("name"))

print(id("first"))

print("types:")

print(type("name"))

print(str(0))

print(tuple([1, 2]))

print(list('abc'))

print("Mutability:")

age = 10

print(id('age'))

age = age + 1

print(age)

print(id(age))

zero_chars = ''

print(zero_chars)

names = []

print(id('names'))

names.append("Fred")

print(id('names'))
