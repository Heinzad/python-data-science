""" stack.py 
    Exercises from Brad Miller and David Ranum, "Problem Solving with Algorithms and Data Structures using Python", Luther College
    [4.5. Implementing a Stack in Python](https://runestone.academy/ns/books/published/pythonds/BasicDS/ImplementingaStackinPython.html) 

    LIFO: A Stack is Last-in, first-out - just like a pile of books or unwashed dishes. 
    A browser history may be implemented as a stack, with the url of the first page visited at the bottom of the stack 
    and the last page visited at the top of the stack. Pushing the back button pops the last url off the top of the stack. 
    
""" 

import doctest 

class Stack: 
    """ Uses a list to implement a stack abstract data type. 
        Implements stack operations using list methods (e.g. append and pop)  
        
        # Methods: 
        Stack() creates a stack (which is empty)  
        push(item) adds a given item to the top of the stack 
        pop() removes the top item from the stack
        peek() displays the top item from the stack 
        is_empty() flags if the stack is empty 
        size() returns an item count 

    """ 

    def __init__(self): 
        """ Initialise an empty stack as a list """
        self.items = [] 
    
    def is_empty(self):  
        """ Flags if a stack holds zero or more items. 
            Returns a boolean value 

        >>> nihil = Stack()
        >>> nihil.is_empty()
        True

        """
        return self.items == [] 
    
    def push(self, item): 
        """ Adds a given item to the top of a stack 
        
        >>> pushy = Stack()
        >>> pushy.push('proposition')
        >>> pushy
        proposition

        """ 
        self.items.append(item) 

    
    def pop(self): 
        """ Returns the top item on the stack

        >>> poppy = Stack()
        >>> poppy.push('putty')
        >>> popper = poppy.pop()
        >>> popper
        'putty'

        """
        return self.items.pop()
     
    
    def peek(self): 
        """ Displays the top item on the stack 
        
        >>> peeper = Stack()
        >>> peeper.push('peek-a-boo')
        >>> print(peeper.peek())
        ['peek-a-boo']

        """ 
        return self.items[-1:] # will return even if empty
     
    
    def size(self): 
        """ Displays the number of items in the stack 

        >>> girthy = Stack()
        >>> girthy.push('one')
        >>> girthy.push('two')
        >>> girthy.push('three')
        >>> print(girthy.size())
        3
        """
        return len(self.items) 
    
    def __str__(self): 
        """ Stringifies the items in the stack to enable printing """
        stringifer = ''
        for item in self.items: 
            stringifer += f"{item}" + chr(32)
        return stringifer.strip() 
    
    def __repr__(self): 
        """ Returns a string to represent the object """
        return str(self)
    

if __name__ == '__main__': 
    """ run all the doc tests"""
    doctest.testmod() 

