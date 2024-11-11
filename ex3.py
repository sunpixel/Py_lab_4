'''Exercise 3'''
# pylint:disable=W0718
# Comment to suppress warning

def func_1(values):
    '''Function 1'''
    try:
        # numbers
        x = 0
        for i in values:
            x += float(i)
            print(f'Current value: {x}')
    except Exception:
        # strings
        x = ''
        for i in values:
            x += i
            print(f'Current value: {x}')
    finally:
        print (f'Result: {x}')
        print('Program finished')
