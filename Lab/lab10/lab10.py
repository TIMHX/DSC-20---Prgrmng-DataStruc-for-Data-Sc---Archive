import numpy as np

# 1 Sets (simple)
def common_letters(input1, input2):
    """
    >>> common_letters("marina", "langlois")
    'The common letters are: a i n'

    >>> common_letters("turkey", "gravy")
    'The common letters are: r y'

    >>> common_letters("cat", "dog")
    'There are no common letters'
    """
    # YOUR CODE HERE #
    set1 = set(list(input1))
    set2 = set(list(input2))
    lst3 = list(set1 & set2)
    lst3.sort()
    if len(lst3) == 0:
        return 'There are no common letters'
    else:
        return 'The common letters are: ' + ' '.join(lst3)


# 2 Sets
def common_words(file1, file2):
    """
    >>> common_words("file1.txt", "file4.txt")
    'File does not exist'
    
    >>> common_words("file1.txt", "file2.txt")
    'The common words are: Today World! a is'

    >>> common_words("file2.txt", "file3.txt")
    'The common words are: Goodbye, rainy'

    >>> common_words("file1.txt", "file3.txt")
    'There are no common words'
    """
    # YOUR CODE HERE #
    try:
        f1 = open(file1).read()
        f2 = open(file2).read()
    except:
        return 'File does not exist'
    set1 = set(f1.split())
    set2 = set(f2.split())
    lst3 = list(set1 & set2)
    lst3.sort()
    if len(lst3) == 0:
        return 'There are no common words'
    else:
        return 'The common words are: ' + ' '.join(lst3)


# 3 Stack
class Stack():
    """
    >>> stack = Stack(3)
    >>> isinstance(stack.items, np.ndarray)
    True
    >>> stack.nelem
    0
    >>> print(stack)
    (bottom)(top)
    >>> stack.push(1)
    >>> stack.push(2)
    >>> print(stack)
    (bottom) 1 -> 2 (top)
    >>> stack.pop()
    2
    >>> print(stack)
    (bottom) 1 (top)
    >>> stack.pop()
    1
    >>> stack.pop()
    'No elements to remove'
    >>> stack.push(5)
    >>> stack.push(10)
    >>> stack.push(15)
    >>> stack.push(20)
    'No space to add elements'
    >>> print(stack)
    (bottom) 5 -> 10 -> 15 (top)
    >>> stack.peek()
    15
    >>> print(stack)
    (bottom) 5 -> 10 -> 15 (top)
    """
    # YOUR CODE HERE #
    def __init__(self, n):
        self.size = n
        self.nelem = 0
        self.items = np.array([]).astype(int)

    def push(self, num):
        if self.nelem == self.size:
            return 'No space to add elements'
        self.items = np.append(self.items, num)
        self.nelem += 1

    def pop(self):
        if self.nelem == 0:
            return 'No elements to remove'
        out = self.items[-1]
        self.items = self.items[:-1]
        self.nelem -= 1
        return out

    def peek(self):
        return self.items[-1]

    def __str__(self):
        out = ''
        for i in self.items:
            out += (' ' + str(i) + ' ->')
        return '(bottom)' + out[:-2] + '(top)'
