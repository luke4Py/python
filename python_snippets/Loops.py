############################### Loops #########################


# While Loop

# Example for 'While loop'

# N number of times

# i = int(input())
i = 20

while i > 10:
    print(f"i value is {i}")
    i-=1

from numpy import random

tries = ['rock','paper','scissor']

random.choice(tries)

print(i)
# GAME
# random_number = random.randint(1,10,1)[0]
# print(f"random_number is {random_number}")
# guess = int(input('enter value between 1-10'))
# while guess != random_number:
#     if guess > 0:
#         if guess > random_number:
#             print(f"guess number {guess} is big than random")
#         elif guess < random_number:
#             print(f"guess number {guess} is less than random")
#     else:
#         print("sorry that you have giveup!")
#         break
#     random_number = random.randint(1,10,1)[0]
#     print(f"random_number is {random_number}")
# else:
#     print("Congratulations. YOU WON!")


# for Loop

# Example for 'for loop'

#Example : 1

snacks = ['pizza', 'burger', 'shawarma', 'franky'] #List

for snack in snacks:
    print(f"Todays Special is {snack.upper()}")



for ind, snack in enumerate(snacks, start=10):
    print(ind, snack)


loop_count = 0
for snack in snacks:
    loop_count += 1
    print(f"Loop_number = {loop_count}")
    print("current snack: ", snack)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in nums:
    if i % 2 == 0:
        print(f'{i} is an even number')
    else:
        print(f'{i} is an odd number')


#Range
a = 1
b = 2
name1 = 'Luke'
name2 = 'pavithra'

sum([a, b])
len(name1)
no_students = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

list(range(1,27))

list(range(27))

user_number = int(input('Enter a number'))

for i in range(0,user_number):
    if i%2==0:
        print(f"{i} is an even number")
    else:
        print(f"{i} not an even number")


#nested Loops
from numpy.random import randint
names = ['Priya','venu','Salam','Tamil']
subject = ['Maths','Social','Science']

for student in names:
    for sub_name in subject:
        print(f"{student} subject is {sub_name} and marks is {randint(0,100)}")
    print('\n')

# range
r = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
range('start,stop,step')
range(0, 11, 1)

list1 = []
for i in range(1, 21, 1):
    print(i)
    list1.append(i)

for i in range(40, 19, -1):
    print(i)

#Example: 2

for i in range(11):
    print(i)

for i in range(1, 3+1):
    print(i)

for i in range(1, 20, 2):
    print(i)

# Ex 3
# nested list
stock_prices = [['Apple', 300], ["samsung", 400], ["nokia", 100]]

"""
[
item  =  ['Apple',300],
item  =  ["samsung",400],
item  =  ["nokia",100]
]
"""

"""
[
item  =  ['Apple',300] --> item[0],
item  =  ["samsung",400]--> item[0],
item  =  ["nokia",100]--> item[0]
]
"""
for item in stock_prices:
    print(item[0])

#   _______________________________________________

d = {'k1': 1, 'k2': 2, 'k3': 3}
d = {
    'kA': {
        'ki': [1, 2, 3],
        'kii': [4, 5, 6]
    },

    'kB': {
        'kiii': [7, 8, 9],
        'kiv': [10, 11, 12]
    }

}


d.items()

for item in d.items():
    print(item)

loop = 0
for key, value in d.items():
    loop += 1
    print(f"loop : {loop}")
    print(f"key : {key}")
    print(f"value : {value}")


# Nested Loops
# Nested 'for in for' and for in while will be asignments problems
# Nested while in for

travelling = input("yes or no")

while travelling == 'yes':

    num = int(input("number of people travelling: "))

    for num in range(1, num+1):
        name = input("Name: ")

        Gender = input("Male or Female: ")

        print(name)

        print(Gender)
    break


for i in range(11):
    print('i : ', i)
    for j in range(10, 21):
        print('j :', j)

# range(start, stop, step) = []


a = 5
if a > 0:
    print('No')
else:
    pass  # skip


# pass, break, continue

for i in range(1, 21):  # [1...20]
    if 11 >= 10:
        if 11 % 2 == 0:
            print(f'even numb : {11}')
        else:
            pass #skip
            print('continuing the loop')
            # continue
    else:
        print(i)


# PASS
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in nums:
    if i % 2 == 0:
        print(f'{i} is an even number')
    else:
        pass


for i in nums:
    print(i)
else:
    print('Luke')