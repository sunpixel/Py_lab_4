'''Excercise 4'''
# pylint:disable=W0718
# Comment to suppress warning

import json
import main

def func_1(num1, num2):
    '''Function 1'''
    try:
        float(num1)
        float(num2)
        print(f'Division result: {num1 / num2}')
    except ValueError:
        print("One or two of the provided numbers are not a number")
        print('Enter 2 new NUMBERS to procced:')
        func_1(input(), input())
    except ZeroDivisionError:
        print("Division by 0 is forbidden, so i changed it to 1")
        print(f'Here is the result: {num1}')
    except BaseException:
        print(f"Sorry for the trouble, but the program has run into an issue. {Exception}")
        print('Please try again later.')
    finally:
        print("Func_1 exception block finished execution with.")

def func_2(*nums):
    '''Function 2'''
    x = 0
    i = 0
    try:
        while i <= len(nums):
            print(f'Current number in tuple is: {nums[i]}')
            if i == 0:
                x = nums[i]
                i += 1
            else:
                print(f'Division result is: {x / nums[i]}')
                x = nums[i]
                i += 1

    except IndexError:
        print('IndexError detected, switching to another execuatble')
        while i < len(nums):
            print(f'Current number in tuple is: {nums[i]}')
            if i == 0:
                x = nums[i]
                i += 1
            else:
                print(f'Division result is: {x / nums[i]}')
                x = nums[i]
                i += 1

    except ZeroDivisionError:
        print('Zero division is not permitted. Reseting your result')
        func_2(main.get_val_unk(len(nums)))

    except ValueError:
        print('ValueError detected, switching to another execuatble')
        while i <= len(nums):
            print(f'Current number in tuple is: {nums[i]}')
            if i == 0:
                x = float(nums[i])
                i += 1
            else:
                print(f'Division result is: {x / float(nums[i])}')
                x = float(nums[i])
                i += 1


def func_3(file_path = 'Py_4\123.json'):
    '''Function 3'''
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        for key, value in data.items():
            print(f"{key}: {value}")

    except FileNotFoundError as e:
        print(f"Файл не найден: {file_path}. Error: {e}")

    except PermissionError as e:
        print(f"Permission to read denied: {file_path}. Error: {e}")

    except json.JSONDecodeError as e:
        print(f"Невозможно декодировать JSON: {file_path}. Error: {e}")
