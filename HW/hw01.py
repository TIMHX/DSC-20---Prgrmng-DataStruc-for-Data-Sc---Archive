"""
TODO: This will be the module docstring; please put the description
of this module, or file, here as how it is done with the method
docstrings
"""

# Question 1


def sum_two(x, y):
    """Return the result sum of x and y
    >>> sum_two(2,-2)
    0
    >>> sum_two(-100,150)
    50
    >>> sum_two(-10, -10)
    -20
    """
    # YOUR CODE GOES HERE#
    return x + y

# Question 2


def distance(x1, y1, x2, y2):
    """Return the distance between the points (float)
    between (x1,y1) and (x2,y2)
    >>> distance(0, 0, 3, 4)
    5.0
    >>> distance(-3, -4, 3, 4  )
    10.0
    >>> distance (100, 100, 100.5, 100)
    0.5
    """
    # YOUR CODE GOES HERE#
    return float(((x1 - x2)**2 + (y1 - y2)**2))**0.5

# Question 3


def find_slope(x1, y1, x2, y2):
    """Return the slope of the line (float) between
    points (x1,y1) and (x2,y2)
    >>> find_slope(0,0,5,5)
    1.0
    >>> find_slope(0, 0, 1 , 0.5)
    0.5
    >>> find_slope(1, 1, -1, -1)
    1.0
    >>> find_slope(0, 0, 1, 2)
    2.0
    """
    # YOUR CODE GOES HERE#
    if x1 == x2:
        return "Slope undefined"
    return float((y2 - y1) / (x2 - x1))

# Question 4


def find_intercept(x1, y1, x2, y2):
    """Return y intercept of the line (float) between
    points (x1,y1) and (x2,y2)
    >>> find_intercept(0, 0, 123, 123)
    0.0
    >>> find_intercept(-22, -55, 55, 22)
    -33.0
    >>> find_intercept(-20, 20, 30, 40)
    28.0
    """
    # YOUR CODE GOES HERE#
    if x1 == x2:
        return "No intercept"
    k = float((y2 - y1) / (x2 - x1))
    return y1 - k * x1

# Question 5


def is_triangle(x1, y1, x2, y2, x3, y3):
    """Return True if points (x1,y1), (x2,y2) and (x3,y3) form a
    triangle. Returns False otherwise.
    >>> is_triangle(0, 0, 3, 0, 3, 4)
    True
    >>> is_triangle(-3, -3, 0, 0, 3, 3)
    False
    >>> is_triangle(-5, -5, 1, 2, -10, 15)
    True
    """
    # YOUR CODE GOES HERE#
    D1 = distance(x1, y1, x2, y2)
    D2 = distance(x1, y1, x3, y3)
    D3 = distance(x2, y2, x3, y3)
    Distance_list = [D1, D2, D3]
    Distance_list.sort()
    if Distance_list[0] + Distance_list[1] > Distance_list[2]:
        return True
    else:
        return False

# Question 6


def is_right_triangle(x1, y1, x2, y2, x3, y3):
    """Return True if points (x1,y1), (x2,y2) and (x3,y3)
    form a right triangle. Returns False otherwise.
    >>> is_right_triangle(0, 0, 0, 3, 4, 0)
    True
    >>> is_right_triangle(0, 0, 0, 12, 5, 0)
    True
    >>> is_right_triangle(-3, -3, 0, 0, 3, 3)
    False
    >>> is_right_triangle(0, 0, 5, 5, 10, 10)
    False
    """
    # YOUR CODE GOES HERE#
    accuracy = 3
    D1 = round(distance(x1, y1, x2, y2), accuracy)
    D2 = round(distance(x1, y1, x3, y3), accuracy)
    D3 = round(distance(x2, y2, x3, y3), accuracy)
    Distance_list = [D1, D2, D3]
    Distance_list.sort()
    if Distance_list[0]**2 + Distance_list[1]**2 == Distance_list[2]**2:
        return True
    else:
        return False

# Question 7


def is_equilateral_triangle(x1, y1, x2, y2, x3, y3):
    """Return True if points (x1,y1), (x2,y2) and (x3,y3) form a
    equilateral triangle. Returns False otherwise.
    >>> is_equilateral_triangle(2,1, 7,1 ,4.5, 5.33)
    True
    >>> is_equilateral_triangle(0, 0, 10, 0, 3, 4)
    False
    >>> is_equilateral_triangle(-5, -4, -2, -4, -3.5, -1.402)
    True
    """
    # YOUR CODE GOES HERE#
    accuracy = 3
    D1 = round(distance(x1, y1, x2, y2), accuracy)
    D2 = round(distance(x1, y1, x3, y3), accuracy)
    D3 = round(distance(x2, y2, x3, y3), accuracy)
    return (D1 == D2) and (D1 == D3)

# Question 8


def type_of_triangle(x1, y1, x2, y2, x3, y3):
    """Return the type of triangle formed by
    points (x1,y1), (x2,y2)  and (x3,y3).
    >>> type_of_triangle(-5, -4, -2, -4, -3.5, -1.402)
    'Equilateral triangle'
    >>> type_of_triangle(0, 0, 0, 3, 4, 0)
    'Right triangle'
    >>> type_of_triangle(0, 0, 0, 12, 5, 0)
    'Right triangle'
    >>> type_of_triangle( 1, 2, 3, 4, -2, 6)
    'Simple triangle'
    >>> type_of_triangle( -3, -3, 0, 0, 3, 3)
    'Not a triangle'
    """
    # YOUR CODE GOES HERE#
    if is_triangle(x1, y1, x2, y2, x3, y3):
        if is_right_triangle(x1, y1, x2, y2, x3, y3):
            return 'Right triangle'
        elif is_equilateral_triangle(x1, y1, x2, y2, x3, y3):
            return 'Equilateral triangle'
        else:
            return 'Simple triangle'
    else:
        return 'Not a triangle'

# Question 9:


def even_odd_list(lst1):
    """Return a new list indicating which replaces each
    element of lst1 with "Even" or "Odd". See the doctest
    examples for reference.
    >>> even_odd_list([1, 2, 3])
    ['Odd', 'Even', 'Odd']
    >>> even_odd_list([5, 8, 9, 10, 12])
    ['Odd', 'Even', 'Odd', 'Even', 'Even']
    >>> even_odd_list([-5, -1, -3])
    ['Odd', 'Odd', 'Odd']
    >>> even_odd_list([-2, 3, 11])
    ['Even', 'Odd', 'Odd']
    """
    # YOUR CODE GOES HERE#
    for i in range(len(lst1)):
        if lst1[i] % 2 == 0:
            lst1[i] = 'Even'
        else:
            lst1[i] = 'Odd'
    return lst1


# Question 10
def party(guests):
    """Scans the guests of the event. If the # of people who
    want to party (42's) is equal to or above 50%,
    returns "There is a party!". Otherwise returns
    "No party this time".

    >>> party([0,1,42,42,42,13,6,5])
    'No party this time'
    >>> party([0,1,42,42,42,42,6,7])
    'There is a party!'
    >>> party([0,42,6,42,42,7,66,12,13,42,42,42])
    'There is a party!'
    >>> party([0,1,42,5,6,42,42,42,5])
    'No party this time'
    """
    # YOUR CODE GOES HERE#
    count = 0
    for i in guests:
        if i == 42:
            count += 1
    if count >= len(guests) * 0.5:
        return 'There is a party!'
    else:
        return 'No party this time'
