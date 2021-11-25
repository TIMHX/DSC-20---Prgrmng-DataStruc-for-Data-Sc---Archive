"""
DSC 20 HW 02
NAME: Xing Hong
PID:A1586795
"""

## Question 1 ##


def convert_1(path):
    """
    Read a file that contains pairs of name and company and convert these
    pairs to a list of tuples.

    >>> convert_1('tests/q1_test1.txt')
    [('Wesley', 'Microsoft'), ('Aaron', 'Microsoft'), ('Aaron', 'Apple'), \
('Judy', 'Microsoft'), ('Judy', 'Facebook')]
    >>> convert_1('tests/q1_test2.txt')
    [('Owen', 'TMobile'), ('Aaron', 'AT&T'), ('Wesley', 'SoftBank'), \
('Owen', 'Qualcomm'), ('Xiang', 'Qualcomm'), ('Wesley', 'AT&T'), \
('Xiang', 'SoftBank'), ('Aaron', 'TMobile')]
    >>> convert_1('tests/q1_test3.txt')
    [('David', 'Intel'), ('David', 'Amazon'), ('Judy', 'Intel'), \
('Judy', 'AMD'), ('Judy', 'Amazon'), ('Aaron', 'Amazon'), \
('Xiang', 'Amazon'), ('Wesley', 'Amazon')]
    >>> convert_1('tests/q1_test4.txt')
    [('11', '111'), ('22', '222'), ('33', '222'), ('44', '111'), \
('.dp', 'a]d')]
    >>> convert_1('tests/q1_test5.txt')
    [('&***', '(4D'), ('.d/', 'ice'), ('~/', 'ice'), ('Nanan', '""'), \
('0cp', '""')]
    >>> convert_1('tests/q1_test6.txt')
    [('...', 'you'), ('|||', 'kitty'), ('Hello', 'kitty'), ('Fuc', 'you'),
 ('No', 'offense')]
    """
    # YOUR CODE GOES HERE #
    # file = open(path, 'r')
    file = open(path, 'r')
    tup_list = [tuple(i.rstrip().split(' '))
            for i in file]
    return tup_list

## Question 2 ##


def convert_2(lst):
    """
    Convert the given list of tuples that contain pairs of names and companies
    to a dictionary that has companies as keys and names that pairs with
    these companies as values.

    >>> convert_2([('Wesley', 'Microsoft'), ('Aaron', 'Microsoft'),\
    ('Aaron', 'Apple'), ('Judy','Microsoft'), ('Judy', 'Facebook')])
    {'Microsoft': ['Wesley', 'Aaron', 'Judy'], 'Apple': ['Aaron'], \
'Facebook': ['Judy']}
    >>> convert_2([('Owen', 'TMobile'), ('Aaron', 'AT&T'), ('Wesley',\
    'SoftBank'), ('Owen', 'Qualcomm'), ('Xiang', 'Qualcomm'),\
    ('Wesley', 'AT&T'), ('Xiang', 'SoftBank'), ('Aaron', 'TMobile')])
    {'TMobile': ['Owen', 'Aaron'], 'AT&T': ['Aaron', 'Wesley'], \
'SoftBank': ['Wesley', 'Xiang'], 'Qualcomm': ['Owen', 'Xiang']}
    >>> convert_2([('David', 'Intel'), ('David', 'Amazon'), ('Judy',\
    'Intel'), ('Judy', 'AMD'), ('Judy', 'Amazon'), ('Aaron',\
    'Amazon'), ('Xiang', 'Amazon'), ('Wesley', 'Amazon')])
    {'Intel': ['David', 'Judy'], 'Amazon': ['David', 'Judy', 'Aaron', \
'Xiang', 'Wesley'], 'AMD': ['Judy']}
    >>> convert_2([('11', '111'), ('22', '222'), ('33', '222'),\
('44', '111'), ('.dp', 'a]j'))
    {'111': ['11','44'], '222': ['22','33'],'a]j': ['.dp']}
    >>> convert_2([('&***', '(4D'), ('.d/', 'ice'), ('~/', 'ice'),\
('Nanan', '""'), ('0cp', '""')])
    {'(4D': ['&***'], 'ice': ['.d/', '~/'], '""': ['Nanan', '0cp']}
    >>> convert_2([('...', 'you'), ('|||' , 'kitty'), ('Hello' , 'kitty'),\
('Fuc', 'you'), ('No','offense')])
    {'you': ['...', 'Fuc'], 'kitty': ['|||', 'Hello'], 'offense': ['No']}
    """
    # YOUR CODE GOES HERE #
    dic_list = {}
    for i in lst:
        if i[1] not in dic_list:
            dic_list[i[1]] = []
        dic_list[i[1]].append(i[0])
    return dic_list


## Question 3 ##

MAX_N = 9


