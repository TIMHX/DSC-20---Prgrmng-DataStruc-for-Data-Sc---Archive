"""
DSC 20 HW 05
NAME: XING HONG
PID: A15867895
"""

from functools import reduce

# Question 1.1:


def question1_1():
    """Return a list with answers to the True/False questions.
    >>> out = question1_1()
    >>> type(out) == list
    True
    >>> len(out)
    10
    >>> all([isinstance(i, bool) for i in out])
    True
    """
    lst = [True, False, False, True, False, False, True, True, True, True]
    return lst

# Question 1.2:


def question1_2():
    """Return a list with answers to the code complexity questions.
    >>> out = question1_2()
    >>> type(out) == list
    True
    >>> len(out)
    15
    >>> all([isinstance(i, int) and i<=7 and i>=1 for i in out])
    True
    """
    lst = [3, 6, 2, 2, 5, 5, 5, 6, 2, 2, 2, 4, 3, 3, 5]
    return lst

# Question 2.1:


zero = 0


def make_id(name, suffix):
    """Returns a netid for name with suffix n.
    >>> make_id('Marina Aleksandrovna Langlois', 17)
    'mal17'
    >>> make_id('Donald Trump', "boss")
    'dtboss'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> make_id('yo ya', "bo")
    'yybo'
    >>> make_id('I IIIIII', "IIIII")
    'iiiiiii'
    >>> make_id('oK', 0)
    'o0'
    """
    names = name.lower().split(' ')
    return ''.join([i[zero] for i in names]) + str(suffix).lower()

# Question 2.2:


def do_you_have_me(dic, item):
    """Returns a key for which item exists
    otherwise returns "Not there"
    >>> do_you_have_me({"key1":[1,2,3,4], "key2": [5,4,7,8]}, 9)
    'Not there'
    >>> do_you_have_me({"key1":[1,2,3,4], "key2": [5,4,7,8]}, 1)
    'key1'
    >>> do_you_have_me({"key1":[1,2,3,4], "key2": [5,4,7,8]}, 4)
    'key1'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> do_you_have_me({"key1":[], "key2": [5]}, 5)
    'Not there'
    >>> do_you_have_me({"key1":['richboi12345'], "key2": [5]}, 3)
    'Not there'
    """
    for i in dic.keys():
        if item in dic[i]:
            return i
        else:
            return 'Not there'


# Question 2.3:
zero = 0
one = 1
ten = 10


def read_menus(food_cat, *menus):
    """Return a string that summarized amount of items from the same category
    in the menus.
    >>> read_menus("food_cat.txt", "menu1.txt", "menu2.txt")
    'There are 7 burgers, 4 salads and 5 desserts'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> read_menus("food_cat.txt", "menu1.txt")
    'There are 4 burgers, 2 salads and 2 desserts'
    >>> read_menus("food_cat.txt", "menu2.txt")
    'There are 3 burgers, 2 salads and 3 desserts'
    """
    cat = open(food_cat, 'r').read()
    cat = cat.rstrip('\n').split('\n')
    cat2, menu, out = [], [], []
    for i in cat:
        cat2.append(i.split(': '))
    cat = cat2

    # to make a dict for category
    cat_dict = {'Burger': [], 'Salad': [], 'Dessert': []}
    for i in cat:
        for j in cat_dict.keys():
            if i[one] == j:
                cat_dict[j].append(i[zero])

    for i in menus:
        # read in menus,remove ':' and split each menu by lines
        menu.append(open(i, 'r').read().rstrip('\n').
                    replace(':', '').split('\n'))

    menu = [x for j in menu for x in j]  # join menus

    def re(x):
        # remove the numbers in menu and the space before number
        for i in range(ten):
            x = x.replace(str(i), '')
        return x.rstrip()
    menu = list(map(re, menu))

    burger, salad, dessert = 0, 0, 0

    for i in menu:
        if i in cat_dict.get("Burger"):
            burger += 1
        elif i in cat_dict.get("Salad"):
            salad += 1
        elif i in cat_dict.get("Dessert"):
            dessert += 1

    return ('There are {0} burgers, {1} salads and {2} desserts'.
            format(burger, salad, dessert))

