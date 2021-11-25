# Question 1
def question1(num_list):
    """
    >>> question1([1,2,3,4,5,6,7,8,9,10])
    2 4 6 8 10
    >>> result = question1([1,3,5,7,9])
    >>> print(result)
    None
    >>> question1([1,3,5,7,9, 0])
    0
    """
    if len(num_list) == 0:
        return
    if num_list[0] % 2 == 0:
        print(num_list[0], end=' ')
    question1(num_list[1:])


# Question 2
count = 0


def question2(words_list):
    """ Counts the number of "SOS" occurrences in a list
    >>> question2(["SOS", "Not SOS", "SOS", "Not SOS"])
    2
    >>> question2(["SOS", "Alarm", "Help"])
    1
    >>> question2(["Alarm", "Help", "Fire", "Not SOS"])
    0
    >>> question2(["SOS", "SOS", "SOS", "SOS"])
    4
    >>> question2([])
    0
    """
    global count
    if len(words_list) == 1:
        if words_list[0] == 'SOS':
            count += 1
        out, count = count, 0
        return out
    if len(words_list) == 0:
        return count
    else:
        if words_list[0] == 'SOS':
            count += 1
        return question2(words_list[1:])


# Question 3
count = 0


def question3(number):
    """
    >>> question3(123456)
    21
    >>> question3(123)
    6
    >>> question3(123908)
    23
    >>> question3(5)
    5
    """
    global count
    count += number % 10
    if number < 10:
        out, count = count, 0
        return out
    return question3(number // 10)


# Question 4
outer = []


def question4(string):
    """
    >>> question4("Recursion is cool.")
    'Recursion is cool'
    >>> question4("M.A.R.I.N.A.")
    'MARINA'
    >>> question4("No dots here!")
    'No dots here!'
    """
    global outer
    if len(string) == 0:
        out, outer = outer, []
        return ''.join(out)
    if string[0] != '.':
        outer.append(string[0])
    return question4(string[1:])

# Question 5


def question5(number):
    """
    >>> question5(1181)
    4
    >>> question5(181)
    2
    >>> question5(11911)
    6
    >>> question5(111111)
    11
    """
    if number == 0:
        return 0
    if number % 10 == 1:
        if number // 10 % 10 == 1:
            return 2 + question5(number // 10)
        return 1 + question5(number // 10)
    return question5(number // 10)

# Question 6


def hailstone(n):
    """Print the hailstone sequence starting at n and return its length.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(int(n))
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n / 2)
    else:
        return 1 + hailstone(3 * n + 1)


# Question 7
out = []


def question7(int1, int2):
    """
    >>> question7(8, 1)
    '8 7 6 5 4 3 2 1'
    >>> question7(1, -1)
    '1 0 -1'
    >>> question7(10, 10)
    '10'
    """
    global out
    out.append(int1)
    if int1 == int2:
        out = []
        return str(int1)
    if int1 - 1 != int2:
        return question7(int1 - 1, int2)
    out.append(int2)
    new_out = [str(x) for x in out]
    out = []
    string = ' '.join(new_out)
    return string

# Question 8
out = []


def question8(int1, int2):
    """
    >>> question8(8, 1)
    '8 7 6 5 4 3 2 1'
    >>> question8(1, -1)
    '1 0 -1'
    >>> question8(10, 10)
    '10'
    >>> question8(1, 8)
    '1 2 3 4 5 6 7 8'
    >>> question8(-1, 1)
    '-1 0 1'
    """
    global out
    out.append(int1)
    if int1 == int2:
        out = []
        return str(int1)
    if int1 > int2:
        if int1 - 1 != int2:
            return question8(int1 - 1, int2)
        out.append(int2)
        new_out = [str(x) for x in out]
        out = []
        string = ' '.join(new_out)
        return string
    elif int1 < int2:
        if int1 + 1 != int2:
            return question8(int1 + 1, int2)
        out.append(int2)
        new_out = [str(x) for x in out]
        out = []
        string = ' '.join(new_out)
        return string
