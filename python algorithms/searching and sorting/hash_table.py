"""binary_search.py
    Exercises from chapter 5 of 
    Miller &amp; Ranum "Problem Solving with Algoritms and Data Structrues Using Python" (second edition)
""" 

import doctest 

class HashTable: 
    """ Implements the map abstract data type.
        The slots list holds the keys while the data list holds the values. 
        Consider the key list as a hash table. 
        The initial size needs to be a prime number  
    # Create and populate a hash table with keys and values: 
    >>> hh = HashTable()
    >>> hh[54] = "cat"
    >>> hh[26] = "dog"
    >>> hh[93] = "lion"
    >>> hh[17] = "tiger"
    >>> hh[77] = "bird"
    >>> hh[31] = "cow"
    >>> hh[44] = "goat"
    >>> hh[55] = "pig"
    >>> hh[20] = "chicken"
    >>> print(hh.slots)
    [77, 44, 55, 20, 26, 93, 17, None, None, 31, 54]
    >>> print(hh.data)
    ['bird', 'goat', 'pig', 'chicken', 'dog', 'lion', 'tiger', None, None, 'cow', 'cat']
    >>> print(hh[20])
    'chicken'
    >>> print(hh[17])
    'tiger'
    >>> hh[20] = 'duck'
    >>> print(hh[20])
    'duck'
    >>> print(hh.data)
    ['bird', 'goat', 'pig', 'duck', 'dog', 'lion', 'tiger', None, None, 'cow', 'cat']
    >>> print(hh[99])
    None

    """ 

    def __init__(self): 
        self.size = 11 # a prime number 
        self.slots = [None] * self.size 
        self.data = [None] * self.size 


    def hashfunction(self, key, size): 
        """Implements the simple remainder method. 
            The collision resolution technique is linear probing 
            with a 'plus 1' rehash function 
            It computes the original hash value and if that slot is not empty, 
            iterates the rehash function until an empty slot occurs. 
            If a nonempty slot already contains the key, 
            the old data value is replaced with the new data value. 
        """
        return key%size 
    

    def rehash(self, oldhash, size): 
        return(oldhash+1)%size 
    

    def put(self, key, data): 
        hash_value = self.hashfunction(key, len(self.slots)) 

        if self.slots[hash_value] == None: 
            self.slots[hash_value] = key 
            self.data[hash_value] = data 
        else: 
            if self.slots[hash_value] == key: 
                self.data[hash_value] = data # overwrite 
            else: 
                next_slot = self.rehash(hash_value, len(self.slots)) 
                while self.slots[next_slot] != None and \
                self.slots[next_slot] != key: 
                    next_slot = self.rehash(next_slot, len(self.slots)) 

                if self.slots[next_slot] == None: 
                    self.slots[next_slot] = key 
                    self.data[next_slot] = data 
                else: 
                    self.data[next_slot] = data # overwrite 


    def get(self, key): 
        """
            Computes the initial hash value. 
            If the value is not found in the initial slot, 
            finds the next possible posn using rehash. 
            The search will terminate by checking we have not 
            returned the initial slot. 
            In that case, we have exhausted all possibilities 
            and the item is not in any of the slots. 
        """

        start_slot = self.hashfunction(key, len(self.slots)) 

        data = None 
        stop = False 
        found = False 
        posn = start_slot # position 

        while self.slots[posn] != None and \
        not found and not stop: 
            if self.slots[posn] == key: 
                fount = True 
                data = self.data[posn] 
            else: 
                posn = self.rehash(posn, len(self.slots)) 
                if posn == start_slot: 
                    stop = True 
        
        return data 

    # overload the dunder methods to allo access using lists[] index
    def __getitem__(self, key): 
        return self.get(key) 
    
    def __setitem__(self, key, data): 
        self.put(key, data) 

 

if __name__ == "__main__":
    
    print("docstring test start ...")
    verbosity = True
    doctest.run_docstring_examples(HashTable, None, verbose=verbosity)
    print("...docstring test end")



