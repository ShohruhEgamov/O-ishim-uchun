import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#arr = np.array([1,2,3,5,6])

#print(np.__version__)

#arr = np.array([1, 2, 3, 4, 5])

#print(arr)

#print(type(arr))

#arr = np.array(42)

#print(arr)


#arr = np.array([[1,2,3],[4,5,6]])
#print(arr)

#a = np.array(42)
#b = np.array([1, 2, 3, 4, 5])
#c = np.array([[1, 2, 3], [4, 5, 6]])
#d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

#print(a.ndim)
#print(b.ndim)
#print(c.ndim)
#print(d.ndim)

#arr = np.array([1,2,3], ndmin=6)
#print(arr)
#print("bu sonni nechtaligi: ", arr.ndim) 

#arr = np.array([1,2,3,4])

#print(arr[1] + arr[3])


#arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

#print('2nd element on 1st row: ', arr[0, 1])

#arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

#print(arr[1, 0, 2])

#import random

#a = random.randint(1, 10)
#b = random.randint(1, 10)
#c = int(input(f"{a} * {b} = "))
#s = a * b
#if c ==s:
#	print("bu togri")
#else:
#	print("bu notogri")

#a = np.array([1,2,3,4,5,6,7])

#print(a[1:5:2])

#a = np.array([[1,2,3,4],[5,6,7,8]])

#print(a[1, 0:3:2])

#a = np.array([1,2,3,4])

#print(a.dtype)


#arr = np.array(['apple', 'banana', 'cherry'])

#print(arr.dtype)

#a = np.array([1,2,3,4], dtype="4")

#print(a)
#print(a.dtype)

#a = np.array([1.1, 2.1, 3.1])

#newarr = a.astype('f')

#print(newarr)
#print(newarr.dtype)

#arr = np.array([1, 2, 3])

#newarr = arr.astype(bool)

#print(newarr)
#print(newarr.dtype)

#a = nu.array([1,2,3,4,5])
#x = a.copy()
#x = a.view()
#a[0] = 5

#print(a)
#print(x)



#arr = np.array([1, 2, 3, 4])

#print(arr.dtype)


#a = np.array([1,2,3,4,5])
#x = a.view()
#a [0] = 31
#print(a)
#print(x)


#a = np.array([1, 2, 3, 4, 5])

#x = a.copy()
#y = a.view()

#print(x.base)
#print(y.base)


#arr = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[1, 2, 3, 4], [5, 6, 7, 8]])

#print(arr.shape)

#3arr = np.array([1, 2, 3, 4], ndmin=10)

#print(arr)
#print('o\'lchamlar soni:', arr.shape)

#a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
#nex = a.reshape(6,2)
#a = nex.copy()
#print(nex)
#print(nex.dtype)
#print(a)

#arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

#newarr = arr.reshape(3, 4, 1)

#print(newarr)

#a = np.array([1,2,3,4,5,6,7,8])
#a[0] = 1
#a.reshape(2,4)
#print(a.reshape(2,4).base)

#a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
#new = a.reshape(-1)
#print(new)

#a = np.array([[[1,2,3],[4,5,6]],[[6,7,8],[10,11,12]]])

#for x in a: # 1-D skanerlash
#	for y in x:  # 2-D skanerlash aylantiris
#		for c in y:  # 3-D skanerlash aylantiris
#			print(c)


#arr = np.array(([[[1,2],[3,4]], [[5,6],[7,8]]]))

#for x in np.nditer(arr):
#	print(x)

#arr = np.array([1,2,3])

#for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
#	print(x)

#arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

#for x in np.nditer(arr[:, ::3]):
#	print(x)

#arr = np.array([1,2,3])
#for idx, x in np.ndenumerate(arr):
#	print(idx, x) 

#arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

#for idx, x in np.ndenumerate(arr):
#  print(idx, x)

#arr1 = np.array([1,2,3])

#arr2 = np.array([4,5,6])

#arr = np.concatenate((arr1,arr2))

