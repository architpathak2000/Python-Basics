
# Object Types / Data Types
- Number : 1234, 3.14, 3+4j, 0b111, Decimal(),Fraction()
- String: 'spam', "BOB", b'a\x01c'
- List: [1,[2,'three'], 4.5], list(range(10))
- Tuple: (1, 'spam', 4, 'U'), tuple('spam'), namedtuple
- Dictionary: {'food': 'spam', 'taste':yum }, dict(hours=10)
- Set: set('abc'), {'a', 'b', 'c'}
- File: open('eggs.txt'), open(r'C:\ham.bin, 'wb')
- Boolean: True, False
- None: None
- Functions, modules, classes
- Advanced: Decorators, Generators, Iterators, MetaProgramming


<!-- hnb  -->
<!-- 
architpathak@Archits-MacBook-Air Python % ls
01_basics
architpathak@Archits-MacBook-Air Python % python3
Python 3.13.2 (v3.13.2:4f8bb3947cf, Feb  4 2025, 11:51:10) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> username = "Archit"
>>> username
'Archit'
>>> 2.5*6
15.0
>>> 2 ** 6
64
>>> 2 ** 1000
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
>>> import math
>>> math.pi
3.141592653589793
>>> import random
>>> random.random()
0.7913546719605683
>>> random.choice([1,2,3,4,5])
5
>>> random.choice([1,2,3,4,5])
1
>>> username = "Chaiaurcode" 
>>> len(username)
11
>>> username[0]
'C'
>>> username[0] = 'A'
Traceback (most recent call last):
  File "<python-input-14>", line 1, in <module>
    username[0] = 'A'
    ~~~~~~~~^^^
TypeError: 'str' object does not support item assignment
>>> username[-2]
'd'
>>> username[1:3]
'ha'
>>> dir(username)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> mylist = [123, 'Chai', 3.14]
>>> mylist
[123, 'Chai', 3.14]
>>> len(mylist)
3
>>> myD = {'one':'lemon', 'two':'ginger', 'naag':'Parseltongue'}
>>> myD
{'one': 'lemon', 'two': 'ginger', 'naag': 'Parseltongue'}
>>> myD['naag']
'Parseltongue'
>>> myD['key']
Traceback (most recent call last):
  File "<python-input-24>", line 1, in <module>
    myD['key']
    ~~~^^^^^^^
KeyError: 'key'
>>> myTup = (1,2,4)
>>> myTup =[0]
>>> mytup[0]
Traceback (most recent call last):
  File "<python-input-27>", line 1, in <module>
    mytup[0]
    ^^^^^
NameError: name 'mytup' is not defined. Did you mean: 'myTup'?
>>> myTup[0]
0
>>> myTup = (1,2,4)
>>> myTup[1]
2
>>> 
 -->

 # Complex Numbers
  >> 2+1j
(2+1j)
>>> (2+1j)*3
(6+3j)
>>> 

# Octal, Hexadecimal,Binary
oct(64) int('64',8)
hex(64) int('64',16)
bin(64) int('64',2)

# Bitwise
x << 2

# Random
>>> import random
>>> random.random()
0.8890529257148854
>>> random.randint(1,10)
3
>>> random.randint(1,10)
4
>>> l1 = [1,2,3,4]
>>> random.choice(l1)
3
>>> random.choice(l1)
4
>>> random.shuffle(l1)
>>> l1
[2, 4, 1, 3]
>>> 

# Decimal and Fractions

 >>> from decimal import Decimal
>>> Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3')
Decimal('0.0')

>>> from fractions import Fraction
>>> myFrac = Fraction(2,7)
>>> myFrac
Fraction(2, 7)
>>> 

# Set

>>> setone = {1,2,3,4}
>>> setone & {1,3}
{1, 3}
>>> setone | {1,3,7}
{1, 2, 3, 4, 7}
>>> setone- {1,2,3,4}
set()
>>> type({})
<class 'dict'>
>>> 

<!-- 
>>> True + 1
2 
-->

# Strings
<!-- 
>>> chai = "Lemon Tea"
>>> first_char = chai[0]
>>> print(first_char)
L
>>> slice_chai = chai[0:6]
>>> print(slice_chai)
Lemon 
>>> num_list = "0123456789"
>>> num_list[:]
'0123456789'
>>> num_list[3:]
'3456789'
>>> num_list[:7]
'0123456'
>>> num_list[0:7:2]
'0246'
>>> num_list[0:8:3]
'036'
>>> chai = "   Masala Tea    "
>>> chai.strip()
'Masala Tea'
>>> chai.replace("Masala" , "Ginger")
'   Ginger Tea    '
>>> chai = "Lemon, Ginger, Masala, Mint"
>>> chai
'Lemon, Ginger, Masala, Mint'
>>> chai.split()
['Lemon,', 'Ginger,', 'Masala,', 'Mint']
>>> chai.split(", ")
['Lemon', 'Ginger', 'Masala', 'Mint']
>>> 
>>> chai = "Masala Chai"
>>> chai.find("Chai")
7
>>> chai = "Masala tea tea tea"
>>> chai.count("tea")
3
>>> chai_type = "Masala"
>>> quantity = "2"
>>> order = "I ordered {} cups of {} tea"
>>> order.format(quantity,chai_type)
'I ordered 2 cups of Masala tea'
 -->
# Covert List to String
>>> chai = "Masala Chai"
>>> chai.find("Chai")
7
>>> chai = "Masala tea tea tea"
>>> chai.count("tea")
3
>>> chai_type = "Masala"
>>> quantity = "2"
>>> order = "I ordered {} cups of {} tea"
>>> order.format(quantity,chai_type)
'I ordered 2 cups of Masala tea'

<!-- 
>>> chai = "He said, "Masala chai is awesome" "
  File "<python-input-40>", line 1
    chai = "He said, "Masala chai is awesome" "
                      ^^^^^^
SyntaxError: invalid syntax
>>> chai = "He said, \"Masala chai is awesome" "
  File "<python-input-41>", line 1
    chai = "He said, \"Masala chai is awesome" "
                                               ^
SyntaxError: unterminated string literal (detected at line 1)
>>> chai = "He said, \"Masala chai is awesome\" "
>>> chai
'He said, "Masala chai is awesome" '
>>> 

>>> chai = "Masala\nchai"
>>> chai
'Masala\nchai'
>>> print(chai)
Masala
chai
>>> chai = r"Masala\nchai"
>>> print(chai)
Masala\nchai
>>> 

>>> chai = "Masala chai"
>>> print("Masala" in chai)
True
>>> 

 -->