'''Exercise 1'''
# pylint:disable=W0718
# Comment to suppress warning

def func_1(number):
    '''Function 1'''
    try:
        number = float(number)
        number += 222
        print(f'Your number increase by 222 is {number}')
    except TypeError:
        print("You entered an invalid number")

def func_2(string):
    '''Function 2'''
    try:
        number = float(string)
        print('Ypur string is a number!!')
        print(number)
    except ValueError:
        print("There can be numbers in a string, but strinmg itself is not a number. Yay!!!")
        print(f'Result: {string}')
