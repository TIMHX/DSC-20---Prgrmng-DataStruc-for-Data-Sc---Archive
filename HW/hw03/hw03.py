"""
DSC 20 HW 03
NAME: XING HONG
PID: A15867895
"""

from math import isclose

## Question 1 ##


def order_scores(student_ids, student_scores, student_hours_worked):
    """
    Orders elements of student_ids, student_scores, and student_hours_worked,
    according to the contents of student_scores (descending order)

    >>> order_scores(['Work','Hard','Get','A'],[100, 80, 90, 70],[10,12,13,10])
    {'Work': (100, 10), 'Get': (90, 13), 'Hard': (80, 12), 'A': (70, 10)}
    >>> order_scores(['A1','A2','A3'],[90, 27, 56],[9,10, 6])
    {'A1': (90, 9), 'A3': (56, 6), 'A2': (27, 10)}
    >>> order_scores(['A1','A2','A3'],[90.4, 27],[9,10, 6])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> order_scores(['A1','A2','A3'],[90, 27, 80],[9,10, "hello!!"])
    Traceback (most recent call last):
    ...
    AssertionError

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> order_scores(['A1','A2','A3'],[90, 27, 80, 0],[9,10, "hello!!"])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> order_scores([1, 2, 3],[90, 27, 80, 0],[9,10, "hello!!"])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> order_scores([],[],[])
    {}
    """
    assert len(student_ids) == len(student_scores) == len(student_ids)
    dic_unsorted = {}
    dic_sorted = {}
    for i in range(len(student_ids)):
        assert type(student_ids[i]) == str
        assert type(student_scores[i]) == int
        assert type(student_hours_worked[i]) == int
        dic_unsorted[student_ids[i]] = (
            student_scores[i], student_hours_worked[i])
    sort = sorted(dic_unsorted.items(), key=lambda item: item[1], reverse=True)
    for i in sort:
        dic_sorted[i[0]] = i[1]
    return dic_sorted


## Question 2 ##

def word_length_count(book):
    """
    Returns a dictionary containing the count of each length of word
    E.g. how many words total of length 1, 2, 3...?

    This function takes in a string book, which is a file name
    string. The function reads the file with the argument string
    and returns a dictionary where the keys are the length of words
    and the values are the number of words of that length. The keys
    should be sorted in ascending order.

    >>> word_length_count('War_and_Peace_no_punc.txt')[6]
    48342
    >>> word_length_count('War_and_Peace_no_punc.txt')[15]
    254
    >>> word_length_count('War_and_Peace_no_punc.txt')[23]
    2

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> word_length_count('War_and_Peace_no_punc.txt')[8]
    29986
    >>> word_length_count('War_and_Peace_no_punc.txt')[10]
    11155
    >>> word_length_count('War_and_Peace_no_punc.txt')[20]
    8
    """
    txt = open(book, 'r', encoding='utf-8').read()
    txt = txt.lower()
    '''for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~1234567890':
        txt = txt.replace(ch, " ")'''
    words = txt.split()
    len_list = [len(i) for i in words]
    for key in len_list:
        dict[key] = dict.get(key, 0) + 1
    return dict


## Question 3 ##
filt = 3


def counting_spaces(list_of_strings):
    """
    >>> test = ["s t r i n g ", 'nospace', 'one space']
    >>> counting_spaces(test)
    [True, True, 1]

    >>> test2 = ["two spac es", "thr ee spa ces", "nospaces"]
    >>> counting_spaces(test2)
    [2, True, True]

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> test3 = [' ', '  ', '   ', '    ']
    >>> counting_spaces(test3)
    [1, 2, True, 4]

    >>> test4 = [1]
    >>> counting_spaces(test3)
    Traceback (most recent call last):
    ...
    AssertionError

    >>> test5 = 1
    >>> counting_spaces(test5)
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert type(list_of_strings) == list
    for i in list_of_strings:
        assert type(i) == str
    task_1 = [word.count(' ') for word in list_of_strings]
    task_2 = [True if i % filt == 0 else i for i in task_1]
    return task_2

## Question 4 ##


def create_trigrams(input_file, starting_words, num_words):
    """read in the input text, create a dictionary of trigrams, generate
    a new story based on the sequence of words starting a pair of words
    >>> create_trigrams("data/sherlock_small.txt", "one night", 10)
    'one night it was on the twentieth of march 1888'

    >>> create_trigrams("data/sherlock_small.txt", "i was", 10)
    'i was returning from a journey to a patient for'

    >>> create_trigrams("data/sherlock_small.txt", "Holmes Sherlock", 10)
    Traceback (most recent call last):
    ...
    AssertionError
    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> create_trigrams("data/sherlock_small.txt", "march 1888", 10)
    'march 1888 i was returning from a journey to a patient for'

    >>> create_trigrams(123, "march 1888", 10)
    Traceback (most recent call last):
    ...
    AssertionError

    >>> create_trigrams("data/sherlock_small.txt", "", 10)
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert type(input_file) == str
    assert type(starting_words) == str
    assert type(starting_words) != ''
    # I believe it's not a magic number
    assert len(starting_words.split()) == 2
    txt = open(input_file, 'r', encoding='utf-8').read()
    txt = txt.lower()
    starting_words = starting_words.lower()
    assert starting_words in txt
    assert type(num_words) == int
    for ch in '\n':
        txt = txt.replace(ch, " ")
    words = tuple(txt.split())  # list unshashable, interesting
    dict = {words[index] + ' ' + words[index + 1]: words[index + 2]
            for index in range(len(words) - 2)}  # creat dict of tri-pairs
    # To avoid key missing erro at the end
    dict[words[-2] + ' ' + words[-1]] = ''
    out_string = starting_words  # initialize the output
    for i in range(num_words):
        if len(out_string.split()) == len(words):
            break
        out_string = out_string + ' ' + \
            dict[out_string.split()[-2] + ' ' + out_string.split()[-1]]

    return out_string.rstrip()


