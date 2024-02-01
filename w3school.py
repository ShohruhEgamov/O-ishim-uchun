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

#Python satrlari

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#String orqali aylanish

for x in "banana":
  print(x)

#Satrda ma'lum bir ibora yoki belgi mavjudligini tekshirish
# uchun biz kalit so'zdan foydalanishimiz mumkin in.

txt = "salom shohruh qalaysan"
print("shohruh" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#Yo`qligini tekshiring
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#Python - satrlarni o'zgartirish

a = "Hello, World!"
print(a.upper())

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#Python - Format - Strings

age = 36
txt = f"My name is John, and I am {age}"
print(txt)

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


#Python mantiqiy

a = 200
b = 33

if b > a:
  print("b katta a dan")
else:
  print("b kichik a dan")


# bool har qanday malumotlarni baholaydi
  
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

#bular false qiymatini qaytaradi

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# len qaytaruvchisidan qaytarilgan qiymat 0 bo`lsada false qaytaradi
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# mantiqiy qiymat qaytaradigan 
 
def myFunction():
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

# isinstance() Python shuningdek , ob'ektning ma'lum bir
#ma'lumot turiga tegishli ekanligini aniqlash uchun ishlatilishi mumkin bo'lgan funktsiya 
#kabi mantiqiy qiymatni qaytaradigan ko'plab o'rnatilgan funktsiyalarga ega :

x = 200
print(isinstance(x, int))


#Python operatorlari

'''Python operatorlarni quyidagi guruhlarga ajratadi:

Arifmetik operatorlar
Belgilash operatorlari
Taqqoslash operatorlari
Mantiqiy operatorlar
Identifikatsiya operatorlari
A'zolik operatorlari
Bitli operatorlar'''

'''()	Parentheses	
**	Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	Addition and subtraction	
<<  >>	Bitwise left and right shifts	
&	Bitwise AND	
^	Bitwise XOR	
|	Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	Logical NOT	
and	AND	
or	OR'''

#Python Bitwise operatorlari

'''& 	AND	Sets each bit to 1 if both bits are 1	x & y	
|	OR	Sets each bit to 1 if one of two bits is 1	x | y	
^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
~	NOT	Inverts all the bits	~x	
<<	Zero fill left shift	Shift left by pushing zeros in from the right 
and let the leftmost bits fall off	x << 2	
>>	Signed right shift	Shift right by pushing copies of the leftmost bit 
<<<<<<< HEAD
in from the left, and let the rightmost bits fall off	x >> 2 '''



a = 20 % 3      # 20 ni 3ga  bo'lib bolib qolgan qoldiqni qaytaradi 
print(a)


#salom mening ismin Shohruh bugun sana 27.01.2024

# Python ro'yhatlar

thislist = ["apple", "banana", "cherry"]
#a = int(input("son kirit "))
#b = input("soz kirit ")
thislist[a] = b

print(thislist)


meva = ["apple", "banana", "cherry"]
meva.remove("banana")
print(meva)

# belgilangan indexni olib tashlash

meva = ["apple", "banana", "cherry"]
meva.pop(1)  # index korsatmasa oxirgi belgini olib tashlaydi
print(meva)

# kali del indexni olib tashlaydi. u royhatni ham ochirib yuboradi

meva = ["apple", "banana", "cherry"]
del meva[0]
print(meva)

# ro'yhatni tozalash

meva = ["apple", "banana", "cherry"]
meva.clear()
print(meva)

# loop dan foydalanish

meva = ["apple", "banana", "cherry"]
for i in range(len(meva)):
  print(meva[i])

# while siklidan foydalanish
  
meva = ["apple", "banana", "cherry"]
i = 0
while i < len(meva):
  print(meva[i])
  i = i + 1


# ro'yhatlarni tushunish

meva = ["apple", "banana", "cherry"]
yangi = []

for x in meva:
  if "a" in x:
    yangi.append(x)
print(yangi)

meva = [x for x in meva if x != "apple"] # olmadan boshqa hammasini chiqaradi

newlist = [x for x in range(10) if x < 5] # 5 dan kichiklarni chiqaradi

newlist = ['hello' for x in fruits] # hammasini helloga aylantirish

newlist = [x if x != "banana" else "orange" for x in fruits] # bananni apelsinga almashtirish

newlist = [x.upper() for x in fruits] # ifodani qiymatlarni katta harif bilan belgilash

meva = ["orange", "mango", "kiwi", "pineapple", "banana"]   # alfanumerik tartiblash
meva.sort() # (reverse = True) kamayish boyicha tartiblash
print(meva)

# raqamni ozingiz saralaysiz. 50 ga yaqin sonlardan

def myfunc(n):
  return abs(n - 50)

son = [100, 50, 65, 82, 23]
son.sort(key = myfunc) # sort katta hariflarni oldin korsatadi agar siz buni hohlamasangiz "key = str.lower"
print(son)             # .reverse() ro'yhatni teskari tartiblaydi

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()  # kopyalash "list(thislist)" bu ham kopyalashni bir yo'li
print(mylist)



list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)  #extend()Ro'yxat 1 ning oxiriga list2 qo'shish uchun usuldan foydalaning :
print(list1)

