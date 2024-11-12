'''Excercise 5'''
# pylint:disable=W0718
# Comment to suppress warning

def func_1(value):
    '''Function 1'''
    try:
        if value < 0:
            raise ValueError("Negative value is not allowed.")
        elif value % 2 != 0:
            raise TypeError("Only even numbers are accepted.")
        elif value > 100:
            raise OverflowError("The value exceeds the limit.")
        else:
            print(f"Valid value: {value}")

    except ValueError as e:
        print(f"ValueError: {e}")
    except TypeError as e:
        print(f"TypeError: {e}")
    except OverflowError as e:
        print(f"OverflowError: {e}")
