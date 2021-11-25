class Stack():
    def __init__(self):
        self.items = []
    def push(self, elem):
        self.items.append(elem)
    def pop(self):
        value = self.items[-1]
        self.items = self.items[:-1]
        return value
    def peek(self):
        value = self.items[-1]
        return value
    def size(self):
        return len(self.items)


def stack_almost_min(stk, maxval):
    """
    >>> stk_one = Stack()
    >>> stk_one.push(10)
    >>> stk_one.push(3)
    >>> stk_one.push(1)
    >>> stack_almost_min(stk_one, 100)
    3
    """
    # YOUR CODE HERE
    def sorting(stk):
        temp = Stack()
        while stk.size() > 0:
            stk_pop = stk.pop()
            while temp.size() > 0 and temp.peek() > stk_pop:
                temp_pop = temp.pop()
                stk.push(temp_pop)
            temp.push(stk_pop)
        return temp.items

    out = sorting(stk)[::-1]
    del (out[0])
    for i in out:
        if i < maxval:
            return i