for x in list2:
  list1.append(x)  

list3 = list1 + list2



# Python kortejlari

#Tupleda "olma" mavjudligini tekshiring:

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# KARTEJGA QOSHISH
  
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# kartejga kartej qoshish

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)


# Element olib tashlash

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# hammasini o'chirish

thistuple = ("apple", "banana", "cherry")
#del thistuple # bu hatoni keltirib chiqaradi. chunki kartej endi yo'q
print(thistuple)


fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


# Python - Loop Tuples

fruits = ("apple", "banana", "cherry")
for x in fruits:
  print(x)


fruits = ("apple", "banana", "cherry")
for i in range(len(fruits)):
  print(fruits[i])


# while siklidan foydalanish

fruits = ("apple", "banana", "cherry")
i = 0
while i < len(fruits):
  print(fruits[i])
  i = i + 1

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)



#Python to'plamlari

#Quyidagi usul yordamida to'plamga element qo'shing add() 

set = {"apple", "banana", "cherry"}

set.add("orange")

print(set)

#Joriy to'plamga boshqa to'plamdan elementlar qo'shish uchun update() usuldan foydalaning.

set = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

set.update(tropical)

print(set)


# faqat toplam emas hamma narsa qoshiladi

set = {"apple", "banana", "cherry"}
mylist = ["pineapple", "mango", "papaya"]

set.update(mylist)
print(set)

#To'plamdagi elementni olib tashlash uchun , remove() yoki discard()usulidan foydalaning.

set = {"apple", "banana", "cherry"}
set.remove("banana") # ochiriladigan elemen bolmasa hato beradi
print(set)

set = {"apple", "banana", "cherry"}
set.discard("banana") # ochiriladigan element bolmasa hato bermaydi
print(set)

# usul pop() element belgilanmasa hohlagan elementni olib tashlaydi
set = {"apple", "banana", "cherry"}

x = set.pop()

print(x)
print(set)

#Usul clear() to'plamni bo'shatadi:
set = {"apple", "banana", "cherry"}
set.clear()
print(set)

#Kalit delso'z to'plamni butunlay o'chirib tashlaydi:
set = {"apple", "banana", "cherry"}
del set
print(set)

# Usul union()ikkala to'plamdagi barcha elementlar bilan yangi to'plamni qaytaradi:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# Usul intersection_update()faqat ikkala to'plamda mavjud bo'lgan narsalarni saqlaydi.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x)

#Usul faqat ikkala to'plamda mavjud bo'lgan narsalarni o'z ichiga olgan yangiintersection() to'plamni qaytaradi .

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection(y)
print(x)

# Usul symmetric_difference_update()faqat ikkala to'plamda mavjud bo'lmagan elementlarni saqlaydi.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)
print(x)



#Python Lugatlar

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#Lug'atning "brend" qiymatini chop eting:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#Lug'at elementlaridagi qiymatlar har qanday turdagi ma'lumotlarga ega bo'lishi mumkin:

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}


#Lug'at yaratish uchun dict() usulidan foydalanish:

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


#get()Sizga bir xil natija beradigan usul ham mavjud :

#Misol
#"Model" kalitining qiymatini oling:

#x = thisdict.get("model")

#Usul keys()lug'atdagi barcha kalitlarning ro'yxatini qaytaradi.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x)


#Yangi kiritish

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change


#Hamma royhatlarni oladi. 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.values()

print(x)

#Asl lug'atga o'zgartirish kiriting va qiymatlar ro'yxati ham yangilanishini ko'ring:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

#Asl lug'atga yangi element qo'shing va qiymatlar ro'yxati ham yangilanishini ko'ring:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change


#Usul items()lug'atdagi har bir elementni ro'yxatdagi kortejlar sifatida qaytaradi.

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

#Lug'atda belgilangan kalit mavjudligini aniqlash uchun inkalit so'zdan foydalaning:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


#Usul update()lug'atni berilgan argumentdagi elementlar bilan yangilaydi.Agar element mavjud bo'lmasa, element qo'shiladi.

#Argument lug'at yoki kalit: qiymat juftliklari bilan takrorlanadigan ob'ekt bo'lishi kerak.


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

#Usul pop()belgilangan kalit nomi bilan elementni olib tashlaydi:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#Usul popitem()oxirgi kiritilgan elementni olib tashlaydi (3.7 dan oldingi versiyalarda uning o'rniga tasodifiy element o'chiriladi):

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#Kalit delso'z belgilangan kalit nomi bilan elementni olib tashlaydi:

