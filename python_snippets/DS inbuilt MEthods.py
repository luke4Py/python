
# Inbuilt Methods(function) for data Structures:

import numpy as np
'Data Structures has Inbuilt methods'


x = {'luke':'hyd', 'devraj':'chennai', 'luke': 'telangana', 'Luke':'hyd'}
x['luke']

Ds = 'list, set ,tuple, dict'
    #  [] ,  {},  (),   {k:v}


# Indbuilt methods for list :

list1 = ['luke', 'Mohan', 'yasmin', 'pavitra']
print(list1)


# 1) Append
list1.append('chaitanya')  # adding elements at the end
list1.append('chaitanya')  # adding elements at the end
print(list1)
list1.append(222222222222200000000000000000.5555555)

# 2) pop
list1.pop()  # removing element from the end
print(list1)

list1.pop('index_position')
"""removing element with the help of index value/position"""

list1.pop(-1)
print(list1)

list1.pop(1)
print(list1)


#list1.remove('sahana')

# 3) Insert:
''' 
insert a value using index number
list1.append('saba')
print(list1)
'''

list1.insert('index position', 'value to be added')
list1.insert(1, 'vamshi')
list1.insert(0, 'venky')
list1.insert(1, 'Devraj')
print(list1)

# 4) extend
aList = [123, 'xyz', 'tommy', 'abc', 123]
bList = [2009, 'beneli']


print(aList)
print(bList)

aList.extend(bList)
print(aList)


bList.extend(aList)
print(bList)

# Append <-> Extend
AList = [123, 'xyz', 'tommy', 'abc', 123]
BList = [2009, 'beneli']
AList.append(BList)
print(AList)

# Reverse: to reverse the given list
aList = [123, 'xyz', 'tommy', 'abc', 124]
aList.reverse()
print(aList)
aList[4]

# Sort: sort the given list from ascending or descending
blist = [8, 99, 45, 33]
print(blist)
blist.sort()  # default ascending order
print(blist)
blist.sort(reverse=True)  # descending order

blist = ['a', 'c', 'd', 's', 'x', 'v', 'b']
blist.sort(reverse=True)
blist.sort()
print(blist)



# count: count the value in given list of elements
aList = [123, 'xyz', 'zara', 'abc', 123, "zara"]

print(aList.count(123))
print(aList.count('zara'))
print(aList.count('abc'))
print(aList.count('ab'))


# index #will give only the first occurances index value.
students = ['x','y','a','b','c','c','lalitha']
print(aList.index('zara'))
print(students.index('lalitha'))
print(students.index('c'))
students.pop(6)

count= 1
# for idx, each_value in enumerate(aList):
#     print(idx, each_value)
#     # if each_value == 'zara':
    #     # print(f"Position of {count} Zara : {idx}")
    #     count+=1


# remove
aList = [123, 'xyz', 'zara', 'abc', 123, "zara", 'lalitha']
print(aList)

aList[7]


aList.pop(5)

aList.remove('zara')
aList.remove('lalitha')
aList.remove(123)

# clear
aList = [123, 'xyz', 'zara', 'abc', 123, "zara"]
aList.clear()
print(aList)


#deleting multiple occurance -> Assignment.

    




#list comprehension
[each_element for each_element in aList if aList.count(each_element)<2]

print(aList)
"""
append()
pop()
insert()
extend()
sort()
reverse()
count()
index()
remove()
clear()
"""

# Inbuilt Methods for Tuple.

tup = (1, 2, 3, 4, 5, 6, 5)
tup[7]
set(tup)
list(tup)

"""
count()
index()
"""
tup.count(5)
tup.index(5)
tup[4] = 7

# Inbuilt Methods for set.

# set1[1]
"Unordered"
set2 = {'luke', 'murali', 'JC', 'SD'}
print(set2)

set2.remove('luke')

# add Adds an element to the set
set2.add('Nikitha')

print(set2)

set2.add('Ajith')

set2.add('Ajith')

print(set2)


# clear()  Removes all the elements from the set
set2.clear()

# copy Returns A copy of the set
set3 = set2.copy()

print(set2)
print(set3)

# difference() :Returns a set containing the
# elements from the first set which doesnt
# match with second set


x = {"apple", "banana", "cherry", 'yellow', 'luke'}
y = {"google", "microsoft", "apple"}

print(x)
print(y)

# x-y
z = x.difference(y)

print(x)
print(y)
print(z)

z = x.difference(y)

z = y.difference(x)
print(z)


# difference_update

x = {"apple", "banana", "cherry", 'luke'}
y = {"google", "microsoft", "apple"}

print(x)
print(y)


x.difference_update(y) # x-y
print(x)
print(y)

y.difference_update(x)
print(y)


# Discard

fruits = {"apple", "banana", "cherry", 'apple', 'banana'}
print(fruits)
# fruits = {1,1,1,2,3,4,5,6,7,8}

fruits.discard("banana")
print(fruits)

fruits.discard('apple')
print(fruits)

fruits.discard('banana')

fruits.remove('banana')

fruits.remove('banana')

# Intersection

x = {"apple", "banana", "cherry", 'luke', 'x'}

