import numpy as np

class Stack():
    def __init__(self, n):
        self.nsize = n
        self.nelem = 0
        self.items = np.array([]).astype(int)

    def push(self, num):
        if self.nelem == self.nsize:
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
    
    def size(self):
        return self.nelem

    def isEmpty(self):
        if self.nelem == 0:
            return True
        else:
            return False

    def __str__(self):
        out = ''
        for i in self.items:
            out += (' ' + str(i) + ' ->')
        return '(bottom)' + out[:-2] + '(top)'
