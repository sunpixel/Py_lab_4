'''Excercise 4'''
# pylint:disable=W0718
# Comment to suppress warning

import json
import main

def func_1(num1, num2):
    '''Function 1'''
    try:
        num1 = float(num1)
        num2 = float(num2)
        print(f'Division result: {num1 / num2}')
    except TypeError:
        print("One or two of the provided numbers are not a number")
        print('Enter 2 new NUMBERS to procced:')
        func_1(input(), input())
    except ZeroDivisionError:
        print("Division by 0 is forbidden, so i changed it to 1")
        print(f'Here is the result: {num1}')
    except BaseException as e:
        print(f"Sorry for the trouble, but the program has run into an issue. {e}")
        print('Please try again later.')
    finally:
        print("Func_1 exception block finished execution.")

def func_2(*nums):
    '''Function 2'''
    x = 0
    i = 0
    try:
        while i <= len(nums[0]):
            print(f'Current number in tuple is: {nums[0][i]}')
            if i == 0:
                x = nums[0][i]
                i += 1
            else:
                print(f'Division result is: {x / nums[0][i]}')
                x = nums[0][i]
                i += 1

    except IndexError:
        print('IndexError detected, switching to another execuatble')
        while i < len(nums[0]):
            print(f'Current number in tuple is: {nums[0][i]}')
            if i == 0:
                x = nums[0][i]
                i += 1
            else:
                result = x / float(nums[0][i])
                print(f'Division result is: {result}')
                x = result
                i += 1

    except ZeroDivisionError:
        print('Zero division is not permitted. Reseting your result')
        func_2(main.get_val_unk(len(nums[0])))

    except TypeError:
        print('TypeError detected, switching to another execuatble')
        i = 0
        while i < len(nums[0]):
            print(f'Current number in tuple is: {nums[0][i]}')
            if i == 0:
                x = float(nums[0][i])
                i += 1
            else:
                result = x / float(nums[0][i])
                print(f'Division result is: {result}')
                x = result
                i += 1


def func_3(file_path = 'Py_4/123.json'):
    '''Function 3'''
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        for key, value in data.items():
            print(f"{key}: {value}")

    except FileNotFoundError as e:
        print(f"File not found: {file_path}. Error: {e}")

    except PermissionError as e:
        print(f"Permission to read denied: {file_path}. Error: {e}")

    except json.JSONDecodeError as e:
        print(f"Unable to decode JSON: {file_path}. Error: {e}")
