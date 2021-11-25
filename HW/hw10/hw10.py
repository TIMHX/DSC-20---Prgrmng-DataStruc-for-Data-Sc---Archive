import numpy as np
from stack import Stack


## Question 1 ##
def paren_checker(expression):
    """
    YOU MUST USE YOUR STACK CLASS THAT YOU IMPLEMENTED IN LAB10. Check the
    writeup for details. This function checks whether the pairs and the orders
    of '{', '}', '(','), '[', ']' are correct in a given expression.

    >>> paren_checker("(((]})")
    False
    >>> paren_checker("(")
    False
    >>> paren_checker("(){}[]")
    True
    >>> paren_checker("(   x   )")
    True
    >>> paren_checker("a()b{}c[]d")
    True
    >>> paren_checker("")
    True

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> paren_checker("([{}])")
    True
    >>> paren_checker(")[{}](")
    False
    >>> paren_checker("[]]----()")
    False
    """
    # Your Code Here
    s = Stack(len(expression))
    if s.nsize == 0:
        return True
    for i in range(len(expression)):
        if expression[i] == '(':
            s.push(1)
        elif expression[i] == '[':
            s.push(2)
        elif expression[i] == '{':
            s.push(3)

        if expression[i] == ')':
            x = s.pop()
            if x == 2 or x == 3:
                return False
            elif x == 'No elements to remove':
                return False
        elif expression[i] == ']':
            x = s.pop()
            if x == 1 or x == 3:
                return False
            elif x == 'No elements to remove':
                return False
        elif expression[i] == '}':
            x = s.pop()
            if x == 1 or x == 2:
                return False
            elif x == 'No elements to remove':
                return False

    if s.isEmpty():
        return True
    else:
        return False


