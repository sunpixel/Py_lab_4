'''Main executable file'''

# pylint:disable=W0718
# Comment to suppress warning

import ex1
import ex2
import ex3
import ex4
import ex5
import ex6

def divide():
    '''Prints spaces'''
    print('=' * 40)

def get_value():
    '''Function to get value of unspecified type from user'''
    print('Please enter a value:')
    value = input()
    return value

def get_val_unk(number = 0):
    '''Function to get an unknown number of variables'''
    values = []
    i = 0
    if number <= 0:
        print('Enter number of variables: ')
        num = int(input())
    else:
        num = number
    while num > i:
        i += 1
        print('Enter value:')
        values.append(input())
    return values

if __name__ == '__main__':
    try:
        ex1.func_1(get_value())
        divide()
        ex1.func_2(get_value())
        divide()
        #
        ex2.func_1(get_value(), get_value())
        divide()
        #
        ex3.func_1(get_val_unk())
        divide()
        #
        ex4.func_1(get_value(), get_value())
        divide()
        ex4.func_2(get_val_unk())
        divide()
        ex4.func_3()
        divide()
        #
        ex5.func_1(get_value())
        divide()
        #
        print('We would like to get the following info:')
        print('Name, Price, Quantity')
        ex6.func_1(get_val_unk(3))
        divide()
    except Exception as e:
        print('An error occured durin execution sorry')
        print(e)
