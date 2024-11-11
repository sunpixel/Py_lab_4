'''Exercise 2'''
# pylint:disable=W0718
# Comment to suppress warning

def func_1(num1, num2):
    '''Function 1'''
    try:
        print(f'Devision result is: {float(num1) / float(num2)}')
    except Exception:
        print("You sneaky bastard, trying to do smthing wrong. No can do")
        print('Enter 2 new numbers:')
        num1 = float(input())
        num2 = float(input())
        func_1(num1, num2)