# Question 2.4


def cuboid_coordinates(x, y, z, n):
    """
    Return a list of all possible coordinates (i, j, k)
    such that i + j + k is not equal to n.

    Restrictions: Your solution must be one line.

    >>> cuboid_coordinates(1, 1, 1, 2)
    [(0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0), (1, 1, 1)]

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> cuboid_coordinates(0, 0, 0, 2)
    [(0, 0, 0)]
    >>> cuboid_coordinates(0, 3, 0, 2)
    [(0, 0, 0), (0, 1, 0), (0, 3, 0)]
    >>> cuboid_coordinates(3, 0, 0, 2)
    [(0, 0, 0), (1, 0, 0), (3, 0, 0)]
    """
    return [(i, j, k) for i in range(x + 1) for j in range(y + 1)
            for k in range(z + 1) if i + j + k != n]

# Question 2.5


def k_mapping(inp, k):
    """
    Maps each element in the circular list to the
    element k spaces in front of it.

    >>> k_mapping([1, 2, 3, 4, 5], 2)
    '1 -> 3, 3 -> 5, 5 -> 2, 2 -> 4, 4 -> 1'
    >>> k_mapping([1, 2, 3], 3)
    '1 -> 1, 2 -> 2, 3 -> 3'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> k_mapping([1, 2, 3, 4, 5], 0)
    '1 -> 1, 2 -> 2, 3 -> 3, 4 -> 4, 5 -> 5'
    >>> k_mapping([0], 2)
    '0 -> 0'
    >>> k_mapping([1, 2, 3, 4, 5], 26)
    '1 -> 2, 2 -> 3, 3 -> 4, 4 -> 5, 5 -> 1'
    """
    if k > len(inp) - 1:
        k = k % len(inp)
    count = k
    out = []
    if count == 0:
        out = inp
    else:
        while count != 0:
            out.append(inp[count])
            count += k
            if count > len(inp) - 1:
                count -= len(inp)
        count = 1

    # help list to make map
    out2 = []
    if count != 0:
        for i in range(len(out)):
            out2.append(', ' + str(out[i]) + ' -> ')
    else:
        for i in range(len(out)):
            out2.append(str(out[i]) + ' -> ' + str(out[i]))

    if count != 0:
        # join two lists
        out3 = []
        for i in zip(out, out2):
            out3.extend(list(i))
        # change all elements to str
        for i in range(len(out3)):
            out3[i] = str(out3[i])
        return str(inp[0]) + ' -> ' + ''.join(out3) + str(inp[0])
    else:
        out3 = ', '.join(out2)
        return out3

# Question 2.6


def gcd_fraction(frac_lst):
    """
    Returns the reduced fraction made by multiplying
    fractions in frac_lst. The first element of each
    tuple represents the numerator and the second
    element represents the denominator.

    Restrictions: No loops or maps outside the gcd inner function.
    Must use reduce.

    >>> gcd_fraction([(1, 2), (3, 4), (10, 6)])
    (5, 8)

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> gcd_fraction([(9, 1)])
    (9, 1)
    >>> gcd_fraction([(9, 1), (8, 1), (1, 1)])
    (72, 1)
    >>> gcd_fraction([(9, 1), (8, 1), (1, 1),(1,3),(9,1)])
    (216, 1)
    """
    def gcd(x, y):
        """
        Find the greatest common divisor between x and y.
        """
        while y != 0:
            t = y
            y = x % y
            x = t
        return x
    out = reduce(lambda x, y: (x[0] * y[0], x[1] * y[1]), frac_lst)
    gcommon = gcd(out[0], out[1])
    out = (int(out[0] / gcommon), int(out[1] / gcommon))
    return out
