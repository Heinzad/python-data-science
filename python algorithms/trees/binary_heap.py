"""binary_search_tree.py 
    Exercises from chapter 6 section 6.11 'Binary Heap Implementation' of 
    Miller & Ranum 'Problem Solving with Algorithms and Data Structures Using Python' (second edition)

    
""" 
import doctest 

class BinaryHeap: 
    """ Binary Heap 
        A list or array can be conceived as a heap where 
        a child index number is double that of its parent, and  
        a parent index number is half that of its child.
    """ 
    def __init__(self): 
        self.priority_queue = [None] # [0] not used so integer division can be used
        self.queue_length = 0 

    def _limb_up(self, idx): 
        """ Percolates a given item up a tree
            by switching positions (via temporary storage) 
            if its value is greater than that of its parent node. 
            (A parent node has an index number half that of its child) 
        """ 
        while idx // 2 > 0: # is below root 
            if self.priority_queue[idx] < self.priority_queue[idx//2]: 
                upper = self.priority_queue[idx//2] 
                self.priority_queue[idx//2] = self.priority_queue[idx] 
                self.priority_queue[idx] = upper 
            idx = idx // 2 # integer division 

    def ins(self, k): 
        """ Appends a given item at the end of a list, 
            conceptualised as a leaf node in a binary tree. 
        """
        self.priority_queue.append(k) 
        self.queue_length += 1   # next index position 
        self._limb_up(self.queue_length) 

    def _limb_down(self, idx): 
        """ Percolates a given item down a tree 
            if its value is less than that of its child node 
            (a child index number is double that of its parents index) 
        """ 
        while (idx * 2) <= self.queue_length: 
            child_ix = self._get_min(idx)
            if self.priority_queue[idx] > self.priority_queue[child_ix]:  
                downer = self.priority_queue[idx] 
                self.priority_queue[idx] = self.priority_queue[child_ix] 
                self.priority_queue[child_ix] = downer 
            idx = child_ix 

    def _get_min(self, idx): 
        """ Pass """ 
        if (idx * 2 + 1) > self.queue_length: 
            return (idx * 2) # left child index is double the parent
        elif self.priority_queue[idx * 2] < self.priority_queue[idx * 2 + 1]: 
            return (idx * 2) # left child index is double the parent
        else: 
            return (idx * 2 + 1) # right child index is double the parent plus one

    def out(self): 
        """ Returns the smallest value and prunes it from the top of the tree """
        result = self.priority_queue[1] 
        self.priority_queue[1] = self.priority_queue[self.queue_length] # move to end 
        self.queue_length -= 1 # index of last leaf postition is shrunk  
        self.priority_queue.pop() # remove end 
        self._limb_down(1) 
        return result 
    
    def is_empty(self): 
        return self.queue_length == 0 
    
    def heapify(self, qlist): 
        """ Builds a priority queue heap from a given list
        
        >>> pqueue = BinaryHeap()
        >>> pqueue.heapify([9,5,8,4,7,3,6,1,2])
        >>> result_list = []
        >>> while not pqueue.is_empty(): result_list.append(pqueue.out())
        >>> print(result_list)
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
        """
        idx = len(qlist) // 2 
        self.queue_length = len(qlist) 
        self.priority_queue = [0] + qlist[:] 
        while idx > 0: 
            self._limb_down(idx)
            idx -= 1 


if __name__ == "__main__":
    
    print("docstring test start ...")
    doctest.run_docstring_examples(BinaryHeap.heapify, None, verbose=False)
    print("...docstring test end")


    




    







