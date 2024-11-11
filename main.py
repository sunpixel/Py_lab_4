'''Main executable file'''

import ex1
import ex2
import ex3
import ex4


def get_value():
    '''Function to get value of unspecified type from user'''
    print('Please enter a value:')
    value = input()
    return value

def get_val_unk(number = 0):
    '''Function to get an unknown number of variables'''
    values = []
    i = 0
    print('Enter number of variables: ')
    if number <= 0:
        num = int(input())
    num = number
    while num > i:
        i += 1
        print('Enter value:')
        values.append(input())
    return values

if __name__ == '__main__':
    ex1.func_1(get_value())
    ex1.func_2(get_value())
    #
    ex2.func_1(get_value(), get_value())
    #
    ex3.func_1(get_val_unk())
    #
    ex4.func_1(get_value(), get_value())
    ex4.func_2(get_val_unk())
    ex4.func_3()
    #
