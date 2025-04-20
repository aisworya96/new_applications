import sys, random

print(sys.version)

n = 6
fact = 1
for i in range (1, n+1):
    fact *= i
print(fact)

# unpack a collection

fruits = ["Apple", "orange", "banana"]
x, y, z = fruits
print(x)
print(y)
print(z)
# output multiple variable separated by a comma
print(x, y, z)

# global and local variable

x = "awesome"

def myfunc():
    global y
    y = "Dezy"
    x = "fantastic"
    y = "Aisworya"
    print("Python is " + x, y)

myfunc()

print("Python is " + x, y)

print(random.randrange(1, 10))

# slicing string
b = "Aisworya, Panda!"
print(b[1:5])
# negative indexing

b = "Aisworya, Panda!"
print(b[-5:-1])



