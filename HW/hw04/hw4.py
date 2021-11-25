"""
DSC 20 HW 04
NAME: XING HONG
PID: A15867895
"""

from math import factorial
from math import floor

## Question 1 ##
prime = 2

def prime_number_generator(number_of_primes):
    """
    Generator for creating the first 'number_of_primes' prime numbers
    using the prime number formula based on Wilson's theorem

    Restrictions:
    You should use a generator in this question.

    Parameters:
    number_of_primes (int): Number of primes to be generated

    Returns:
    The required generator of the question.

    >>> prime_gen = prime_number_generator(2)
    >>> next(prime_gen)
    2
    >>> list(prime_number_generator(10))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    >>> prime_gen = prime_number_generator(20)
    >>> list(prime_gen)[10:20]
    [31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> list(prime_number_generator(20))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, /
    53, 59, 61, 67, 71]
    >>> list(prime_number_generator(0))
    [None]
    """
    n , count= prime, 0
    if number_of_primes != 0:
        yield prime
    else:
        yield
    while count < number_of_primes-1:
        out = floor(factorial(n) % (n+1)/n)*(n-1) + 2
        n += 1
        if out != prime:
            yield out
            count += 1
        if out != prime:
            continue
    
    
## Question 2.1 ##
def exp_gen(n, e):
    """A generator that yields the following exponentials
    (given n, e as inputs):
    n**e, (n*e)**e, (n*e*e)**e, (n*e*e*e)**e, ... (and so on)
    >>> gen = exp_gen(2,2)
    >>> next(gen)
    4
    >>> next(gen)
    16
    >>> next(gen)
    64
    >>> next(gen)
    256

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> gen = exp_gen(3,2)
    >>> list(gen)[0:10]
    256
    >>> next(gen)
    9
    >>> next(gen)
    36
    >>> next(gen)
    144
    
    """
    count, original_n= 0, n
    while True:
        n = original_n
        n = n*(e**count)
        yield n**e
        count += 1    

## Question 2.2 ##
two = 2
one = 1

def luc_seq():
    """A generator that yields the Lucas Sequence
    >>> gen = luc_seq()
    >>> next(gen)
    2
    >>> next(gen)
    1
    >>> next(gen)
    3

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> gen = luc_seq()
    >>> for i in range(10):
    ... print(next(gen))
    2
    1
    3
    4
    7
    11
    18
    29
    47
    76
    """
    num_list = []
    n = 0
    while True:
        if n == 0:
            yield two
            num_list.append(2)
        if n == one:
            yield one
            num_list.append(1)
        if n > one:
            number = num_list[n-1] + num_list[n-2]
            yield number
            num_list.append(number)
        n += 1

## Question 2.3 ##
def alpha_gen(stars_count, word):
    """Return a function that creates a generator that yields a
    letter from a given string with a specified number of stars between
    each letter.

    >>> alpha_gen = alpha_gen(2, "marina")
    >>> next(alpha_gen)
    'm'
    >>> next(alpha_gen)
    '*'
    >>> next(alpha_gen)
    '*'
    >>> for i in alpha_gen:
    ... 	print(i, end='')
    a**r**i**n**a**

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> alpha_gen = alpha_gen(0, "yoyobro")
    >>> next(alpha_gen)
    'y'
    >>> next(alpha_gen)
    'o'
    >>> for i in alpha_gen:
    ... 	print(i, end='')
    yobro
    """
    lst = []
    for i in word:
        lst.append(i+stars_count * '*')
    for i in ''.join(lst):
        yield i


