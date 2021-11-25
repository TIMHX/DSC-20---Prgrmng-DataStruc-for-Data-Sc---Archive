"""
DSC 20 HW 09
NAME: XING HONG
PID: A15867895
"""
two = 2


## Question 1 ##

def checkingInputs(input1, input2, input3):
    """
    You will be handling 3 basic checks
    - are all the input types correct
    - does input2 exist within input3
    - can you divide input1 by input3

    >>> checkingInputs(15, 'key1', {'key1': 5, 'key2': 10})
    3.0

    >>> checkingInputs(15, 'key1', {'key1': 0, 'key2': 10})
    Traceback (most recent call last):
    ...
    ZeroDivisionError: Cannot divide 15 by 0

    >>> checkingInputs(15, 'key1', {'key2': 10})
    Traceback (most recent call last):
    ...
    KeyError: 'Cannot find key1 in the dictionary'

    >>> checkingInputs("15", 2810, ['key2', 10])
    Traceback (most recent call last):
    ...
    TypeError: Inputs are not the correct type

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> checkingInputs(15, 'well', ['well', 10])
    Traceback (most recent call last):
    ...
    TypeError: Inputs are not the correct type
    >>> checkingInputs(1, 'key1', {'key1': 1, 'key2': 10})
    1.0
    >>> checkingInputs(1, '0', ['0', 0])
    Traceback (most recent call last):
    ...
    TypeError: Inputs are not the correct type
    """

    ## YOUR CODE HERE ##
    if not isinstance(input1, int):
        raise TypeError('Inputs are not the correct type')
    if not isinstance(input2, str):
        raise TypeError('Inputs are not the correct type')
    if not isinstance(input3, dict):
        raise TypeError('Inputs are not the correct type')
    if input2 not in list(input3.keys()):
        raise KeyError('Cannot find {0} in the dictionary'.format(input2))
    if input3[input2] == 0:
        raise ZeroDivisionError('Cannot divide {0} by 0'.format(input1))
    return input1 / input3[input2]


## Question 2 ##

def loadFile(filename):
    """
    >>> loadFile("file1.txt")
    'File loaded'

    >>> loadFile("file2.txt")
    Traceback (most recent call last):
        ...
    FileNotFoundError: file2.txt does not exist

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> loadFile("yoyo.txt")
    Traceback (most recent call last):
        ...
    FileNotFoundError: yoyo.txt does not exist
    """
    ## YOUR CODE HERE ##
    try:
        f = open(filename)
        f.close()
    except FileNotFoundError:
        raise FileNotFoundError('{0} does not exist'.format(filename))
    else:
        return 'File loaded'


## Question 3.1 ##

def recursive_triangle(n):
    """
    Creates a triangle structure with * characters. The triangle has n
    levels, each level has one more element than the previous. n is a
    positive integer, no validation is required.
    Parameters: n (int), positive integer
    Returns: triangle string (str)
    Restrictions. This function should be recursive.
    >>> print(recursive_triangle(1))
    *
    >>> print(recursive_triangle(2))
    *
    **
    >>> print(recursive_triangle(3))
    *
    **
    ***

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> print(recursive_triangle(4))
    *
    **
    ***
    ****
    >>> print(recursive_triangle(5))
    *
    **
    ***
    ****
    *****
    """
    ## YOUR CODE HERE ##
    if n == 0:
        return ''
    if n == 1:
        return '*'
    else:
        return recursive_triangle(n - 1) + ('\n' + '*' * n)


