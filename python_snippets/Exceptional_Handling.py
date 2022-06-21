
# Exceptional Handling


inp = int(input('Please enter a Number : '))


try:
    inp = int(input('Please enter a Number : '))
    result = 265/inp
    # raise Exception('zero and valuerror exception cant handle this error')
# except Exception as e:
#     print(f'im handling : {e}')
except ValueError:
    print('Please Enter roll number but no words')
    inp = int(input('Please enter a Number : '))


except ZeroDivisionError:
    print('Please Enter roll number again[ because of zero division error]')
    inp = int(input('Please enter a Number : '))
    print(inp)

'title'
'price'
'condition'
'description'

for _ in range(5):
    try:
        title =input('enter title')
        if len(title) == 0:
            raise Exception('Title not available')

        price =input('enter price')
        if len(price) == 0:
            raise Exception('price not available')

        condition = 'refurbished'

        descp = 'xyz'

        print(title, price, condition, descp)

    except Exception as e:
        print(e)
        pass


"""
try 
except
"""
a = 'luke'

int(a)

d = {'luke': 'Faculty', "saiteja": 'participant', 'Keerthi': 'participant'}

d['ameena']


try:
    inp = int(input('Please enter a Number : '))
    div_op = 25/inp
    print(f'div_op : {div_op}')
    print(f'Roll_number : {inp}')
except ValueError:
    print('Value Error was Raised')
    print('Please enter an integer/numerical Number')
    inp = int(input('Please enter a Number : '))
    print(f'Roll_number : {inp}')
except ZeroDivisionError:
    print('You"re in ZeroDivisionError')
    div_op = 25/(inp+1)
    print(f"from zerodiverror div_op is : {div_op} ")
finally:
    print('Program completed')


try:
    inp = int(input('Please enter a Number : '))
    div_op = 25/inp
    print(f'div_op : {div_op}')
    print(f'Roll_number : {inp}')
except:
    print('Run the program again since an error raise')
finally:
    print('Program completed')


def user():
    try:
        print('code is in Try block')
        inp = int(input('Please enter a Number : '))
    except:
        print('code is in except block')
        user()


user()

def rec_func(x):
    print(x)
    try:
        if x == 1:
            print(' X is equal to 1')
        else:
            raise Exception('X is not 1')
    except Exception as e:
        print(f"--> exception is {e}")
        rec_func(x-1)


rec_func(10)


for i in range(1, int(input()),1):
    try:
        if i%2==0:
            print(f"{i} is even")
            continue
        else:
            raise Exception(f'The num {i} is an odd number')
    except Exception as e:
        print(f"Error : {e}")
        if i%2!=0:
            print(f'Provided Num is odd')
    finally:
        print('This is DS7 Batch')

names = ['Luke','venu','vidhya','priya']

new_names = []
for i in names:
    new_names.append(i.upper())


[i+' DS07' for i in names]


#Map

# map(func, iterable)

set(map(str.upper, names))
vals = ['1','2','3','4']
list(map(int,vals))


list_vals = ['luke', 'Manthan', 'Yogesh']
map(str.upper, )

list(filter(int,vals))


seq = [0, 1, 2, 3, 5, 8, 13]
  
result = filter(lambda x: x % 2 != 0, seq)
even_result = filter(lambda x: x % 2 == 0, seq)
print(list(even_result))
  