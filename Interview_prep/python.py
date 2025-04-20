import sys

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

