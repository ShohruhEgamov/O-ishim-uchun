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
in from the left, and let the rightmost bits fall off	x >> 2 '''

a = 20 % 3      # 20 ni 3ga  bo'lib bolib qolgan qoldiqni qaytaradi 
print(a)