## Question 2 ##
class Queue:
    """
    A queue ADT that dequeues from front and enqueues at rear.

    >>> a=Queue()
    >>> a.enqueue(1)
    >>> a.enqueue(2)
    >>> a.enqueue(3)
    >>> a.enqueue(4)
    >>> a.enqueue(5)
    >>> a.print_queue()
    [ | 1 | 2 | 3 | 4 | 5 | ]
    >>> a.front
    0
    >>> a.rear
    5
    >>> a.data
    array([1, 2, 3, 4, 5, None, None, None, None, None], dtype=object)
    >>> a.capacity
    10
    >>> a.dequeue()
    1
    >>> a.print_queue()
    [ | 2 | 3 | 4 | 5 | ]
    >>> a.front
    1
    >>> a.rear
    5

    >>> a=Queue(10)
    >>> a.capacity
    10

    >>> b=Queue()
    >>> b.dequeue()
    Attempt to dequeue from an empty queue
    >>> b.enqueue(1)
    >>> b.enqueue(max)
    >>> b.print_queue()
    [ | 1 | <built-in function max> | ]
    >>> b.dequeue()
    1
    >>> b.dequeue()
    <built-in function max>
    >>> b.front
    2
    >>> b.rear
    2
    >>> b.dequeue()
    Attempt to dequeue from an empty queue

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> c = Queue(capacity=3)
    >>> c.capacity
    3
    >>> c.enqueue(1)
    >>> c.num_elements
    1
    >>> c.dequeue()
    1
    >>> c.num_elements
    0
    >>> c.print_queue()
    []
    >>> c.expand()
    >>> c.capacity
    6
    >>> c.dequeue()
    Attempt to dequeue from an empty queue
    """

    def __init__(self, capacity=5):
        """
        >>> q = Queue()
        >>> q.capacity
        5
        >>> q.data
        array([None, None, None, None, None], dtype=object)
        >>> q.num_elements
        0
        """
        # Your Code Here
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.num_elements = 0
        self.data = np.array([None] * capacity, dtype=object)

    def dequeue(self):
        """
        dequeues from the front of the queue
        >>> q = Queue()
        >>> q.dequeue()
        Attempt to dequeue from an empty queue
        >>> q.enqueue(1)
        >>> q.enqueue(2)
        >>> q.enqueue(3)
        >>> q.num_elements
        3
        >>> q.dequeue()
        1
        >>> q.num_elements
        2
        >>> q.front
        1
        """
        # Your Code Here
        if self.is_empty():
            print("Attempt to dequeue from an empty queue")
            return
        else:
            temp = self.data[self.front]
            self.data[self.front] = None
            self.front = (self.front + 1) % self.capacity
            self.num_elements -= 1
            return temp

    def enqueue(self, elem):
        """
        enqueue at the rear of the queue
        >>> q = Queue()
        >>> q.enqueue("a")
        >>> q.enqueue(1)
        >>> q.data
        array(['a', 1, None, None, None], dtype=object)
        >>> q.num_elements
        2
        >>> for i in range(4): q.enqueue(i)
        >>> q.data
        array(['a', 1, 0, 1, 2, 3, None, None, None, None], dtype=object)
        >>> p = Queue()
        >>> for i in range(5): p.enqueue(i)
        >>> p.data
        array([0, 1, 2, 3, 4, None, None, None, None, None], dtype=object)
        """
        # Your Code Here
        if self.is_full():
            self.expand()
        self.data[self.rear] = elem

        self.rear = (self.rear + 1) % len(self.data)
        self.num_elements += 1


    def expand(self):
        """
        expand the capacity of the circular array when needed
        >>> q = Queue()
        >>> q.capacity
        5
        >>> q.expand()
        >>> q.capacity
        10
        >>> q.expand()
        >>> q.capacity
        20
        """
        # Your Code Here
        self.data = np.append(self.data, \
                                   np.array([None] * self.capacity, dtype=object))
        self.capacity = 2*self.capacity

    def is_full(self):
        """
        checks if circular array is full
        >>> q = Queue()
        >>> for i in range(4): q.enqueue(i)
        >>> q.data
        array([0, 1, 2, 3, None], dtype=object)
        >>> q.is_full()
        False
        >>> q.enqueue(4)
        >>> q.is_full()
        False
        >>> q.capacity
        10
        """
        # Your Code Here
        return (self.rear + 1) % self.capacity == self.front

    def is_empty(self):
        """
        checks if circular array is full
        >>> q = Queue()
        >>> q.is_empty()
        True
        >>> q.enqueue('a')
        >>> q.is_empty()
        False
        >>> q.dequeue()
        'a'
        >>> q.is_empty()
        True
        """
        # Your Code Here
        return self.num_elements == 0

    def print_queue(self):
        """
        prints out queue in a human-friendly format
        >>> q = Queue()
        >>> for i in range(5): q.enqueue(i)
        >>> q.print_queue()
        [ | 0 | 1 | 2 | 3 | 4 | ]
        >>> p = Queue()
        >>> p.print_queue()
        []
        >>> p.enqueue('a')
        >>> p.print_queue()
        [ | a | ]
        >>> p.dequeue()
        'a'
        >>> p.print_queue()
        []
        """
        # Your Code Here
        lst = []
        if self.is_empty():
            print(lst)
        else:
            out = '[ | '
            for data in self.data:
                if data != None:
                    out += str(data) + " | "
            out += ']'
            print(out)


## Question 3 ##
def cursed_carousel(n, m):
    """
    m is the number of customers in line
    n is the number of customers sent to the back of the line
    Return the number of the customer which is last to be served

    >>> cursed_carousel(6,3)
    3
    6
    4
    2
    5
    1
    >>> cursed_carousel(-1,-2)
    m and n should be positive!
    >>> cursed_carousel('5','1')
    Invalid input data type.

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> cursed_carousel(5,3)
    3
    1
    5
    2
    4
    >>> cursed_carousel(5,1)
    1
    2
    3
    4
    5
    >>> cursed_carousel(5,5)
    5
    1
    3
    4
    2
    """
    # Your Code Here
    if not (isinstance(n,int) and isinstance(m,int)):
        print('Invalid input data type.')
        return
    if not (n > 0 and m > 0):
        print('m and n should be positive!')
        return

    q = Queue()
    for i in range(1, n + 1):
        q.enqueue(i)

    count = 1
    while not (q.is_empty()):
        if count % m == 0:
            out = q.dequeue()
            print(out)
        else:
            out = q.dequeue()
            q.enqueue(out)
        count += 1


## Question 4 (Extra Credit) ##
def find_best_farm(land_plots):
    """
    Finds the best farm given a list of land plots.

    Restrictions: You must use a stack and your algorithm must run
    in O(n) time. Make sure to fill out extra_credit.txt to get credit.

    >>> find_best_farm([3, 2, 3])
    6
    >>> find_best_farm([1, 2, 3, 4, 5])
    9
    >>> find_best_farm([5, 4, 3, 2, 1])
    9

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    """
    # Your Code Here
