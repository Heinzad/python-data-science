""" unordered_list.py 
    #4.21 Implementing an Unorderd List: Linked Lists 
    # 4.21.2. The Node Class 
""" 

import doctest 

class Node: 
    """ a basic node for a linked list 
    >>> temp = Node(93)
    >>> temp.get_data()
    93
    
    """
    def __init__(self, initdata): 
        self.data = initdata 
        self.next = None 
        
    def get_data(self): 
        return self.data 
    
    def get_next(self): 
        return self.next 
    
    def set_data(self, newdata): 
        self.data = newdata 
        
    def set_next(self, newnext): 
        self.next = newnext 
        


def run_tests():  
    """run through docstring tests """
    doctest.run_docstring_examples(Node, None, verbose=False) 
    

if __name__ == "__main__": 
    run_tests() 