## Question 2.4 ##
def generate_generators():
    """
    Return a generator that yields the previous three generators.
    First Yield:  exp_gen
    Second Yield: luc_seq
    Third Yield:  alpha_gen

    >>> gen_list = generate_generators()
    >>> exp_gnr = next(gen_list)
    >>> lucas_gnr = next(gen_list)
    >>> alpha_func = next(gen_list)
    >>> func1 = exp_gnr(2,2)
    >>> next(func1)
    4
    >>> next(func1)
    16
    >>> next(func1)
    64
    >>> next(lucas_gnr)
    2
    >>> next(lucas_gnr)
    1
    >>> next(lucas_gnr)
    3
    >>> alpha_gen = alpha_func(2, "marina")
    >>> next(alpha_gen)
    'm'
    >>> next(alpha_gen)
    '*'
    >>> next(alpha_gen)
    '*'
    >>> for i in alpha_gen:
    ... 	print(i, end='')
    a**r**i**n**a**

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> gen_list = generate_generators()
    >>> exp_gnr = next(gen_list)
    >>> lucas_gnr = next(gen_list)
    >>> alpha_func = next(gen_list)
    >>> func1 = exp_gnr(3,2)
    >>> next(func1)
    9
    >>> next(func1)
    36
    >>> next(func1)
    144
    >>> next(lucas_gnr)
    2
    >>> next(lucas_gnr)
    1
    >>> next(lucas_gnr)
    3
    >>> alpha_gen = alpha_func(2, "yoyo")
    >>> next(alpha_gen)
    'y'
    >>> next(alpha_gen)
    '*'
    >>> next(alpha_gen)
    '*'
    >>> for i in alpha_gen:
    ... 	print(i, end='')
    y**o**y**o**
    """
    def exp_gen(n, e):
        count, original_n= 0, n
        while True:
            n = original_n
            n = n*(e**count)
            yield n**e
            count += 1
    
    two = 2
    one = 1

    def luc_seq():
        num_list = []
        num = 0
        while True:
            if num == 0:
                yield two
                num_list.append(2)
            if num == one:
                yield one
                num_list.append(1)
            if num > one:
                number = num_list[n-1] + num_list[n-2]
                yield number
                num_list.append(number)
            num += 1
            
    def alpha_gen(stars_count, word):
        lst = []
        for i in word:
            lst.append(i+stars_count * '*')
        for i in ''.join(lst):
            yield i
            
    fuc_lst = [exp_gen,luc_seq,alpha_gen]
    for i in fuc_lst:
        yield i

    
## Question 3 ##
def get_negative_lists(super_list):
    """
    Return a map object containing the lists in the
    super list that contain negative numbers.

    Restrictions:
    No loops (Not even list comprehension!)

    Parameters:
    super_list (list): A list containing sublists of integers

    Returns:
    The map required by the question.

    >>> subLsts = [[1, 5, 2, 8, 4], [-900, -22, 33, -90, 529],\
[0, -2, 5, -199, 300]]
    >>> isinstance(type(get_negative_lists(subLsts)), type(map))
    True
    >>> list(get_negative_lists(subLsts))
    [[-900, -22, 33, -90, 529], [0, -2, 5, -199, 300]]
    >>> subLsts = [[7, 2, -1, -6, -100], [-1, 0, 5, 2, 3], [0, 0, 1, 0, 0]]
    >>> list(get_negative_lists(subLsts))
    [[7, 2, -1, -6, -100], [-1, 0, 5, 2, 3]]

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> subLsts = [[-1], [-1, 0, 5, 2, 3], [0, 0, -1, 0, 0]]
    >>>> list(get_negative_lists(subLsts))
    [[-1], [-1, 0, 5, 2, 3], [0, 0, -1, 0, 0]]
    isinstance(type(get_negative_lists(subLsts)), type(map))
    """
    def filt_neg(x):
        if x == []:
            return True
        if True in x:
            return False
        else:
            return True
            
    return filter(filt_neg, super_list)

    