#Usul clear()lug'atni bo'shatadi:

#values()Lug'at qiymatlarini qaytarish uchun usuldan ham foydalanishingiz mumkin :

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)


#Usul clear()lug'atni bo'shatadi:

#Usul bilan lug'at nusxasini yarating copy():

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#Funktsiyaga ega lug'at nusxasini yarating dict() :

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#ichki lugat yaratish

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#Ichki lug'atdagi elementlarga kirish uchun siz tashqi lug'atdan boshlab lug'atlar nomidan foydalanasiz:

print(myfamily["child2"]["name"])

#3 ta tugma bilan lug'at yarating, ularning barchasi 0 qiymatiga ega:

x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)

#Usul fromkeys()belgilangan kalitlarga va belgilangan qiymatga ega lug'atni qaytaradi.

#Usul setdefault()belgilangan kalit bilan elementning qiymatini qaytaradi.

#Agar kalit mavjud bo'lmasa, kalitni belgilangan qiymat bilan kiriting, quyidagi misolga qarang

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "White")

print(x)


# Python shartlari va If iboralari

#Teng: a == b
#Teng emas: a != b
#Kichikroq: a < b
#Kichik yoki teng: a <= b
#Kattaroq: a > b
#dan katta yoki teng: a >= b

# Elif kalit so'zi Pythonning "agar oldingi shartlar to'g'ri bo'lmagan bo'lsa, bu shartni sinab ko'ring" deyish usulidir.

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#Ushbu misolda a b ga teng , shuning uchun birinchi shart to'g'ri emas, lekin elif sharti to'g'ri, shuning uchun biz "a va b teng" deb ekranga chop etamiz.
  
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# QISQA QOL
if a > b: print("a is greater than b")

# bu satirga kop buyruq joylashtiramiz

a = 340
b = 330
print(("A") if a > b else print("Teng") if a == b else("B"))

# Qaysi katta bo'lsa shuni chiqaradi

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Bu to'g'ri")

#Kalit or (yoki) so'z mantiqiy operator bo'lib, shartli gaplarni birlashtirish uchun ishlatiladi:

a = 200
b = 33
c = 500
if a > b or a > c:
  print("ikkalasindan biri katta")

# Kalit notso'z mantiqiy operator bo'lib, shartli gapning natijasini teskari o'zgartirish uchun ishlatiladi:

a = 33
b = 200
if not a > b:
  print("a katta emas b dan")

# Siz bayonotlar ifichida bayonotlarga ega bo'lishingiz mumkin, bu ichki iboralar ifdeb ataladi . if

x = 15

if x > 10:
  print("10 katta")
  if x > 20:
    print("20 x dan katta")
  else:
    print("20 kichik x")

# ifbayonotlar bo'sh bo'lishi mumkin emas, lekin agar sizda biron sababga ko'ra ifmazmunsiz bayonot bo'lsa, passxatolikka yo'l qo'ymaslik uchun bayonotni kiriting.

a = 33
b = 200

if b > a:
  pass

# Python while loops

# while tsikli bilan biz shart to'g'ri bo'lsa, bir qator bayonotlarni bajarishimiz mumkin.

i = 1
while i < 6:
  print(i)
  i += 1

# break iborasi yordamida biz while sharti to'g'ri bo'lsa ham tsiklni to'xtata olamiz:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# continue (Davom etish) iborasi bilan biz joriy iteratsiyani to'xtatib, keyingisini davom ettirishimiz mumkin:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue  # amal 3 ni tashlab otib ketadi
  print(i)

  # Looplar uchun Python

  a = ["apple", "banana", "cherry","nok","anjir","olma", "olcha"]
  for x in a:
   #print(x) # bu cherryni ham chiqaradi
    if x == "cherry":
      break
    print(x) # bu cherrydan oldingilarnichiqaradi

a = ["apple", "banana", "cherry","nok","anjir","olma", "olcha"]

for x in a:
  if x == "cherry":
    continue
  print(x)

#  range () funktsiyasi sukut bo'yicha 0 dan boshlanadigan raqamlar ketma-ketligini qaytaradi va 1 ga (sukut bo'yicha) ortadi va belgilangan raqamda tugaydi.
  
for x in range(6): # 0 dan 6 gacha
  print(x)

for x in range(1, 6): # qaysidan boshlashni bildiradi
  print(x)


for x in range(2,30,3):
  print(x)             # nechidan boshlab nechigacha nechi oshirishi bildiradi

for x in range(6):
  print(x)
else:
  print("Finally finished!")

a = ["red", "big", "tasty"]
b = ["apple", "banana", "cherry"]

for x in a:
  for y in b:
    print(x,y)
