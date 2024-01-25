#This is a comment
print("Hello, World!")

print("Hello, World!") #This is a comment

"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")


#Python O`zgaruvchilar
x = 5
y = "John"
print(x)
print(y)

#Agar siz o'zgaruvchining ma'lumotlar turini belgilamoqchi
#bo'lsangiz, bu casting yordamida amalga oshirilishi mumkin.

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#Funktsiya yordamida o'zgaruvchining ma'lumotlar turini olishingiz mumkin type()

x = 5
y = "John"
print(type(x))
print(type(y))

#Python - o'zgaruvchilar nomlari

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Noqonuniy o'zgaruvchilar nomlari:

''' 2myvar = "John"
	my-var = "John"
	my var = "John"  '''

#Python o'zgaruvchilari - bir nechta qiymatlarni belgilash

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Python - Chiqish o'zgaruvchilari

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#Python - Global o'zgaruvchilar

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

x = "awesome"


#Agar funksiya ichida bir xil nomli o‘zgaruvchi yaratsangiz, 
#bu o‘zgaruvchi mahalliy bo‘ladi va faqat funksiya ichida ishlatilishi mumkin.
# Xuddi shu nomdagi global o'zgaruvchi avvalgidek,
# global va asl qiymati bilan qoladi.

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#Global kalit so'z

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#Python ma'lumotlar turlari

x = str("Hello World")
x = int(20)
x = float(20.5)
x = complex(1j)
x = list(("apple", "banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = range(6)
x = dict(name="John", age=36)
x = set(("apple", "banana", "cherry"))
x = frozenset(("apple", "banana", "cherry"))
x = bool(5)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))