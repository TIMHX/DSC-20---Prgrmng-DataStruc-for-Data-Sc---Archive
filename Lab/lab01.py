
# Question 1
def calculator(input1, input2, operation):
    """
    Return the result of the given operation
    >>> calculator(3, 4, '+')
    7
    >>> calculator(3, 4, '-')
    -1
    >>> calculator(3, 4, '*')
    12
    >>> calculator(3, 4, '/')
    0
    >>> calculator(3, 4, '%')
    'Something went wrong'

    >>> calculator(3, 4, 5)
    'Something went wrong'
    >>> calculator(5, 8, "/")
    0
    >>> calculator(10, 8, "/")
    1
    >>> calculator(5, 10, "-")
    -5
    """
    # YOUR CODE IS HERE #
    if operation == '+':
        return input1 + input2
    elif operation == '-':
        return input1 - input2
    elif operation == '*':
        return input1 * input2
    elif operation == '/':
        if input2 == 0:
            return None
        else:
            return input1//input2
    elif operation == '%':
        if input1 >= input2:
            return input1 % input2
        else:
            return 'Something went wrong'
    else:
        return 'Something went wrong'
# Question 2

def new_string(input):
    """
    Return a tripled string with only two first and two
    last characters. If the string is shorter than 4 characters then
    triple the entire string and return it.
    >>> new_string("mac")
    'macmacmac'
    >>> new_string("mouse")
    'mosemosemose'

    >>> new_string("")
    ''
    >>> new_string("pin")
    'pinpinpin'
    >>> new_string("pinned")
    'piedpiedpied'
    >>> new_string(" ")
    '   '
    >>> new_string(" = ^v^ = ")
    ' ==  ==  == '
    """
    # YOUR CODE IS HERE #
    if len(input)<4:
        return input*3
    else:
        return (input[:2]+input[-2:])*3

# Question 3

def i_want_cake(calories, isSunday):
    """ Return a string according to the rules
    provided in th write up.
    >>> i_want_cake(150, 1)
    'safe to eat'
    >>> i_want_cake(150, 0)
    'proceed with caution'

    >>> i_want_cake(165, True)
    'proceed with caution'
    >>> i_want_cake(999, 999)
    'better not'
    >>> i_want_cake(1, False)
    'safe to eat'
    >>> i_want_cake(155, 0)
    'better not'
    """
    # YOUR CODE IS HERE #
    if isSunday != 1:
        if calories <= 100:
            return 'safe to eat'
        elif 101 <= calories <=150:
            return 'proceed with caution'
        else:
            return 'better not'
    elif isSunday == 1:
        if calories <= 150:
            return 'safe to eat'
        elif 151 <= calories <=200:
            return 'proceed with caution'
        else:
            return 'better not'

# Question 4

def is_bingo(input, index):
    """Return True if one of the first elements in the
    list is a "bingo!" can be found before a given index.
    The list length may be less than a given position.
    If that's the case, return False
    >>> is_bingo(['bingo!', 'table'], 1)
    True
    >>> is_bingo(['bingo!', 'table'], 0)
    False
    >>> is_bingo(['bingo!', 'table'], 6)
    False

    >>> is_bingo([], 0)
    False
    >>> is_bingo(['bingo!'], 0)
    False
    >>> is_bingo(['not', 'bingo'], 2)
    False
    >>> is_bingo(['Bingo!', 'bingo!'], 1)
    False
    >>> is_bingo(['Bingo!', 'bingo!'], 2)
    True
    >>> is_bingo(['Bingo!', 'bingo!'], 5)
    False
    """
    # YOUR CODE IS HERE #
    if index > len(input):
        return False
    else:
        for i in range(len(input)):
            if input[i] == 'bingo!' and index > i:
                return True
        else:
            return False