y = {"google", "microsoft", "apple", 'luke','x'}

z = {'x', 'y', 'apple', 'j', 'luke'}

zz = x.intersection(y)


zz = x.intersection(y, z)
print(zz)

zz = y.intersection(x, z)

zz = y.intersection(z)



# Intersection_update
x = {"apple", "banana", "cherry", 'luke'}
y = {"google", "microsoft", "apple", 'luke'}
z = {'x', 'y', 'apple', 'j'}

print(x)
print(y)
print(z)

x.intersection_update(y, z)
print(x)
print(y)
print(z)


# isdisjoint()

{'apple'} == set()

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook", 'apple'}


z = x.isdisjoint(y)  # if there no instersection is present


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

x.isdisjoint(y)  # if there no instersection is present

# issubset()

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

y.issubset(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook", 'apple'}

x.issubset(y) == True
y.issubset(x)


# issuperset
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

x.issubset(y)
y.issuperset(x)

x = {"apple", "banana", "cherry", "google", "microsoft", "facebook"}
y = {"microsoft", "facebook", 'apple'}

x.issubset(y)

y.issubset(x)
x.issuperset(y)

#y is subset of x
#x is superset of y

x.issubset(y)
y.issubset(x)

x.issuperset(y)
y.issuperset(x)


# POP
fruits = {"apple", "banana", "cherry", "google", "microsoft", "facebook",1}

print(fruits)

fruits.pop()

print(fruits)


# Remove:

fruits = {"apple", "banana", "cherry"}

print(fruits)

fruits.discard('banana')

print(fruits)

fruits.remove("banana")

print(fruits)

fruits.remove("banana")



# Symmetric_difference :
"""
Return a set that contains all items from both sets, 
except items that are present in both sets
"""

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference(y)

x = {"apple", "banana", "cherry", 'LUKE'}
y = {"google", "microsoft", "apple", 'sahana', 'LUKE'}

z = x.symmetric_difference(y)

print(z)

# Symmetric_difference_update:

# inserts the symmetric differences from this set and another

x.symmetric_difference_update(y)

# Union :-

# Return a set containing the union of sets

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple", "banana"}

print(x)
print(y)

z = x.union(y)

print(z)

x = {"apple", "banana", "cherry"}
y = ("google", "microsoft", "apple", "banana")
x.union(y)

{"apple", "banana", "cherry"}.union(("google", "microsoft", "apple", "banana"))

z = x.union(y)


# update()
# Update the set with another set, or any other iterable

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple", "banana"}

print(x)
print(y)

x.update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = ["google", "microsoft", "apple", "banana"]
x.update(y)
print(x)

names ={'pavitra', 'Luke', 'Mahalaxmi', 'yaswanth', 'saiKumar'}


# Inbuilt Methods In Dictionary (11):
"""
{K:v}
"""

# clear()
""" clear method in Dict deletes all the values in dict and return empty dict"""

car = {"brand": "Ford", "model": "Mustang", "year": 1964}
type(car) == dict 
print(car)

car.clear()

print(car)


# copy

car = {"brand": "Ford", "model": "Mustang", "year": 1964}

x = car.copy()

print(x)

# fromkeys

"dict.fromkeys(keys, values)"
"{k:v}"

x = ('key1', 'key2', 'key3')  # keys
y = []  # values

thisdict = dict.fromkeys(x, y)

x = ['key1', 'key2', 'key3', 'key4', 'key5']  # keys
y = [1,2,3,4,5]  # values

xx = dict.fromkeys(x, y)
print(xx)

keys = ['punith', 'sahana', 'luke']
value = []

empty_dict = dict.fromkeys(keys, value)
print(empty_dict)

from numpy.random import randint

for each_key in empty_dict.keys():
    empty_dict[each_key] = randint(0,100,5).tolist()





# get

car = {"brand": "Ford", "model": "Mustang", "year": 1964}

car.get("cc", " ")

# dict.get('key')

car.get('model')
car.get('brand')

car['model']

# items
x = car.items()

for k, v in car.items():
    print(f'this is Key : {k}')
    print(f"this is value : {v}")
    print('end of a loop')
    print('\n')


# keys
car.keys()

# values
car.values()

# pop
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(car)
car.get('model')
car.pop('year')


# update:
car.update({'color': 'white'})
print(car)

car['owner'] = 'lakshmi'

# popitem
car.popitem()
print(car)


# setdefault
car.setdefault('xyz124', 'luke')
print(car)

car.setdefault("model", "Mustang")
print(car)


#assignment
names = ['pavitra', 'Luke', 'Mahalaxmi', 'yaswanth', 'saiKumar', 'Luke', 'luke', 'saikumar', 'Yasmin', 'Sacheeta']

names_list = [i.lower() for i in names]
'remove repated names and finally remove luke'

for i in names_list:
    if names_list.count(i)>1: #3
        if i == 'luke':
            range_count = names_list.count(i)
        else:
            range_count = names_list.count(i)-1
        for each_count in range(range_count):
            names_list.remove(i)
        


x = 'chaitanya'

x[::-1]

num = 123456
'Typecasting'
type(int(str(num)[::-1]))