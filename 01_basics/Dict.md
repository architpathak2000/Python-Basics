# Dictionary
>>> chai_types = { "Masala":"Spicy","Ginger":"Zesty","Green":"Mild"  }
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
>>> chai_types["Masala"]
'Spicy'
>>> chai_types.get("Ginger")
'Zesty'
>>> chai_types.get("Gingery")
>>> chai_types["Masalaa"]
Traceback (most recent call last):
  File "<python-input-11>", line 1, in <module>
    chai_types["Masalaa"]
    ~~~~~~~~~~^^^^^^^^^^^
KeyError: 'Masalaa'
>>> 
>>> for chai in chai_types:
...     print( chai , chai_types[chai])
...     
Masala Spicy
Ginger Zesty
Green Mild
>>> 

>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
>>> chai_types["Earl Grey"] = "Citrus"
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild', 'Earl Grey': 'Citrus'}
>>> 

>>> chai_types.pop("Green")
'Mild'
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Earl Grey': 'Citrus'}
>>> chai_types.popitem()
('Earl Grey', 'Citrus')
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty'}
>>> 
when we define dict under dict we have to give a key and define value as another dictionary.

>>> tea_shop = {
... "chai" : {"Masala":"Spicy" , "Ginger":"Zesty"},
... "tea" : {"Green":"Mild","Black":"Strong"}}
>>> 
>>> tea_shop["chai"]
{'Masala': 'Spicy', 'Ginger': 'Zesty'}
>>> tea_shop["chai"]["Ginger"]
'Zesty'
>>> 
>>> squared_num = { x:x**2 for x in range(6)}
>>> squared_num
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
>>> squared_num.clear()
>>> squared_num
{}
>>> 
>>> keys = ["Masala","Ginger","Lemon"]
>>> default_value = "Delicious"
>>> new_dict = dict.fromkeys(keys,default_value)
>>> new_dict
{'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}
>>> 

# Tuples

Tuples are immutable

>>> tea_types = ("Black","Green","Oolong")
>>> tea_types[1]
'Green'
>>> tea_types[1]= "Lemon"
Traceback (most recent call last):
  File "<python-input-39>", line 1, in <module>
    tea_types[1]= "Lemon"
    ~~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
>>> 
We cannot mutate the orginal tea_types

>>> tea_types = ("Black","Green","Oolong")
>>> (B,G,O)=tea_types
>>> b
>>> B
'Black'
>>> type(B)
<class 'str'>











