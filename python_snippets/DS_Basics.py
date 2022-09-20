'Data Structures'
'list, tuple, set, Dictionary'
"""
var = [............]
"""
[]

'LIST'

jj = []
jj
type(jj)

kk = list()
kk
type(kk)

f = [123, 124, 125]
print(f)
type(f)


# int

students_rolls = [123, 124, 125, 126, 127]
print(students_rolls)
'int, float, string, complex'

# strings
student_names = ['luke', 'nanda', 'devraj', 'manoj', 'grishma', 'navya']
print(student_names)


# float
student_marks = [123.5, 124.5, 125.5]
print(student_marks)

# mixed Data types
one_student = [123,'luke', 95.0, 95.0]
print(one_student)

type(one_student)
print(one_student)


'Tuple'

kk = ()
print(kk)
type(kk)

jj = tuple()
print(jj)
type(jj)


x = (1, 2, 3)
print(x)
type(x)

y = (222,555,333)

ff = (123.5, 124.0, 125.0)
print(ff)
type(ff)

student_tuple = ('luke', 'nanda', 'devraj', 'manoj', 'grishma', 'navya')
print(student_tuple)
type(student_tuple)

one_student_tuple = (123,'luke', 95.0, 95.0)
print(one_student_tuple)
type(one_student_tuple)


"set"
# x = {}
# print(x)
# type(x)

sets = set()
print(sets)
type(sets)


y_set = {222,555,333}

ff_set = {123.5, 124.0, 125.0}

student_set = {123, 'luke', 'nanda', 'devraj', 'Manoj', 'grishma', 'navya'}

one_student_set = {123,'luke', 95.0, 95.0}

set1 = {'luke','luke', 95.0, 550, 550, 'Luke', 'Ashish'}
type(set1)
print(set1)


# dictionary

#  {k:v} Key-value pair

luke = 'Hyderabad'
Anil = 'Hyderabad'
Avinash = 'Nellor'
Anirudh = 'punjab'
Manthan = 'Mumbai'


{'key': 'value'}

{'name': 'city'}

{'Luke': 'Hyderabad'}


location = {
               'Luke': 'Hyderabad',
               'Anil' : 'Hyderabad',
               'Avinash' : 'Nellor',
               'Anirudh' : 'punjab',
               'Manthan' : 'Mumbai'
          }
type(location)

location.get('Luke')


student_marks =   {    
                    'divya'        : 45, 
                    'pravalika'    : 46,
                    'piyush'       : 50,
                    'vamshi'       : 46 
                    }

student_name =   {    
                     'std1' : 'divya', 
                     'std2' : 'pravalika',
                     'std3' : 'piyush',
                     'std4' : 'vamshi' 
                    }

student_marks['vamshi']

#same key with different value
student_name =   {    
                    'std1' : 'divya', 
                    'std2' : 'pravalika',
                    'std3' : 'piyush',
                    'std4' : 'vamshi', 
                    'std4' : 'deepan' 
                    }

student_name['std4']


student_marks[student_name['std3']]

special_char =   {    
                     'spc1' : '@', 
                     'spc2' : '#',
                     'spc3' : '*',
                     'spc4' : '^' 
                    }
special_char['spc1']

student_name['std4']
student_marks['divya']
student_marks['pravalika']



f = {'k1':'v1', 'k2':'v2', 'k3':'v3'}


ff = {1:0, 2:1, 3:2, 4:3} #possible


fff = {1.5 : 0, 2.9 : 1, 3.0 : 2, 4.0 : 3}

fff[3]


x = {'luke': 'Hyderabad', 
     'Anil': 'Hyderabad',
     'Anirudh': 'punjab', 
     'Manthan': 'Mumbai'}

student_marks_int =   {    
                    'divya'        : 45, 
                    'pravalika'    : 46,
                    'piyush'       : 50,
                    'vamshi'       : 46 
                    }

student_marks_float =   {    
                    'divya'        : 45.0, 
                    'pravalika'    : 46.0,
                    'pravalika'    : 46.0,
                    'piyush'       : 50.0,
                    'vamshi'       : 46.0 
                    }

type(x)

print(x)

y = {'luke': ['Hyderabad', 'chennai', 'Andhra'], 
     'Anil': ['Hyderabad', 'Andhra']}

y.get('luke')

y = {1: ['Hyderabad', 'chennai', 'Andhra'], 
     'Anil': ['Hyderabad', 'chennai', 'Andhra']}


y = {'luke': ('Hyderabad', 'chennai', 'Andhra'), 
     'Anil': ('Hyderabad', 'chennai', 'Andhra')}

z = {'luke': {'anil':'Hyderabad', "Avinash":'chennai', 'Anirudh':'punjab'},
     'Sahith':{'navya' : 'chennai', 'jeevi':'Madras', 'naveen':'Hyderabad'}}

z.get('luke').get('Anirudh')


print(z)


x['luke']
x['Anirudh']

"""
1) Dictionary's format is {key : value} pair
2) Dict keys can be a string, int or float
3) Dict values can store any type of data ex: int, str, float, list, tuple, set, dict
"""







#########################################################################################################################


'How to create empty data structures:'

list1 = []
x = list()
type(list1)
len(list1)



tuple1 = ()
type(tuple1)
len(tuple1)

set1 = set()
type(set1)
len(set1)


dictionary1 = {}
type(dictionary1)
len(dictionary1)
