# Operators

"""
1. Arithmetic operators
2. comparision Operator
3. Assignment Operators
4. Membership Operators
5. Identity Operators
6. logical Operators
"""

# Arithmetic operators

10+2
a = 10
b = 2

c = 'Rahul'
d = 'M'

# addition +
a + b
d + c #Concatenation


# subtraction
a - b
d - c

# multiplication
a * b
c * 3

# division
a / b # division output will always be float 
c/2

# Modulus
a % b
7 % 2

a, b = 10, 2
# exponential
a**b  # 10**2


#_________________________________#

a = 10
b = 1
# comparision Operator

# It gives in bool values(True/False)

a == 10

a == b # if a is equal to b  

a != b #-> a not equals to b

a > b

a < b

a >= b

a <= b


#python is case sensitive
'luke' == 'Luke'

'Madhuri' != 'madhuri'

len('luke') == len('Luke')

len('mahalaxmi') == len('mahalexmi') #looking len of the string, thus string match is not necessary

# Assignment Operators
a = 10
b = 20
c = 30

c = c+b

c += b  # its nothing but c = c+b c = 30+20
c 
c -= b  # c = c-b
c 
c *= b  # c = c*b ->600
c
c /= b  # c = c/b ->30
c
c %= b # c= c%b
c
c **= b  # 10**20 c = c**b
c

# Membership Operators
# It will check that left value is a member of right value or not
'Python' == 'python'

"y" in "Python"

"l" in "Python"

"p" in "Python"

"P" in "python"

"P" in "python" and 'y' in 'python'  

"p" in ['Python','bdb','rhbebe']

6 in [1,2,3,4,5,6]

# Identity Operators
'IS'
x = int(1)
y = int(1)

x == y

c = [1, 2, 3, 4]
b = [1, 2, 3, 4]
type(c) is tuple
type(1) is int


1 is 1
type('luke') is str
'l' is 'luke'
2.5 is 2.4

# logical Operators

# and , or, not


maths = 75
science = 34
hindi = 55

maths >= 35 and science >= 35  #T and T = T
'   T       and     F    =  F'

maths >= 35 and science <= 35 and hindi >=35


maths >= 35 or science >= 35 or hindi >=35


10 not in [1,2,3,4,5]
'p' not in 'python'

'p' != 'P'


s,k = 80, 70

s > 100 and k < 100  #F
False    and True

s > 100 or k < 100 #T


