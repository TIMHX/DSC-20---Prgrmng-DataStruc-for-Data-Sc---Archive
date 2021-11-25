"""
DSC 20 HW 06
NAME: XING HONG
PID: A15867895
"""

## Question 1.1 ##

ten = 10


def conversion_binary(n):
    """
    Converts the given base-10 number to binary representation.

    Restrictions:
    You should use recursion in this question. You should do input validation.

    Parameters:
    n (int): Number to convert

    Returns:
    (str): Binary representation of the input

    >>> conversion_binary(86)
    '1010110'
    >>> conversion_binary(1)
    '1'
    >>> conversion_binary(0)
    '0'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> conversion_binary(100)
    '1100100'
    >>> conversion_binary(15.5)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> conversion_binary(-1)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> conversion_binary(1.0)
    Traceback (most recent call last):
    ...
    AssertionError
    """
    global ten
    if type(n) != int:
        raise AssertionError
    if n < 0:
        raise AssertionError
    if n % 1 != 0:
        raise AssertionError
    if n == 0:
        return str(0)
    else:
        return str(n % 2 + ten * int(conversion_binary(int(n / 2))))


## Question 1.2 ##
def conversion_any(n, base):
    """
    Converts the given base-10 number to any base representation given by the
    base parameter. Assume that base will be 10 maximum.

    Restrictions:
    You should use recursion in this question. You should do input validation.

    Parameters:
    n (int): Number to convert
    base (int): Base to convert the number to

    Returns:
    (str): Base-x representation of the input number n

    >>> conversion_any(86, 2)
    '1010110'
    >>> conversion_any(86, 3)
    '10012'
    >>> conversion_any(86, 4)
    '1112'
    >>> conversion_any(86, 10)
    '86'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> conversion_any(71, 2)
    '1000111'
    >>> conversion_any(71, 5)
    '241'
    """
    if type(n) != int:
        raise AssertionError
    assert n > 0 and n % 1 == 0
    if n == 0:
        return str(0)
    else:
        cstring = "0123456789"
        if n < base:
            return cstring[n]
        else:
            return conversion_any(n // base, base) + cstring[n % base]


## Question 2.1 ##


def create_recursive_list(rec_count):
    """
    Returns a list with a recursive structure who has "rec_count" levels.

    Restrictions:
    You should use recursion in this question. You should do input validation.

    Parameters:
    rec_count (int): Depth of recursion in the list

    Returns:
    Recursion list specified in the question

    >>> create_recursive_list(0)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> create_recursive_list(1)
    [1]
    >>> create_recursive_list(2)
    [2, [1]]
    >>> create_recursive_list(5)
    [5, [4, [3, [2, [1]]]]]

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> create_recursive_list(1.5)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> create_recursive_list(-1)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> create_recursive_list(8)
    [8, [7, [6, [5, [4, [3, [2, [1]]]]]]]]
    """
    if type(rec_count) != int:
        raise AssertionError
    if rec_count < 0:
        raise AssertionError
    if rec_count % 1 != 0:
        raise AssertionError
    if rec_count == 0:
        raise AssertionError
    if rec_count == 1:
        return [1]
    else:
        out = [rec_count]
        out.append(create_recursive_list(rec_count - 1))
        return out


## Question 2.2 ##
def decode_recursive_list(rec_list):
    """
    Decodes a list of the recursive structure from the previous question.
    Returns a single level list containing the elements of the above list,
    in the same order.

    Restrictions:
    You should do input validation. Recursion is NOT required.

    Parameters:
    rec_list (list): Recursive list as defined in Q1.1

    Returns:
    Recursive list decoded in a normal list format

    >>> decode_recursive_list([1])
    [1]
    >>> decode_recursive_list([2, [1]])
    [2, 1]
    >>> decode_recursive_list([5, [4, [3, [2, [1]]]]])
    [5, 4, 3, 2, 1]

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> decode_recursive_list([8, [7, [6, [5, [4, [3, [2, [1]]]]]]]])
    [8, 7, 6, 5, 4, 3, 2, 1]
    >>> decode_recursive_list([])
    []
    """
    out = []
    if rec_list == []:
        return []
    if type(rec_list) != list:
        raise AssertionError
    for i in rec_list:
        if isinstance(i, list):
            out.extend(decode_recursive_list(i))
        else:
            out.append(i)
    return out


## Question 3.1 ##


def fibonacci_gen():
    """
    Yields the numbers of the Fibonacci sequence starting from F(1).

    Restrictions:
    This function should be a generator

    Returns:
    The fibonacci sequence in generator format

    >>> fibo = fibonacci_gen()
    >>> next(fibo)
    1
    >>> next(fibo)
    1
    >>> [next(fibo) for i in range(8)]
    [2, 3, 5, 8, 13, 21, 34, 55]

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> fibo = fibonacci_gen()
    >>> [next(fibo) for i in range(8)]
    [1, 1, 2, 3, 5, 8, 13, 21]
    >>> [next(fibo) for i in range(8)]
    [34, 55, 89, 144, 233, 377, 610, 987]
    """
    n, a, b = 0, 0, 1
    while True:
        yield b
        a, b = b, a + b
        n = n + 1

## Question 3.2 ##


digit = 3


def approximate_pi(n):
    """
    Returns  the nth approximation of pi according to the Leibniz series.

    Restrictions:
    You should do input validation. You should round results to the 3rd
    decimal place. You should use recursion in this question.

    Parameters:
    n (int): Represents nth approximation of pi.

    Returns:
    (float) The nth approximation of pi.

    >>> approximate_pi(1)
    4
    >>> approximate_pi(25)
    3.181
    >>> approximate_pi(50)
    3.122

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> approximate_pi(100)
    3.131
    >>> approximate_pi(-100)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> approximate_pi('kak')
    Traceback (most recent call last):
    ...
    AssertionError
    """
    global digit
    four = 4
    if type(n) != int:
        raise AssertionError
    if n <= 0:
        raise AssertionError
    Tn = (four / (2 * n - 1) * (-1)**(1 - n))
    if n == 0:
        return 0
    if n == 1:
        return four
    else:
        return round(Tn + approximate_pi(n - 1), digit)

## Question 3.3 ##


def pi_fibo_generator():
    """
    Yields the result of the current approximation of pi times the
    the current fibonacci number in their respective sequences.

    Restrictions:
    You should do input validation. You should round results to the 3rd
    decimal place.

    Returns:
    Multiplication of the nth approximation of pi and nth fibonacci number

    >>> pi_fibo = pi_fibo_generator()
    >>> [next(pi_fibo) for i in range(5)]
    [4, 2.667, 6.934, 8.688, 16.7]
    >>> [next(pi_fibo) for i in range(5)]
    [23.808, 42.692, 63.357, 110.568, 167.255]
    >>> [next(pi_fibo) for i in range(5)]
    [287.559, 440.208, 749.561, 1157.013, 1956.27]

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> pi_fibo = pi_fibo_generator()
    >>> next(pi_fibo)
    4
    >>> next(pi_fibo)
    2.667
    """
    def fibonacci_gen(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci_gen(n - 1) + fibonacci_gen(n - 2)

    def approximate_pi(n):
        """
        pi series
        """
        digit = 3
        four = 4
        if type(n) != int:
            raise AssertionError
        if n <= 0:
            raise AssertionError
        Tn = (four / (2 * n - 1) * (-1)**(1 - n))
        if n == 0:
            return 0
        if n == 1:
            return four
        else:
            return round(Tn + approximate_pi(n - 1), digit)

    n = 0
    digit = 3
    while True:
        n += 1
        out = fibonacci_gen(n) * approximate_pi(n)
        yield round(out, digit)

## Question 4 ##


def create_powerset(parent_list):
    """
    Creates the powerset of the set represented by parent_list.

    Restrictions:
    You should do input validation. You can use at most one loop (not nested).

    Parameters:
    parent_list (list): The list for which the powersets will be created

    Returns:
    (list) The powerset of list parent_list

    >>> create_powerset([])
    [[]]
    >>> create_powerset('hello')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> lst_to_return = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    >>> arg1 = create_powerset([1, 2, 3])
    >>> arg1.sort()
    >>> arg1 == lst_to_return
    True

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> lst_to_return = [[], [1], [1, 2], [2]]
    >>> arg2 = create_powerset([1, 2])
    >>> arg2.sort()
    >>> arg2 == lst_to_return
    True
    """
    if parent_list == []:
        return [[]]
    if type(parent_list) != list:
        raise AssertionError
    out = [[]]
    for x in parent_list:
        out.extend([subset + [x] for subset in out])
    return out

## Question 5.1 ##


def recursive_reverse_up_to_n(name, n):
    """
    Recursively reverses the given string at chunks 1..n

    Restrictions:
    You should use recursion. You should do input validation.

    Parameters:
    name (str): The string to be reversed
    n (int): How many times the string should be reversed

    Returns:
    (str) Reversed string with the given formula

    >>> recursive_reverse_up_to_n('Nabi', 3)
    'bNai'
    >>> recursive_reverse_up_to_n('klmn', 3)
    'mkln'
    >>> recursive_reverse_up_to_n('klmn', 4)
    'nlkm'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> recursive_reverse_up_to_n('123456', 3)
    '312456'
    >>> recursive_reverse_up_to_n('123456', 9)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> recursive_reverse_up_to_n(1, 9)
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert isinstance(name, str)
    assert isinstance(n, int)
    assert n <= len(name)
    if n == 0:
        return name
    return recursive_reverse_up_to_n(name, n - 1)[:n][::-1] + \
        recursive_reverse_up_to_n(name, n - 1)[n:]


## Question 5.2 ##


def undo_recursive_reverse_up_to_n(name, n):
    """
    Recursively corrects the recursive reverse
    done on the string up to n characters.

    Restrictions:
    You should use recursion. You should do input validation.

    Parameters:
    name (str): The string to be corrected
    n (int): How many times the string has been previously reversed

    Returns:
    (str) Corrected string

    Parameters:
    name (str): The string to be corrected
    n (int): How many times the string has been previously reversed

    Returns:
    (str) Corrected string

    >>> undo_recursive_reverse_up_to_n('bNai', 3)
    'Nabi'
    >>> undo_recursive_reverse_up_to_n('mkln', 3)
    'klmn'
    >>> undo_recursive_reverse_up_to_n('nlkm', 4)
    'klmn'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> undo_recursive_reverse_up_to_n('312456', 3)
    '123456'
    >>> undo_recursive_reverse_up_to_n('123456', 9)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> undo_recursive_reverse_up_to_n(1, 9)
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert isinstance(name, str)
    assert isinstance(n, int)
    assert n <= len(name)
    count = 0

    def helping(name, count):
        if count == n + 1:
            return name
        return helping(name, count + 1)[:count][::-1] + \
            helping(name, count + 1)[count:]
    return helping(name, count)

## Question 6 ##


def build_repr(operations, templates):
    """
    Build the representation of the series of operations with the given
    templates. The operations are prioritized from right to left.

    Restrictions:
    You should use recursion. You should do input validation.

    Parameters: operations (list(str)): List of numbers and operations to be
    executed on them

    Returns: (str): String representation of the operations

    >>> build_repr([0, '+', 1, '-', 3], {'+': '({0}, +, {1})', '-':\
    '({0}, -, {1})'})
    '(0, +, (1, -, 3))'

    >>> build_repr([0, '+', 1, '-', 3], \
    {'+': '({0}, add, {1})', '-':'({0}, minus, {1})'})
    '(0, add, (1, minus, 3))'

    >>> build_repr([0, '+', 1, '-', 3], \
    {'+': '({0}, add, {1})', '-': '({0}, minus, {1})'})
    '(0, add, (1, minus, 3))'

    ++++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW:
    ++++++++++++++++++++++++++
    >>> build_repr([1, '*', 1, '/', 3], \
    {'*': '({0}, *, {1})', '/': '({0}, /, {1})'})
    '(1, *, (1, /, 3))'
    >>> build_repr([0, '*', 1, '/', 2], \
    {'*': '({0}, times, {1})', '/': '({0}, divided_by, {1})'})
    '(0, times, (1, divided_by, 2))'
    """
    changed = []

    def changing(operations, templates):
        if len(operations) == 0:
            return changed
        if operations[0] in templates:
            changed.append(templates[operations[0]].split(',')[1].lstrip())
        else:
            changed.append(operations[0])
        return changing(operations[1:], templates)

    new_op = changing(operations, templates)

    changed = []
    right_br_count = 0

    def bracket(new_op):
        if len(new_op) == 1:
            return changed
        if isinstance(new_op[0], int):
            changed.append('(' + str(new_op[0]))
            nonlocal right_br_count
            right_br_count += 1
        else:
            changed.append(new_op[0])
        return bracket(new_op[1:])

    bracketed_op = bracket(new_op)
    bracketed_op.append(str(new_op[-1]) + right_br_count * ')')

    return ', '.join(bracketed_op)