## Question 5 ##

DELTA = 0.0001


def newton_sqrt(n):
    """
    >>> newton_sqrt(4)
    1
    >>> newton_sqrt(1)
    5
    >>> newton_sqrt(2)
    4
    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> newton_sqrt(0)
    1
    >>> newton_sqrt(200)
    7
    >>> newton_sqrt('hohoho!')
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert type(n) == int
    count = 0
    out = n / 2
    while True:
        count += 1
        if isclose(out**2, n, abs_tol=DELTA) == True:
            break
        out = 0.5 * (out + n / out)
    return count


newton_sqrt(200)
## Question 6.1 ##

B = 'O'
W = ' '


def list_to_pixel(file_path, filename):
    """
    >>> list_to_pixel("data/list0.txt","graph.txt")
    >>> with open ("graph.txt", "r") as f:
    ...     print(f.readline())
      OOOO
    <BLANKLINE>

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> with open ("graph.txt", "r") as f:
    ...     print(f.readlines())
    ['  OOOO  \n', ' OO  OO \n', 'OO    OO\n', 'O      O\n', \
     'O      O\n', 'OO    OO\n', ' OO  OO \n', '  OOOO  \n', '\n', '\n']
    """
    txt = open(file_path, 'r', encoding='utf-8').read()
    out = open(filename, 'w')
    count_newlines = txt.count('\n')  # count '\n'
    lines = txt.split()  # split by '\n'
    count_lines = len(lines)  # count number of lines
    for i in lines:
        nums = i.split(',')
        for index in range(len(nums)):
            if index % 2 == 0:
                for times in range(int(nums[index])):
                    out.write(W)
            if index % 2 == 1:
                for times in range(int(nums[index])):
                    out.write(B)
        out.write('\n')
    for i in range(count_newlines - count_lines):
        out.write('\n')

## Question 6.2 ##
line_length = 8
W = ' '
empty = ''

def pixel_to_list(pixel):
    """
    >>> pixel0="O OO OOOO OO O\\n"
    >>> pixel_to_list(pixel0)
    [[0, 1, 1, 2, 1, 4, 1, 2, 1, 1]]

    >>> with open("data/pixel_art.txt",'r') as infile:
    ...     pixel1 = infile.readlines()
    >>> pixel1 = ''.join(pixel1)
    >>> pixel_to_list(pixel1)
    [[2, 4, 2], [1, 2, 2, 2, 1], [0, 2, 4, 2], [0, 1, 6, 1], \
[0, 1, 6, 1], [0, 2, 4, 2], [1, 2, 2, 2, 1], [2, 4, 2]]

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> pixel_to_list(1)
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert type(pixel) == str
    pixel = pixel.split('\n') #split by lines
    pixel.remove(empty) #remove empty ''
    out = []
    for line in pixel:  # each lines of pixel, as a string
        count = 0  
        last_p = line[0]  # store the pixel in the previous looping
        if line[0] != W:  # start with white
            out.append(0)
        for index in range(len(line)): # each element in a line
            if line[index] == last_p: # detect changing in type
                count += 1
            else:      # if element changed type
                out.append(count)
                count = 1    # reinitial counting
            if index == len(line) - 1:  #end of a line
                out.append(count)
            last_p = line[index]
    # group counts by 8 pix per line
    grouped_out = []
    mark = 0     # mark as a start of a group
    add = 0     # sum of counts
    for index in range(len(out)):
        if add == line_length:
            grouped_out.append(out[mark:index])
            mark = index
            add = 0
        add += out[index]
        if index == len(out) - 1:
            grouped_out.append(out[mark:index + 1])
    return grouped_out

## Question 7 Extra Credit ##


def parameter_debugger(*params):
    """
    Given a list of string values representing function parameter, output a
    tuple with two items: a corrected list of parameter and a boolean value
    telling whether the list has been corrected or not.

    >>> parameter_debugger('first', 'second=30', '*third', '**fourth')
    (['first', 'second=30', '*third', '**fourth'], True)
    >>> parameter_debugger('slope', '*constants', 'intercept')
    (['slope', 'intercept', '*constants'], False)
    >>> parameter_debugger('*tutor', 'professor="Marina"', '*ta', 'me')
    (['me', 'professor="Marina"', '*tutor'], False)

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> parameter_debugger('r', 'professor="j"', '*ta', '*me')
    (['r', 'professor="j"', '*ta'], False)
    >>> parameter_debugger('r', 'r', 'r', 'r')
    (['r', 'r', 'r', 'r'], True)
    """
    para = list(params)
    normal = []
    star = []
    equal = []
    double_star = []
    out = []
    for i in para:
        if '*' in i and '**' not in i:
            star.append(i)
        if '=' in i:
            equal.append(i)
        if '**' in i:
            double_star.append(i)
        if '*' not in i and '=' not in i:
            normal.append(i)
    if normal != []:
        for i in normal:
            out.append(i)
    if equal != []:
        for i in equal:
            out.append(i)
    if star != []:
        out.append(star[0])
    if double_star != []:
        out.append(double_star[0])
    if out == para:
        bo = True
    else:
        bo = False
    return (out, bo)
