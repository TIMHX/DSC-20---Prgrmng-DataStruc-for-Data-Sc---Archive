# Question 1

def reverse_list(lst):
    """ Reverses lst in place. Make sure to NOT create
    a new array. That is, switch all the elements
    within the same array. Only switch the elements 
    in the passed list and RETURN NOTHING.
    >>> x = [3, 2, 4, 5]
    >>> reverse_list(x)
    >>> x
    [5, 4, 2, 3]
    >>> x = [3, 2, 4, 5, 1]
    >>> reverse_list(x)
    >>> x
    [1, 5, 4, 2, 3]
    >>> x = []
    >>> reverse_list(x)
    >>> x
    []
    >>> x = [1] 
    >>> reverse_list(x)
    >>> x
    [1]
    """
    # Your code is here #
    lst[:] = list(reversed(lst))
    
 
# Question 2

def swap_lists(alist1, alist2):
    """Swaps content of two lists.
    Does not return anything. 
    >>> list1 = [1, 2]
    >>> list2 = [3, 4]
    >>> swap_lists(list1, list2)
    >>> print(list1)
    [3, 4]
    >>> print(list2)
    [1, 2]
    >>> list1 = [4, 2, 6, 8, 90, 45]
    >>> list2 = [30, 41, 65, 43, 4, 17]
    >>> swap_lists(list1, list2)
    >>> print(list1)
    [30, 41, 65, 43, 4, 17]
    >>> print(list2)
    [4, 2, 6, 8, 90, 45]
    """
    # Your code is here #
    alist1[:], alist2[:] = alist2,alist1[:]
  

# Question 3

def updated_dic(dict_price, dict_quantity):
    """
    >>> dict_price = {"lemon": 7, "orange": 15, "apple": 5}
    >>> dict_quantity = {"apple": 4, "lemon": 2}
    >>> updated_dic(dict_price, dict_quantity)
    >>> sorted(dict_price)
    ['apple', 'lemon']
    >>> [dict_price[i] for i in sorted(dict_price)]
    [20, 14]

    >>> dict_price = {"peaches": 10, "pears": 4, "grapes": 12}
    >>> dict_quantity = {"peaches": 3, "pears": 10}
    >>> updated_dic(dict_price, dict_quantity)
    >>> sorted(dict_price)
    ['peaches', 'pears']
    >>> [dict_price[i] for i in sorted(dict_price)]
    [30, 40]

    >>> dict_price = {"peaches": 10, "pears": 4, "grapes": 12}
    >>> dict_quantity = {}
    >>> updated_dic(dict_price, dict_quantity)
    >>> dict_price == {}
    True
    """
    # Your code is here #
    for i in dict_quantity.keys():
        dict_price[i] = dict_price[i] * dict_quantity[i]
    for i in list(dict_price):
        if i not in dict_quantity.keys():
            del dict_price[i]

# Question 4

def binary_search(lst, left, right, toFind):
    """
    >>> input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> for i in range(11):
    ...     print(binary_search(input, 0, 9, i), end = " ")
    -1 0 1 2 3 4 5 6 7 8 9 
    
    >>> input = [1, 3, 5, 10, 16, 19, 22]
    >>> binary_search(input, 0, 4, 5)
    2
    >>> binary_search(input, 0, 4, 22)
    -1
    >>> binary_search(input, 4, 6, 22)
    6

    >>> input = [1, 2, 3]
    >>> binary_search(input, 2, 0, 2)
    -1
    >>> input = []
    >>> binary_search(input, 0, 0, 6)
    -1
    """
    # Your code is here # 
    if len(lst) == 0:
        return -1
    if right >= left: 
        mid = left + (right - left) // 2
        if lst[mid] == toFind: 
            return mid 
        elif lst[mid] > toFind: 
            return binary_search(lst, left, mid-1, toFind) 
        else: 
            return binary_search(lst, mid + 1, right, toFind) 
    else: 
        return -1

# Question 5

class Aquarium:
    """Creates an Aquarium class with 1 class attribute and two class methods
    >>> Aquarium.content
    'water'
    >>> Aquarium.move()
    'Shattered in pieces'
    >>> Aquarium.install()
    'Bright and shiny'
    """
    # Your code is here #
    content = 'water'
    def move():
        return 'Shattered in pieces'
    def install():
        return 'Bright and shiny'

# Question 6

class FishTank:
    """ Creates a FishTank class with 1 class attribute (content),
    3 instance attributes (shape, w_type, color) and 1 methods.
    >>> tank = FishTank("round", "salt water", "black")
    >>> tank.content
    'water'
    >>> tank.color
    'black'
    >>> tank.w_type
    'salt water'
    >>> tank.change_shape("square")
    >>> tank.shape
    'square'
    """
    content = 'water'
	# Initializer (Constructor) / Instance Attributes
    def __init__(self, shape, w_type, color):
        self.shape = shape
        self.w_type = w_type
        self.color = color
    def change_shape(self, new_shape):
        self.shape = new_shape

# Question 7

class VendingMachine: 
    """ A vending machine that vends some product for some price. 
    >>> v = VendingMachine('candy', 10) 
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15) 
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2) 
    'Current candy stock: 2.'
    >>> v.vend() 
    'You must deposit $10 more.'
    >>> v.deposit(7) 
    'Current balance: $7.'
    >>> v.vend() 
    'You must deposit $3 more.'
    >>> v.deposit(5) 
    'Current balance: $12.'
    >>> v.vend() 
    'Here is your candy and $2 change.'
    >>> v.deposit(10) 
    'Current balance: $10.'
    >>> v.vend() 
    'Here is your candy.'
    >>> v.deposit(15) 
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2) 
    >>> w.restock(3)
    'Current soda stock: 3.'
    >>> w.restock(3) 
    'Current soda stock: 6.'
    >>> w.deposit(2) 
    'Current balance: $2.'
    >>> w.vend() 
    'Here is your soda.'
    """
    # Your code is here #
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.depo = 0
        self.stock = 0
        
    def deposit(self, num):
        if self.stock == 0:
            return 'Machine is out of stock. Here is your ${}.'.format(num)
        else:
            self.depo += num
            return 'Current balance: ${}.'.format(self.depo)
        
    def restock(self, num):
        self.stock += num
        return 'Current {0} stock: {1}.'.format(self.name,self.stock)
        
    def vend(self):
        if self.stock == 0:
            return 'Machine is out of stock.'
        if self.depo < self.price:
            return 'You must deposit ${0} more.'.format(self.price - self.depo)
        elif self.depo == self.price:
            self.stock -= 1
            self.depo = 0
            return 'Here is your {0}.'.format(self.name)
        else:
            self.stock -= 1
            change = self.depo - self.price
            self.depo = 0
            return 'Here is your {0} and ${1} change.'.format(self.name, change)
