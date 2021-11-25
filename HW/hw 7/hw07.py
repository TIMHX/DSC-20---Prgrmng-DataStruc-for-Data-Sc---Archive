"""
DSC 20 HW 07
NAME: XING HONG
PID: A15867895
"""

## Question 1.1 ##
four = 4


def populate_menu_schedule(menu_schedule, recipe_dict):
    """
    Populate the given menu_schedule with recipes based on recipe_dict

    Parameters:
    menu_schedule (tuple): A tuple with five dictionaries representing the menu
    recipe_dict (dict): A dictionary of food recipe

    Returns:
    (None)

    >>> menu_schedule = ( \
            {"Orange Chicken": [], "Broccoli Beef": []}, \
            {"Broccoli Beef": []}, \
            {"Orange Chicken": [], "Spring Roll": []}, \
            {"Fortune Cookie": []}, \
            {"Fortune Cookie": [], "Broccoli Beef": []} \
        )
    >>> recipe_dict = { \
                "Orange Chicken": ["Orange", "Chicken"], \
                "Fortune Cookie": ["Fortune", "Cookie", "Paper"], \
                "Spring Roll": ["Egg"] \
        }
    >>> populate_menu_schedule(menu_schedule, recipe_dict)
    >>> menu_schedule
    ({'Orange Chicken': ['Orange', 'Chicken']}, {}, {'Orange Chicken': \
['Orange', 'Chicken'], 'Spring Roll': ['Egg']}, {'Fortune Cookie': \
['Fortune', 'Cookie', 'Paper']}, {'Orange Chicken': ['Orange', 'Chicken']})
    >>> menu_schedule[0]['Orange Chicken'].append("Hot Sauce")
    >>> menu_schedule[2]['Orange Chicken']
    ['Orange', 'Chicken', 'Hot Sauce']
    >>> menu_schedule[0]['Gyro Plate'] = ['Beef']
    >>> menu_schedule[0]
    {'Orange Chicken': ['Orange', 'Chicken', 'Hot Sauce'], 'Gyro Plate': \
['Beef']}
    >>> menu_schedule[4]
    {'Orange Chicken': ['Orange', 'Chicken', 'Hot Sauce']}
    """
    # YOUR CODE STARTS HERE #
    # remove that not in recipe
    for day in menu_schedule:
        for name in list(day):
            if name not in recipe_dict.keys():
                del day[name]
            else:
                day[name] = recipe_dict[name]

    # rewrite mon&fri
    menu_schedule[four].clear()
    menu_schedule[four].update(menu_schedule[0])


## Question 1.2 ##

def dereference_recipes(menu_schedule):
    """
    Dereference all pairs of recipe that refers to the same recipe object

    Parameters:
    menu_schedule (tuple): A tuple with five dictionaries representing the menu
        whose recipes have been already populated

    Returns:
    (None)

    >>> menu_schedule = ( \
            {"Orange Chicken": [], "Broccoli Beef": []}, \
            {}, \
            {}, \
            {}, \
            {"Orange Chicken": [], "Broccoli Beef": []} \
        )
    >>> oc_recipe = ['Orange', 'Chicken']
    >>> bb_recipe = ['Love']
    >>> menu_schedule[0]["Orange Chicken"] = oc_recipe
    >>> menu_schedule[4]["Orange Chicken"] = oc_recipe
    >>> menu_schedule[0]["Broccoli Beef"] = bb_recipe
    >>> menu_schedule[4]["Broccoli Beef"] = bb_recipe
    >>> menu_schedule[4]["Broccoli Beef"].append('Peace')
    >>> dereference_recipes(menu_schedule)
    >>> menu_schedule[4]["Broccoli Beef"].remove('Peace')
    >>> menu_schedule[0]["Broccoli Beef"]
    ['Love', 'Peace']
    """
    # YOUR CODE STARTS HERE #
    four = 4
    # remove that not in recipe
    for day in menu_schedule:
        for name in list(day):
            day[name] = day[name].copy()


## Question 2 is in hw07_OOP.py ##

## Question 3.1 ##
def create_palindrome_v1(start, end):
    """
    Creates a palindrome of integers starting from start, ending at end
    (in the middle) All inputs are positive integers. No input validation
    required.
    Parameters: start, end (int), positive integers
    Returns: palindrome sequence (str)
    Restrictions. You should use recursion in this question.
    >>> create_palindrome_v1(1, 1)
    '1'
    >>> create_palindrome_v1(3, 5)
    '34543'
    >>> create_palindrome_v1(5, 2)
    '5432345'
    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> create_palindrome_v1(9, 2)   
    '987654323456789'
    >>> create_palindrome_v1(0, 0)
    '0'
    >>> create_palindrome_v1(3, 0)
    '3210123'
    """
    # YOUR CODE STARTS HERE #
    if start == end:
        return str(start)
    # backward
    if start >= end:
        n = -1
    else:
        n = 1
    return str(start) + str(create_palindrome_v1(start + n, end)) + str(start)


## Question 3.2 ##

def create_palindrome_v2(start1, end1, start2, end2):
    """
    Creates a two level palindrome of integers. The first level (outer level)
    starts from start1 and ends at end1. The second level (inner level) starts
    from start2 and end2. No input validation is required.
    Parameters: start1, end1, start2, end2 (int), positive integers
    Returns: palindrome sequence (str)
    Restrictions. You should use recursion in this question.
    >>> create_palindrome_v2(1, 1, 1, 1)
    '1_1_1'
    >>> create_palindrome_v2(2, 5, 5, 4)
    '2345_545_5432'
    >>> create_palindrome_v2(3, 1, 5, 9)
    '321_567898765_123'
    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> create_palindrome_v2(0, 5, 5, 9)
    '012345_567898765_543210'
    >>> create_palindrome_v2(0, 0, 5, 9)
    '0_567898765_0'
    >>> create_palindrome_v2(0, 0, 3, 9)
    '0_3456789876543_0'
    """
    # YOUR CODE STARTS HERE #
    if start1 == end1:  # base
        if end1 == -1 and start1 == -1:
            if start2 == end2:
                return start2
            # count
            if start2 >= end2:
                n = -1
            else:
                n = 1
            return str(start2) + str(create_palindrome_v2(-1, -1, start2 + n, end2)) + \
                str(start2)

        else:  # cur 1
            # set underscore
            return str(start1) + '_' + str(create_palindrome_v2(-1, -1, start2, end2)) + \
                '_' + str(start1)
    # count
    if start1 >= end1:
        n = -1
    else:
        n = 1
    return str(start1) + str(create_palindrome_v2(start1 + n, end1, start2, end2)) + \
        str(start1)