## Question 3.2 ##
def triangle_patterns(n, pattern_count):
    """
    Creates a triangle pattern with * characters. Each triangle has n
    levels, there are pattern_count total triangles. All inputs are
    positive integers, no input validation required.
    Parameters: n, pattern count (int), positive integers
    Returns: triangle string (str)
    Restrictions. This function should be recursive.
    >>> print(triangle_patterns(3, 1))
    *
    **
    ***
    >>> print(triangle_patterns(3, 2))
    *
    **
    ***
    ***
    **
    *
    >>> triangle_patterns(3, 3)
    '*\\n**\\n***\\n***\\n**\\n*\\n*\\n**\\n***'
    >>> triangle_patterns(3, 4)
    '*\\n**\\n***\\n***\\n**\\n*\\n*\\n**\\n***\\n***\\n**\\n*'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> triangle_patterns(2, 2)
    '*\\n**\\n**\\n*'
    >>> triangle_patterns(2, 5)
    '*\\n**\\n**\\n*\\n*\\n**\\n**\\n*\\n*\\n**'
    >>> triangle_patterns(4, 3)
    '*\\n**\\n***\\n****\\n****\\n***\\n**\\n*\\n*\\n**\\n***\\n****'
    """
    ## YOUR CODE HERE ##

    if pattern_count == 0:
        return ''
    else:
        if pattern_count % two == 0:
            return triangle_patterns(n, pattern_count - 1) + '\n' + recursive_triangle(n)[::-1]
        else:
            if pattern_count == 1:
                return recursive_triangle(n)
            else:
                return triangle_patterns(n, pattern_count - 1) + '\n' + recursive_triangle(n)


## Question 4 ##

## This question's implementation will be done in hw09_card.py

## Question 5.1 ##

def full_triangle(n, space_count=0):
    """
    Creates a triangle structure as shown in the doctests. The triangles have
    n - 1 levels. space_count is a helper variable used to help with spacing
    of the triangle. Assume n >= 2, and space_count >= 0. All inputs are
    integers. No input validation is required.
    Parameters: n, space count (int), integers. n >= 1, space_count >= 0.
    Returns: triangle string (str)
    Restrictions. You should use recursion in this question.
    >>> print(full_triangle(2)) # The smallest value we can have
    OO
    >>> print(full_triangle(3))
    -OO-
    OOOO
    >>> print(full_triangle(5))
    ---OO---
    --OOOO--
    -OOOOOO-
    OOOOOOOO
    >>> full_triangle(6)
    '----OO----\\n---OOOO---\\n--OOOOOO--\\n-OOOOOOOO-\\nOOOOOOOOOO'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> full_triangle(4)
    '--OO--\n-OOOO-\nOOOOOO'
    >>> print(full_triangle(4))
    --OO--
    -OOOO-
    OOOOOO

    """
    ## YOUR CODE HERE ##
    out = space_count * '-' + (n - 1) * 'O'
    out += out[::-1]

    if n == two:
        return out

    return full_triangle(n - 1, space_count + 1) + '\n' + out


## Question 5.2 ##

def diamond_patterns(n, pattern_count, space_count=0):
    """
    Assume n >= 2, pattern_count >= 1 and space_count >= 0. All inputs are
    integers. No assertion required.
    >>> print(diamond_patterns(2,1))
    OO
    >>> print(diamond_patterns(2,2))
    OO
    OO
    >>> print(diamond_patterns(5,1))
    ---OO---
    --OOOO--
    -OOOOOO-
    OOOOOOOO
    >>> diamond_patterns(4,2)
    '--OO--\\n-OOOO-\\nOOOOOO\\nOOOOOO\\n-OOOO-\\n--OO--'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> diamond_patterns(4,1)
    '--OO--\n-OOOO-\nOOOOOO'
    >>> print(diamond_patterns(4,3))
    --OO--
    -OOOO-
    OOOOOO
    OOOOOO
    -OOOO-
    --OO--
    --OO--
    -OOOO-
    OOOOOO
    >>> diamond_patterns(2,4)
    'OO\nOO\nOO\nOO'
    """
    ## YOUR CODE HERE ##
    if pattern_count == 1:
        return full_triangle(n, 0)

    if pattern_count % two == 0:
        return diamond_patterns(n, pattern_count - 1, space_count) + \
               '\n' + full_triangle(n, 0)[::-1]
    else:
        return diamond_patterns(n, pattern_count - 1, space_count) + '\n' + full_triangle(n, 0)
