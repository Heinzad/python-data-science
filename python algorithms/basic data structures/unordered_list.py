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
        


class UnorderedList: 
    """ implements a collection of nodes linked by explicit references. 

    >>> mylist = UnorderedList()
    >>> mylist.add(32)
    >>> mylist.add(77)
    >>> mylist.add(17)
    >>> mylist.add(93)
    >>> mylist.add(26)
    >>> mylist.add(54)
    >>> mylist.search(17)
    True
    """ 
    def __init__(self): 
        self.head = None 

    def is_empty(self): 
        """ checks to see if the head of the list is a reference to None """
        return self.head == None 
    
    def add(self, item): 
        """ Creates a new node in the linked list """ 
        temp = Node(item) # create a new node with item for data 
        temp.set_next(self.head) # refer to old first node 
        self.head = temp # modify head to refer to the new node

    def length(self): 
        """ Traverse the linked list to count the number of nodes """ 
        node_n = self.head 
        counter = 0 
        while node_n!= None: 
            counter += 1 
            node_n = node_n.get_next() 
        return counter 

    def search(self, item): 
        """ traverses the list to discover if item in node data """
        node_data = self.head 
        item_found = False 
        while node_data != None and not item_found: 
            if node_data.get_data() == item: 
                item_found == True 
            else: 
                node_data = node_data.get_next() 
        return item_found
    
    def remove(self, item): 
        """ Seek and destroy a node containing the given item and 
        overwrite the references 
        """
        current_node = self.head 
        previous_node = None 
        flag_found = False 
        while not flag_found: 
            if current_node.get_data() == item: 
                flag_found = True 
            else: 
                previous_node = current_node 
                current_node = current_node.get_next() 

        if previous_node == None: 
            self.head = current_node.get_next() 
        else: 
            previous_node.set_next(current_node.get_next()) 
    
    def pop(self, position): 
        pass 

    


def run_tests():  
    """run through docstring tests """ 
    verbosity = False 
    doctest.run_docstring_examples(Node, None, verbose=verbosity) 
    #doctest.run_docstring_examples(UnorderedList, None, verbose=verbosity) 
    

if __name__ == "__main__": 
    print("test run begun")
    run_tests() 
    print("test run done") 


