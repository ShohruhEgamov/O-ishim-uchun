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

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)