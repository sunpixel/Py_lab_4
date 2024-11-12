'''Excercise 6'''
# pylint:disable=W0718
# Comment to suppress warning

from errors import BaseError, ValueErrorExc, VarTypeError

class Product:
    '''Defines product'''
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        # Define extra variables
        self.minp = 100
        self.maxp = 5000
        #
        self.validate_name(name)
        self.validate_price()
        self.validate_quantity()

    def validate_name(self, name):
        '''Performs data validation'''
        if not isinstance(name, str):
            raise BaseError("Name must be a string.")
        if len(name.strip()) == 0:
            raise BaseError("Product name cannot be empty.")

    def validate_price(self):
        '''Performs data validation'''
        self.transform(0)
        if not isinstance(self.price, (int, float)):
            raise VarTypeError(self.price, "Price must be a number.")
        if self.minp >= self.price or self.price >= self.maxp:
            raise ValueErrorExc(self.price, self.minp, self.maxp)

    def validate_quantity(self):
        '''Performs data validation'''
        self.transform(1)
        if not isinstance(self.quantity, int):
            raise VarTypeError(self.quantity, "Quantity must be an integer.")
        if self.quantity < 0:
            raise ValueError("Quantity cannot be negative.")

    def transform(self, choice):
        '''Converts vars'''
        if choice == 0:
            try:
                self.price = float(self.price)
            except TypeError as e:
                raise VarTypeError(self.price, "Price must be a number.") from e
        elif choice == 1:
            try:
                self.quantity = int(self.quantity)
            except TypeError as e:
                raise VarTypeError(self.quantity, "Quantity must be a number.") from e
        else:
            print('Selected action is non existent')

def func_1(args):
    '''Function 1'''
    try:
        product = Product(args[0], args[1], args[2])
        print(f"Product created: Name=  {product.name},")
        print(f"Price=                  {product.price},")
        print(f"Quantity=               {product.quantity}")
    except BaseError as e:
        print(e)
    except VarTypeError as e:
        print(e)
    except ValueErrorExc as e:
        print(e)
