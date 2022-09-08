#input and output
#syntax
var = input()
print(var)
var = input('help message')
roll = input('Please type your roll_no')
type(eval(roll))

print(roll)

type(roll)

name = input('Please enter your name')
roll = input('please type roll')
print(f'My name is {name}, roll_number is {roll}')

#-----------------------------------------------------------#

# Type Casting:
"When you convert one data type to another"

# with input func (str -> int)
x = float('348')

roll = int(input('Please enter a roll no : '))

int('123.0') #error
int(float('123.0')) #no error

jj = '348.0'
xx = float(jj)
mm = int(xx)

'348.0'
'str->float->int = 348'

roll = int(float(input('Please enter a roll no : ')))
print(roll)
type(roll)
# roll_no = int(roll)
# type(roll_no)


# float to integer
x = 123.6
type(x)  # checking the type of x, it should work
value = int(x)
print(value)
type(value)


# integer to float
y = 1235
type(y)
y = float(y)
print(y)
type(y)

"'bat' int or float"
# string to float and int
z = 'bat'
type(z)
int(z)
float(z)
int("AB1234")

zz = '123'
type(zz)
int(zz)
float(zz)

zz = '123.0'
zz = float(zz)
int(zz)


# float and int to string
str(555444892132)
j = 123.52
type(j)
j = str(j)
type(j)
print(j)


j = 125
str(j)

#Summary:
"""
1) float -> int #works
2) int -> float #works
3) str(alpha) -> float, int #not works123
4) str(numeric) -> float, int #works
5) float, int -> str #works
"""