## Question 4 ##
def get_distances():
    """
    Return a list of lambdas that help do bulk distance calculations on city
    coordinates.
    1: Define a function that converts miles to km, with miles as the input.
    2: Define a function that determines the distance between two points that
       use (x, y) coordinates as inputs
    3: Determine how many kilometers are between Point A(424.3601, 71.0589)
       and Point B (-3601.1128, 493.4276)
    4: Return a lambda that returns a map object of the distances between a
       list of tuple pairs of cities.


    >>> cities = [(424.3601, 71.0589), (-3601.1128, 493.4276), \
(158.1010, 8179.001), (-119.030, -117.334)]
    >>> lambda_functions = get_distances()
    >>> lambda_functions[0](1000)
    1609.344
    >>> lambda_functions[1](cities[0][0], cities[0][1],\
cities[1][0], cities[1][1])
    4047.5705537240606
    >>> lambda_functions[2]((cities[0], cities[1]))
    6513.933385212495
    >>> list(lambda_functions[3]([(cities[0], cities[1]),\
(cities[2], cities[3])]))
    [6513.933385212495, 13359.103960657963]

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> cities = [(0, 0), (1, 1), \
(-1, -1), (1, 1)]
    >>> lambda_functions = get_distances()
    >>> lambda_functions[0](1000)
    1609.344
    >>> lambda_functions[1](cities[0][0], cities[0][1],\
cities[1][0], cities[1][1])
    1.4142135623730951
    >>> lambda_functions[2]((cities[0], cities[1]))
    2.2759561113237665
    >>> list(lambda_functions[3]([(cities[0], cities[1]),\
(cities[2], cities[3])]))
    [2.2759561113237665, 4.551912222647533]
    """
    lst = [lambda x: x*1.609344, lambda x,y,z,s: ((x-z)**2+(y-s)**2)** \
    0.5, lambda x: ((x[0][0]-x[1][0])**2 + (x[0][1]-x[1][1])**2)**0.5* \
    1.609344, lambda x: [((x[0][0][0]-x[0][1][0])**2 + (x[0][0][1]- \
    x[0][1][1])**2)**0.5 *1.609344, ((x[1][0][0]-x[1][1][0])**2 + \
    (x[1][0][1]- x[1][1][1])**2)**0.5 *1.609344]] 
    return lst


## Question 5 ##
def calculate_wages(filepath):
    """
    Calculator for tutor wages. See question description for explanation.

    Restrictions:
    No loops (Not even list comprehension!)

    Parameters:
    filepath (str): Path to the input file

    Returns:
    dict: Dictionary of tutor names and their total wages

    >>> calculate_wages('data/input.txt')
    {'Judy': 8, 'Owen': 40, 'Xiang': 460}

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> calculate_wages('data/input.txt')
    {'Judy': 8, 'Owen': 40, 'Xiang': 460}
    >>> calculate_wages('data/input.txt').items()
    dict_items([('Judy', 8), ('Owen', 40), ('Xiang', 460)])
    >>> calculate_wages('data/input.txt').keys()
    dict_keys(['Judy', 'Owen', 'Xiang'])
    """
    file = open(filepath, 'r').read()
    person = file.rstrip().split('\n')
    def to_lst(x):
        return x.split(', ')
    person = list(map(to_lst,person))
    
    def value(x):
        return [x[0],int(x[1]),int(x[2]),int(x[3])]
    value_lst = list(map(value,person))
    
    def cal(x):
        def cal_person(i):
            if i <= 5:
                return 0
            elif i > 5 and i <= 10:
                return (i - 5) * 8
            elif i > 10:
                return (i - 10) * 12 + 5*8
        return list(map(cal_person,x[1:]))
    value_lst = list(map(sum,list(map(cal,value_lst))))
        
    def get_name(x):
        return x[0]
    name_lst = list(map(get_name,person))
    
    out = dict(zip(name_lst, value_lst))
    
    return out
    
