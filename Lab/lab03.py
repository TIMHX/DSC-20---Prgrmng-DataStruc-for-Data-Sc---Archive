
# Question 1


def no_duplicates(*args):
    """Removes all the duplicate elements from the given list below,
    preserving the order
    >>> no_duplicates(1,2,1,2, 4, 5, 1,2)
    [1, 2, 4, 5]
    >>> no_duplicates()
    []
    >>> no_duplicates(5,4,6,1,9,0,3,9,2,7,10,8,4,7,\
    1,2,7,6,5,2,8,2,0,1,1,1,2,10,6,2)
    [5, 4, 6, 1, 9, 0, 3, 2, 7, 10, 8]
    >>> no_duplicates(5, 4, 6, 1, 9, 0, 3, 2, 7, 10, 8)
    [5, 4, 6, 1, 9, 0, 3, 2, 7, 10, 8]

    """

    # YOUR CODE IS HERE
    save_lst = []
    for i in args:
        if i not in save_lst:
            save_lst.append(i)
    return save_lst

# Question 2


def perfect_square(lst1, lst2):
    """Return a list of numbers from lst1 that have perfect squares in lst2
    >>> perfect_square([1, 2, 3], [4])
    [2]
    >>> perfect_square([1, 2, 3], [4, 4, 9, 10])
    [2, 2, 3]
    >>> perfect_square([1, 2, 3], [5, 6, 7, 10])
    []
    """
    # YOUR CODE IS HERE
    return [round(i**0.5) for i in lst2 if i**0.5 in lst1]


# Question 3


def average_rating(ratings, movie_index):
    """Return an average rating of a movie at a given index
    >>> r1=[['',"m1","m2"],["mar",7,0],["rob",3,3],["fi",1,2]]
    >>> average_rating(r1, 1)
    3.667
    >>> average_rating(r1, 2)
    1.667
    >>> r2=[['', "m1", "m2", "m2"], ["mar", 7, 4, 7],["rob", 3, 3, 8],\
    ["cat", 1, 2, 2]]
    >>> average_rating(r2, 2)
    3.0
    """

    # YOUR CODE IS HERE
    score = [i[movie_index] for i in ratings][1:]
    mean = sum(score) / len(score)
    return (round(mean, 3))


# Question 4

def write_columns(lst, fname):
    """
    Given data as a list, write three columns to fname.

    >>> lst =[5,4,6,1,9,0,3,9,2,7,10,8,4,7,1,2,7,6,\
    5,2,8,2,0,1,1,1,2,10,6,2]
    >>> write_columns(lst, "out1.txt")
    >>> with open ("out1.txt", "r") as f:
    ...     print(f.readline())
    5, 25, 6.88
    <BLANKLINE>
    >>> with open ("out1.txt", "r") as f:
    ...     lines=f.readlines()
    ...     print(lines[3])
    1, 1, 0.38
    <BLANKLINE>
    >>> print(lines[len(lines)-1])
    2, 4, 1.25
    <BLANKLINE>
    """

    # YOUR CODE IS HERE
    f = open(fname, 'w')
    for i in lst:
        f.write(str(round(i, 2)) + ', ' + str(round(i**2, 2))
                + ', ' + str(round((i / 2 + i**2) / 4, 2)) + '\n')
    f.close()


# Question 5
def my_zip(*args):
    """Return a list of tuples, like a zip method
    >>> my_zip()
    []
    >>> my_zip([1,2,3])
    [(1,), (2,), (3,)]
    >>> my_zip([1, 2, 3], ["1", "2", "3"])
    [(1, '1'), (2, '2'), (3, '3')]
    >>> my_zip([1, 2, 3], ["1", "2", "3", "4"])
    [(1, '1'), (2, '2'), (3, '3')]
    >>> my_zip([1, 2, 3, 4], ["1", "2", "3"])
    [(1, '1'), (2, '2'), (3, '3')]
    """

    # YOUR CODE IS HERE
    lst = []
    if len(args) == 0:
        return []
    elif len(args) == 1:
        for i in args[0]:
            lst.append((i,))
        return lst
    elif len(args) == 2:
        mini = min(len(args[0]), len(args[1]))
        for i in range(mini):
            lst.append((args[0][i], args[1][i]))
        return lst
