# Question 1


def pattern_triangle(size):
    """Returns a string that represents a triangle.
    The size depends on a passed parameter
    >>> out = pattern_triangle(2)
    >>> print(out)
    *
    **
    <BLANKLINE>

    >>> out = pattern_triangle(5)
    >>> print(out)
    *
    **
    ***
    ****
    *****
    <BLANKLINE>

    >>> out = pattern_triangle(8)
    >>> print(out)
    *
    **
    ***
    ****
    *****
    ******
    *******
    ********
    <BLANKLINE>
    """

    height = int(size)
    lst = []
    for i in range(height):
        for j in range(i + 1):
            lst.append('*')
        lst.append('\n')
    return ''.join(lst)

# Question 2


def pattern_half(n):
    """Returns a string that represents half a diamond.
    The size depends on a passed parameter
    >>> out = pattern_half(2)
    >>> print(out)
    *
    **
    *
    <BLANKLINE>

    >>> out = pattern_half(4)
    >>> print(out)
    *
    **
    ***
    ****
    ***
    **
    *
    <BLANKLINE>

    >>> out = pattern_half(5)
    >>> print(out)
    *
    **
    ***
    ****
    *****
    ****
    ***
    **
    *
    <BLANKLINE>

    """
    s = '*'
    out = []
    for i in range(1, n + 1):
        out.append((s * i).center(1))
        out.append('\n')
    for i in reversed(range(1, n)):
        out.append((s * i).center(1))
        out.append('\n')
    return ''.join(out)


# Question 3

def combine_dic(dict1, dict2):
    """Return a combined dictionary. Has the same keys as both
    dictionaries and for the same keys it should combine the values
    in the list. If the key is unique, then second value in a list
    is "Empty".
    >>> out = combine_dic({1:1, 2:2}, {2:21, 3:3})
    >>> out
    {1: [1, 'Empty'], 2: [21, 2], 3: [3, 'Empty']}

    >>> out = combine_dic({1:1}, {2:21, 3:3})
    >>> out
    {1: [1, 'Empty'], 2: [21, 'Empty'], 3: [3, 'Empty']}

    >>> out = combine_dic({1:1, 2:2}, {})
    >>> out
    {1: [1, 'Empty'], 2: [2, 'Empty']}

    >>> out = combine_dic({1:1, 2:2, 3:33}, {2:21, 3:3})
    >>> out
    {1: [1, 'Empty'], 2: [21, 2], 3: [3, 33]}

    >>> out = combine_dic({'key1':'val1', 'key2':'val2'}, {'key1':'val10'})
    >>> out
    {'key1': ['val10', 'val1'], 'key2': ['val2', 'Empty']}
    """
    out = {}

    for k in dict2.keys():
        if k not in out:
            out[k] = []
        out[k].append(dict2[k])

    for k in dict1.keys():
        if k not in out:
            out[k] = []
        out[k].append(dict1[k])
    for k in out.keys():
        if len(out[k]) == 1:
            out[k].append('Empty')
    return out

# Question 4


def dollar_amount(string):
    """Return total for the dollar amounts
    >>> dollar_amount("I have $5 dollars. I want to buy 2 toys for my kid")
    5
    >>> dollar_amount("My name is Marina. I am 20 years old")
    0
    >>> dollar_amount("Life is tough. Today I made $-100.")
    0
    >>> dollar_amount("I found $5 and $20 in my pocket.")
    25
    >>> dollar_amount("I had $10 and $100 plus $1000")
    1110
    """
    out = ['0']
    for i in range(len(string) - 1):
        if string[i + 1].isdigit():
            if string[i] != '$':
                continue
            else:
                out.append(string[i + 1])
                for x in range(i + 2, len(string)):
                    if string[x].isdigit():
                        out[-1] = out[-1] + string[x]
                    else:
                        break
    out = list(map(lambda x: int(x), out))
    return sum(out)

# Question 5


def dollar_amount_file(file):
    """
    >>> dollar_amount_file("question5_1.txt")
    97
    >>> dollar_amount_file("question5_2.txt")
    10060
    >>> dollar_amount_file("question5_3.txt")
    0
    """
    file = open(file, 'r').read()
    return dollar_amount(file)

# Question 6


def expensive_only(tup, threshold):
    """Return a tuple of lists of items whose price is higher
    than or equals to a given threshold.
    >>> expensive_only((["car",10], ["house", 15], ["laptop", 3]), 5)
    (['car', 10], ['house', 15])
    >>> expensive_only((["car",10], ["house", 15], ["laptop", 3]), 12)
    (['house', 15],)

    >>> expensive_only((["bed", 20], ["lamp", 10], ["desk", 15]), 15)
    (['bed', 20], ['desk', 15])
    >>> expensive_only((["bed", 20], ["lamp", 10], ["desk", 15]), 30)
    ()
    >>> expensive_only((), 5)
    ()
    """
    out = []
    for i in range(len(tup)):
        if tup[i][1] >= threshold:
            out.append(tup[i])
    return tuple(out)

# Question 7


def luxury_dic(tup):
    """Return a dictionary with keys as items, values as prices. 
    If an item appears more than once in a tuple, use a list to
    hold its prices. 
    >>> tup = ["car",4], ["house",6], ["laptop",8], ["laptop", 10]
    >>> new_dictionary = luxury_dic(tup)
    >>> 8 in new_dictionary['laptop']
    True
    >>> 6 in new_dictionary['car']
    False
    >>> new_dictionary['laptop'].sort()
    >>> new_dictionary['laptop']
    [8, 10]
    >>> len(new_dictionary)
    3
    """

    out = {}

    name_lst = list(map(lambda x: x[0], tup))

    for i in range(len(name_lst)):
        if name_lst[i] not in out:
            out[name_lst[i]] = []
        out[name_lst[i]].append(tup[i][1])
    return out
