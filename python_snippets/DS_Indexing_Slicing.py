# Classification of Data Structures
# 1) "Mutable" : changable
# 2) "Immutable" : unchangable

marks1 = 40, 30

data_structures = "list, set, dictionary, tuple"

# Mutable
'list, set, dictionary'

list1 = [1, 2.5, 'mn']
print(list1)

list1.append('tk')
list1[1] = 3.5

set1 = {1, 2.5, 'mn'}
set1.add('TK')  # orderless

dict1 = {1: 'english', 2: 'science', 3: 'tamil'}
dict1[4] = 'maths'


print(dict1)

# Immutable
tup1 = (1, 2.5, 'mn')

tup1[1] = 3.5

tup1[3] = 'tk'

# Data Structures.
# counting [0....inf]


# indexing
"""
Indexing means referring to an element of an 
iterable by its position within the iterable.
"""

'python numbering will start from 0'


students_list = []
for i in range(8):
    pupil_name = input('Please enter the name')
    students_list.append(pupil_name)

students_list

students_list[students_list.index('prasath')]

list1 = [999, 2.5, 'luke']
index =   0,   1,     2  



l =    [ 1,   2,  3,  4,  5,  6,  7,  8,  9, 10]

lind =   0,   1,  2,  3,  4,  5,  6,  7,  8,  9

rind = -10,  -9, -8, -7, -6, -5, -4, -3, -2, -1

from numpy.random import randint, choice
size = choice(randint(0,100,50))

list2 =  randint(0,1000,size).tolist()





"""slicing"""
l[5:9]


print(l[0], l[-1])


JJ = [
      'Lakshmi', 'prasanth', 'Harshini', 'Asshutosh', 
         0           1          2            3
      
      'Viknesh', 'jayram', 'pavan', 'punith'
         4           5          6      7 
      ]

#slicing -> jj[start:stop+1]
JJ[2:6]



k = [0, 1, 2, 3, 4, 5, 6, 'LUKE', 'SAYED']
k[4:]
k[:5]

tup2 = (999, 2.5, 'luke')
tup2[2]

tup = (1, 2, 3, 4, 5, 6)
tup1 = (1.2, 2.3, 3.4, 4.5)
tup3 = ('luke', 'vibhav', 'sayed')
tup3[-2]

set1 = {999, 2.5, 'luke'}



list(set1)

set2 = {'luke', 'murali', 'JC', 'SD'}


set = {1, 2, 3, 4, 5, 6}
set1 = {1.2, 2.3, 3.4, 4.5,'luke', 'murali', 'JC', 'SD'}



set1
l1 = [1, 2, 3, 4, 5, 6,6,5,6,5]
list(set(l1))

list(map(set,l1))

dictionary = {}
# 'key': 'value'


# Keys = int,float,string
# value = int,float,string,list,set,tuple,dictionary


diction = {'std1': 'shree', 'std2': 'tarun', 'std3': 'niyas'}

diction['std1']

diction['std3']

dict = {1: 'english', 2: 'science', 3: 'tamil'}
dict[1]
dict[2]

dict = {1.2: 'english'}
dict[1.2]

dict1 = {'stds': ['shree', 'tarun', 'niyas', 'murali', 'keerthika']}
dict2 = {'stds': ('shree', 'tarun', 'niyas', 'murali', 'keerthika')}

dict1['stds']
dict2['stds']


# SLICING
"""Slicing means getting a subset of elements 
from an iterable based on their index's."""

'list = 5000 elements'
list1 = ['luke', 'shree', 'tarun', 'salam', 'SAYED']
#ltor = [  0,      1,        2,       3,       4   ]
#rtol  =[ -5,     -4,       -3,      -2,      -1   ]

list1[1]
list1[2]
list1[3]

#slicing syntax
list1['start_inx_num':'end_inx_num'+1]
list1[0:4]

name = 'ThenmozhiEZhilarasan'
#indexing on string
name[10]
name[9:]
name[-11:]
name[:9]

name[0:9]






#indexing and slicing on tuple, set and dict

tup1 = ('luke', 'shree', 'tarun', 'niyas', 'SAYED')

tup1[1:4]
tup1[-4:-1]

tup2 = (999, 2.5, 'luke')
tup2[1]

tup = (1, 2, 3, 4, 5, 6)
tup1 = (1.2, 2.3, 3.4, 4.5)
tup3 = ('luke', 'vibhav', 'sayed')

set1 = {999, 2.5, 'luke'}


'set is unordered'
# set1[1]
set2 = {'luke', 'murali', 'JC', 'SD'}


set = {1, 2, 3, 4, 5, 6}
set = {1.2, 2.3, 3.4, 4.5}

dictionary = {}
# 'key': 'value'


diction = {'std1': 'shree', 'std2': 'tarun', 'std3': 'niyas'}
diction.values()
diction['std3']

dict = {1: 'english', 2: 'science', 3: 'tamil'}
dict = {1.2: 'english'}
dict = {'stds': ['shree', 'tarun', 'niyas', 'murali', 'keerthika']}
dict = {'stds': ('shree', 'tarun', 'niyas', 'murali', 'keerthika')}


std = {'MahaLaxmi' : [12,13,14,10,6], 'yasmin' : [14,15,13,12,11]}