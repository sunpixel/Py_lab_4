'''Exception deffinition class'''

class BaseError(Exception):
    '''My own exception'''

    def __init__(self, msg):

        self.message = msg

    def __str__(self):
        '''Printing out the result'''
        return f'Error: {self.message}'

class ValueErrorExc(Exception):
    '''My own exception'''

    def __init__(self, current, minP, maxP):
        self.current = current
        self.min = minP
        self.max = maxP

    def __str__(self):
        '''Printing out the result'''
        return  f'Error: {self.current} is not in ' \
                f'values range {self.min} and {self.max}'


class VarTypeError(Exception):
    '''My own exception'''
    def __init__(self, value, msg):
        self.val = value
        self.msg = msg

    def __str__(self):
        return f'Error: {self.val} {self.msg}'
