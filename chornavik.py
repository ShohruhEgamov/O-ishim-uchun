'''fruits = ("apple", "banana", "cherry")
yangi = []
meva = list(fruits)
for x in meva:
	if "a" in x:
		yangi.append(x)
b = tuple(yangi)
print(b)'''



'''a = ["apple", "banana", "cherry","nok","anjir","olma", "olcha"]
i = 0
while i < len(a):
	i = i + 1
	if i == 3:
		continue
	print(a[i - 1])'''

'''def funksiya(*kids):
  a = int(input("son kirit "))
  print("Bu odamni ismi " + kids[a])
funksiya("Shohruh", "Farrux", "Diyorbek")'''

'''def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)'''

'''x = lambda a : a + 10
print(x(5))'''

'''x = lambda a,b : a*b
print(x(5, 6))'''

'''x = lambda son, sifat: son+sifat
print(x(6, 8))'''

'''def funk(n):
  return lambda a: a*n
son = funk(2)

print(son(11))'''


'''the_world_is_flat = True
if the_world_is_flat:
    print("Be careful not to fall off!")'''

'''class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)
    print("I am " + str(self.age))
x = input("What is you name ")
z = input("Hov old are you ")
p1 = Person(x, z)
p1.myfunc()'''



