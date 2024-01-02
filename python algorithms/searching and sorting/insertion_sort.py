""" insertion_sort.py 
    Exercises from chapter 5 of 
    Miller & Ranum "Problem Solving with Algorithms and Data Structures Using Python" (second edition) 
    [5.9. The Insertion Sort](https://runestone.academy/ns/books/published/pythonds3/SortSearch/TheInsertionSort.html)

    Algorithm: 
    A given list is sorted in-place. It is conceptually divided into two sublists: sorted and unsorted. 
    The boundary between the two sublists is at index position (i). 
    -- Everything to the left of i (i.e. sort_list[0]) is the 'sorted sublist' 
    -- Everything to the right of i (i.e. sort_list[1:]) is the 'unsorted sublist' 
    An outer loop ascends through the unsorted sublist from the left bound to the right bound, 
    launching an innner loop for each unsorted index postition (i):  
    -- The value at the unsorted index position (i) is placed into a temp variable (val), and 
    -- The unsorted index position (i) is mirrored (j) to initialise an inner loop.   
    The inner loop descends through the sorted sublist from right to left, and  
    -- if the sorted value is greater than the temp value, then 
    -- the sorted value is shifted up one place into the vacant slot to the right 
""" 

import doctest 

def insertion_sort(sort_list): 
    """Sorts a given list in place 
    
    >>> test_list = [52, 25, 93, 39, 78, 87, 45, 51, 21, 12]
    >>> insertion_sort(test_list)
    >>> print(test_list)
    [12, 21, 25, 39, 45, 51, 52, 78, 87, 93]

    """ 
    
    # Unsorted Loop: 
    # ascend through unsorted sublist 
    for unsorted_idx in range(1, len(sort_list)):  # begin one position higher than sorted sublist 
        
        val = sort_list[unsorted_idx] # next value in unsorted list
        sorted_idx = unsorted_idx   # set the right bound of the sorted list at the left bound of the unsorted list 

        # Sorted Loop: 
        # descend through sorted sublist until no greater value lies to the left 
        while sorted_idx > 0 and sort_list[sorted_idx -1] > val: 

            # shift higher values up one place to fill the vacated position 
            sort_list[sorted_idx] = sort_list[sorted_idx -1] 
            
            # descend to the next place in the sorted sublist 
            sorted_idx = sorted_idx -1  

        # Write the value into the correct position in the sorted sublist 
        sort_list[sorted_idx] = val




if __name__ == "__main__":
    
    print("docstring test start ...")
    doctest.run_docstring_examples(insertion_sort, None, verbose=False)
    print("...docstring test end")