#print(arr)

#arr1 = np.array([[1, 2], [3, 4]])

#arr2 = np.array([[5, 6], [7, 8]])

#arr = np.concatenate((arr1, arr2), axis=1)

#print(arr)


#arr1 = np.array([[1, 2, 3], [5,8,3]])

#arr2 = np.array([[4, 5, 6], [8,9,3]])

#arr = np.vstack((arr1,arr2))   # stack    hstack    vstack    dstack
#for idx, x in np.ndenumerate(arr):
#  print(idx, x)


#A = np.arange(10, 15)



#print(A)

#arr = np.array([1,2,3,4,5,6,7])

#x = np.where(arr ==4)   # faqat 4 ni qayerda ekanini aytadi
#x = np.where(arr%2 == 0)  # 0 juftni 1 toqni qidiradi
#x = np.searchsorted(arr, 7)
#x = np.searchsorted(arr, [2,4,6])  # qaysi massivlarga qoyishni bildiradi
#print(x)


# arr = np.array([3,2,0,1])
#arr = np.array(['banan', 'cheriy','apple'])
#arr = np.array([True, False, True])
#arr = np.array([[3,2,5],[5,8,9]])

#for idx, x in np.ndenumerate(arr):
#  print(idx, x)
#print(np.sort(arr)).

#arr = np.array([1,2,3])
#print(np.cumsum(arr))


#arr = np.array([41,52,43,44])
#x = arr[[False,False,False,True]]
#print(x)

#a = np.array([41,42,43,44])
#sodda = []
#for element in a:
#	if element <43:
#		sodda.append(True)
#	else:
#		sodda.append(False)
#newarr = a[sodda]

#print(sodda)
#print(newarr)



#a = np.array([1,2,3,4,5,6,7])
#sodda = []

#for son in a:
#	if son % 2 == 0:
#		sodda.append(True)
#	else:
#		sodda.append(False)
#yangi = a[sodda]
#x = a[sodda]

#print(x)
#print(sodda)
#print(a)

#a = np.array([41,42,43,44])
#son = a > 42
#yangi = a[son]
#print(son)
#print(yangi)

#a = np.array([1,2,3,4,5,6,7])
#son = a % 2 == 0
#yangi = a[son]

#print(son)
#print(yangi)

#x = random.rand()  # Tasodifiy float raqam

#print(x)

#x = random.randint(100, size=(5,3))
#x = random.rand(5,5)
#x = random.choice([3,5,7,9], size=(3,7))
#print(x)

#x = random.choice([3,5,7,9], p=[0.3, 0.1, 0.5, 0.1], size=(5))
#print(x)

#a = np.array([1,2,3,4,5])
#random.shuffle(a)
#print(a)

#a = np.array([1,2,3,4,5])
#print(random.permutation(a))

#arr = ([0,1,2,3,4,5,6,7])
#sns.distplot(x, hist=False)
#plt.show()

#x = random.normal(size=(2,3))
#print(x)

#x = random.normal(loc=1, scale=3, size=(2,2))
#sns.distplot(x, hist=False)
#plt.show()
#print(x)

#sns.distplot(random.normal(size=1000), hist=False)
#plt.show()


#x = random.binomial(n=10, p=0.1, size=5)
#print(x)

#sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)
#plt.show()

#sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
#sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')
#plt.show()

#x = random.poisson(lam=2, size=10)
#print(x)
#sns.distplot(random.normal(loc=60, scale=8, size=1000), 
#             hist=False, label="normal")
#sns.distplot(random.poisson(lam=40,size=1000),
#              hist=False, label='poission')
#plt.show()


#sns.distplot(random.binomial(n=1000, p=0.01, size=1000), hist=False, label="binomial")
#sns.distplot(random.poisson(lam=10, size=1000), hist=False, label='poisson')
#plt.show()

#x = random.uniform(size=(2,3))
#print(x)

sns.distplot(random.uniform(size=1000), hist=True)
plt.show()