## Question 6 ##
def calculate_best_scores(formulas, scores):
    """
    Calculates the maximum score achievable with the provided formulas.

    Restrictions:
    No loops (Not even list comprehension!)

    Parameters:
    formulas (list(lambda)) : List of lambda functions to be applied to scores
    scores (list(int)) : List of integers indicating the scores for students

    Returns:
    list : List of scores with the function that maximizes each score applied
    to it

    >>> calculate_best_scores([lambda x : x - 1], [3, 4, 5])
    [3, 4, 5]
    >>> calculate_best_scores([lambda x : x + 1], [3, 4, 5])
    [4, 5, 6]
    >>> calculate_best_scores([lambda x : x + 1, lambda x : x * 2,\
lambda x : x - 1], [3, 4, 5])
    [6, 8, 10]
    >>> calculate_best_scores([lambda x : x + 20, lambda x : x * 2,\
lambda x : x * 3], [3, 4, 20])
    [23, 24, 60]
    >>> calculate_best_scores([lambda x : x + 20, 123], [3, 4, 5])
    [23, 24, 25]
    
    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> calculate_best_scores([lambda x : x**2, lambda x : x/2,\
    lambda x : x/3], [3, 4, 20])
    [9, 16, 400]
    >>> calculate_best_scores([lambda x : x, lambda x : x,\
    lambda x : x], ['3', 4, 20])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> calculate_best_scores([123, lambda x : x*2,\
    lambda x : x], [3, 4, 20])
    [6, 8, 40]
    """
    func_lst = list(filter(callable,formulas))
    func_lst.append(lambda x:x)
    score_lst = list(filter(lambda x: type(x)==int, scores))
    assert len(score_lst) == len(scores)
    
    out = lambda x: max(list(map(lambda f: f(x), func_lst)))
    
    return list(map(out,scores))

## Question 7 ##
def best_champ(champion_dict):
    """
    Returns a dictionary of champions and calculated scores.

    Restrictions:
    No loops (Not even list comprehension!)

    Parameters:
    champion_dict: a dictionary of champions and K/D/A slash lines

    Returns:
    dict: a dictionary of champions and scores

    >>> champ_dict = {'Lucian': '20/7/8', 'Caitlyn': '2/8/4', \
'Kha\'Zix': '0/19/2'}
    >>> best_champ(champ_dict)
    {'Lucian': 77.0, 'Caitlyn': -2.0, "Kha'Zix": -8.5}

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> champ_dict = {'po': '20/7/8', 'pa': '2/8/4', \
'pe': '0/19/2'} 
    >>> best_champ(champ_dict)
    {'po': 77.0, 'pa': -2.0, 'pe': -8.5}
    """
    func_lst = [lambda x: x*2 if x<10 else x*4, \
                lambda x: x*(-1) if x<10 else x*(-0.5), \
                lambda x: x*0.5]
    name_lst = list(champion_dict.keys())
    num_lst = list(champion_dict.values())
    num_lst = list(map(lambda x: x.split('/'),num_lst))
    
    def cal(x):
        def to_int(x):
            return int(x)
        return list(map(to_int,x))
    value_lst = list(map(cal,num_lst))
    value_lst
    def cal_value(x):
        return [func_lst[0](x[0]),func_lst[1](x[1]),func_lst[2](x[2])]
    value_lst = list(map(cal_value,value_lst))
    value_lst = list(map(sum,value_lst))

    return dict(zip(name_lst, value_lst))

## Question 8 ## (Extra Credit)
def find_positive_magic_integer(filepath):
    """
    Find any positive magic integers in the given file and output a dictionary
    whose keys are the string value of the found magic numbers and values
    are the line numbers where they were found.

    Parameters:
    filepath (str): A string containing the filepath.

    Returns:
    The dictionary described above.

    >>> find_positive_magic_integer('./data/magic_number_test1.py')
    {'2': [3, 11], '3': [4, 11], '4': [5, 11], '5': [6, 11], '6': [7, 11], \
'7': [8, 11], '8': [9, 11], '9': [10, 11]}
    >>> find_positive_magic_integer('./data/magic_number_test2.py')
    {'2': [4, 5], '3': [4, 6], '20': [7], '5': [8]}

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++

    """