def multiplication_chart(n):
    """
    Create a triangle multiplication chart with given size. n will be
    positive integers only. If 1 <= n <= 9, create the chart normally.
    If n > 9, add a notice before creating a chart with n = 9.
    See the write-up for detailed description.

    >>> print(multiplication_chart(3))
    01
    02  04
    03  06  09
    >>> print(multiplication_chart(6))
    01
    02  04
    03  06  09
    04  08  12  16
    05  10  15  20  25
    06  12  18  24  30  36
    >>> print(multiplication_chart(10))
    n = 10 is too hard for me! Why not have n = 9?
    01
    02  04
    03  06  09
    04  08  12  16
    05  10  15  20  25
    06  12  18  24  30  36
    07  14  21  28  35  42  49
    08  16  24  32  40  48  56  64
    09  18  27  36  45  54  63  72  81
    >>> print(multiplication_chart(11))
    n = 11 is too hard for me! Why not have n = 9?
    01
    02  04
    03  06  09
    04  08  12  16
    05  10  15  20  25
    06  12  18  24  30  36
    07  14  21  28  35  42  49
    08  16  24  32  40  48  56  64
    09  18  27  36  45  54  63  72  81
    >>> print(multiplication_chart(1))
    01
    """
    # YOUR CODE GOES HERE #
    num_list = []
    if n > MAX_N:
        Erro = ("n = {} is too hard for me! \
        Why not have n = 9?\n".format(n))
        n = 9
    else:
        Erro = ""
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if i != j:
                if i * j > 9:
                    num_list.append\
                    (str(i * j) + " ")
                else:
                    num_list.append\
                    ("0" + str(i * j) + " ")
            else:
                if i * j > 9:
                    num_list.append\
                    (str(i * j) + "\n")
                else:
                    num_list.append\
                    ("0" + str(i * j) + "\n")
    return Erro + "".join(num_list)


## Question 4 ##


def encrypt(s):
    """
    Encrypt the string by capitalizing all letters, applying Atbash cipher,
    and reverse the string. See the write-up for detailed description.

    >>> encrypt('ABCDefg, HIJKlmn, opqRST, uvwXYZ')
    'ABCDEF ,GHIJKL ,MNOPQRS ,TUVWXYZ'
    >>> encrypt('encrypt encrypt?')
    '?GKBIXMV GKBIXMV'
    >>> encrypt('CsE BaSeMeNt >.<')
    '<.> GMVNVHZY VHX'
    >>> encrypt('[]][][][]9i]')
    ']R9][][][]]['
    >>> encrypt('+++++deo 44jd')
    'WQ44 LVW+++++'
    >>> encrypt('?????????OHHHH Yah')
    'SZB SSSSL?????????'
    """

    # YOUR CODE GOES HERE #
    s = s[::-1].upper()
    cypher_dic = {'A': 'Z', 'B': 'Y', 'C': 'X',
              'D': 'W', 'E': 'V', 'F': 'U', 'G': 'T',
              'H': 'S', 'I': 'R', 'J': 'Q', 'K': 'P',
              'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L',
              'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H',
              'T': 'G', 'U': 'F', 'V': 'E', 'W': 'D',
              'X': 'C', 'Y': 'B', 'Z': 'A'}

    answer = ''
    for i in s:
        if(i.isalpha() == False):
            answer += i
        else:
            answer += cypher_dic[i]
    return answer


## Question 5 ##

def sum_some(lst1, num):
    """
    Splits lst1 into subgroups of (equal) size num, and
    sums the contents of each subgroup.
    Returns the individual sums in a new list.
    If splitting can't be done properly, returns "split not valid"

    >>> sum_some([1, 2, 3, 4, 5, 6], 2)
    [3, 7, 11]
    >>> sum_some([1, 2, 3, 4, 5, 6], 3)
    [6, 15]
    >>> sum_some([1,2,3,4,5,6,7], 3)
    'split not valid'
    >>> sum_some([1,2], 3)
    'split not valid'
    >>> sum_some([9999,9999,0,0], 4)
    [9999, 9999, 0, 0]
    >>> sum_some([9999,9999,0,0], 1)
    19998
    >>> sum_some([],4)
    []
    """
    # YOUR CODE GOES HERE #
    out = []
    if len(lst1) == num:
        return lst1
    elif num == 1:
        return sum(lst1)
    elif len(lst1) % num == 0:
        for i in range(0, len(lst1), num):
            out.append(sum(lst1[i:i + num]))
        return out
    else:
        return "split not valid"

## Question 6 ##


def subset(lst1, lst2):
    """
    Returns True if lst1 is a subset of lst2. Returns False otherwise.

    >>> subset([1,2], [1,2,3])
    True
    >>> subset([1,2,3,4], [1,2,3])
    False
    >>> subset([], [1])
    True
    >>> subset([1,2,3], [1,2,3])
    True
    >>> subset([1], [])
    False
    >>> subset([], [])
    True
    >>> subset(["lalal"], ["lalal"])
    True
    >>> subset(["lalal"], ["lalal",123])
    True
    """
    # YOUR CODE GOES HERE #
    return set(lst1).issubset(lst2)
