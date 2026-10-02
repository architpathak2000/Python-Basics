<!-- 
architpathak@Archits-MacBook-Air Python % python3
Python 3.13.2 (v3.13.2:4f8bb3947cf, Feb  4 2025, 11:51:10) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> a = myListOne = [1,2,3]
>>> myListTwo = myListOne
>>> myListTwo
[1, 2, 3]
>>> a
[1, 2, 3]
>>> a="chai"
>>> a
'chai'
>>> myListOne
[1, 2, 3]
>>> myListOne[0] = 33
>>> myListTwo
[33, 2, 3]
>>> 
>>> m = [1,2,3]
>>> n=m
>>> m
[1, 2, 3]
>>> n
[1, 2, 3]
>>> m is n
True
>>> n= [1,2,3]
>>> m == n
True
>>> m is n
False
>>> 
 -->

 >>> teaVarieties = ["Black","Green","Oolong","White"]
>>> print(teaVarieties)
['Black', 'Green', 'Oolong', 'White']

<!-- >>> teaVarieties[1:2] = "Lemon"
>>> teaVarieties
['Black', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'White']
>>> Here String is treated as array -->

>>> teaVarieties = ["Black","Green","Oolong","White"]
>>> teaVarieties[1:2] = ["Lemon"]
>>> teaVarieties
['Black', 'Lemon', 'Oolong', 'White']
>>> 

>>> teaVarieties[1:1] = ["test","test","test"]
>>> teaVarieties
['Black', 'test', 'test', 'test', 'Lemon', 'Oolong', 'White']


>>> for tea in teaVarieties:
...     print(tea, end="-")
...     
Black-test-test-test-Lemon-Oolong-White->>> 

>>> if "Oolong" in teaVarieties:
...     print("Yes")
...     
Yes

>>> teaVarieties = ["Black","Green","Oolong","White"]
>>> teaVarieties.append("Masala")
>>> teaVarieties
['Black', 'Green', 'Oolong', 'White', 'Masala']
>>> 

>>> teaVarieties = ["Black","Green","Oolong","White"]
>>> teaVarieties.append("Masala")
>>> teaVarieties
['Black', 'Green', 'Oolong', 'White', 'Masala']
>>> teaVarieties.pop()
'Masala'
>>> teaVarieties
['Black', 'Green', 'Oolong', 'White']
>>> teaVarieties.remove("Green")
>>> teaVarieties
['Black', 'Oolong', 'White']
>>> 
>>> teaVarieties.insert(1,"Green")
>>> teaVarieties
['Black', 'Green', 'Oolong', 'White']
>>> teaVarieties_copy = teaVarieties.copy() // This will make new referrence in the memory
>>> 
>>> teaVarieties_copy
['Black', 'Green', 'Oolong', 'White']
>>> teaVarieties_copy.append("Lemon")
>>> teaVarieties_copy
['Black', 'Green', 'Oolong', 'White', 'Lemon']
>>> squareNum = [ x**2 for x in range(10)]
>>> squareNum
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> 
>>> cubeNum = [ x**3 for x in range(5)]
>>> cubeNum
[0, 1, 8, 27, 64]
>>> 

