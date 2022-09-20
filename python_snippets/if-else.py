
'Satabdi'

'some sort of condition must be evaluated:'
condition = 'Satabdi is hungry'

"""
a decision must be taken on the condition and 
appropriate action must be performed base on the decision
""" 


"""
condition = 'Satabdi is hungry'

decision:     True          |             False

Actions :   'eating'        |          'not eating'

"""


"""
condition = Venkatesh are you going to college

decision:        True                  |              False

Actions :   'started to  leave'        |           'not going college but going play pubg'

"""


a = 5
b = 5

a == b

type(a) is int

'i' in 'India'
6 in [1, 2, 5, 6, 7, 3, 8]


'if , else, elif'
# Answ = input('Are you hungry T/F')
# Answ ='N'
# if 'T' == 'T':  # True
#     print('eating')
# else:
#     print('Entered Else block since the condition is false')
#     print('not eating')

"""
condition = 'chaitanya is hungry'

decision:     True          |             False

Actions :   'eating'        |          'not eating'

"""

a = 5
b = 15

condition = "is a equal to b => a==b "
decision = True/False 
"""
action = True -> print(A is equal to b)
         False -> print(A is not equal to b)
"""


a = 5
b = 15

if a==b:

    '-> do a particular action'

else:
    
    '-> do another particular action'
    



if a == b:
    print("a is equal to b")
else:
    print("a is not equal to b")


a = 15

if a%2==0:
    print("Even")
else:
    print("Odd")








a=5
b=15

#    T   or    F = T
if a < b or a == b:  # decision
    # True --> #action
    print('Yes')
else:
    # False --> #action
    print('No')

#if else
# elif
a = 5
b = 10
if a == b:
    print('xyz')

elif a <= 5:
    print('5abc')

elif a <= 10:
    print('10abc')

elif a>10 and a<=15: #T and T = T
    print('uvw')

elif a>15 or a>20: #T or F = T
    print('ijk')

else:
    print('No')





'not'

'logical operator :'
'and, or'

'and'

if  a >=0:
    print(...)
elif a <= 10:
    print(...)
else:
    print(...)

a = 1

if a >= 0 and a >= 10:
    # T   and   F = F
    print('variable a value doesn"t lie between 0 and 10')
else:
    print('a is rouge')

a = 5






if a >= 0 or a <= 2:
   # True  or  False  = T
    print('variable a value lies between 0 and 10')
else:
    print('a is rouge')

# false and false =
# true and false =


# OR

a = 5

if a >= 0 or a <= 2:
    # T    or    F = T
    print('variable a value lies between 0 and 10')
else:
    print('a is rouge')


'if else'

a = 10
b = 6

if a > 5:
    c = a+b
    print(c)
else:
    c = a-b
    print(c)


'if elif else'


inp = input()
print(inp)
# Hungry
if inp.lower() == 'hungry':
    print('eat')
else:
    print('dont eat')


students = ['satabdi', 'Vamshi', 'Chaitanya', 'venkatesh', 'Niharika', 'christina']




inp = input()
if inp in students:
    print('Student')
else:
    print('not student')




'nested statements:'
a = 4.9

'Nested if else'
if a >= 0: #T
    if a > 5: #T
        if a < 10: #F
            print('yes')
        else:
            print('No')
    else:
        print('valid')
else:
    print('Invalid')


a = 17
if a >= 0:
    if a > 5:
        if a < 10:
            print('yes')

    


a = 25

if a == 5:
    print('Yes')
elif a <= 10:
    print('higher')
else:
    print('No')

"""
section1(M1-10)
section2(M11-20)
section3(M20-above)

section4(F1-10)
section5(F11-20)
section6(F20-above)
"""
'M/F'

gender = 'F'
age = 12

if gender == 'M':
    if age in range(1,11):
        print('Section 1')
    elif age in range(11,21):
        print('Section 2')
    else:
        print('Section 3')
else:
    if age in range(1,11):
        print('Section 4')
    elif age in range(11,21):
        print('Section 5')
    else:
        print('Section 6')




a = 'l'
name = 'Luke'

if a in name:
    print(f'{a} is in {name}')
else:
    print(f'{a} not in {name}')

############################################################

age = input('Please enter age')
gender = input('Please enter your gender')


if gender.lower() == 'm':
    if age>=1 and age<=10:
        print('section1')
    if age>=11 and age<=20:
        print('section2')
    if age>20:
        print('section3')
else:
    if age>=1 and age<=10:
        print('section4')
    if age>=11 and age<=20:
        print('section5')
    if age>20:
        print('section6')
