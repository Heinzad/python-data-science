""" insertion_sort.py 
    Exercises from chapter 5 of 
    Miller & Ranum "Problem Solving with Algorithms and Data Structures Using Python" (second edition) 
    [5.9. The Insertion Sort](https://runestone.academy/ns/books/published/pythonds3/SortSearch/TheInsertionSort.html)

    Algorithm: 
    A given list is sorted in-place. It is conceptually divided into two sublists: sorted and unsorted. 
    The boundary between the two sublists is at index position (i). 
    The two sublists are described as invariants, defined as: 
    -- Everything to the left of i (i.e. sort_list[0]) is 'sorted' 
    -- Everything to the right of i (i.e. sort_list[1:]) is 'unsorted'  
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
    """Sorts a given list in place, returning the number of comparisons 
    The number of comparisons varies by the size of the list and the extent of pre-sorting: 
    -- (n-1) for the O(n) best case (a list already sorted in ascending order)
    -- (n**2 -n)/2 for the O(n**2) worst case (a list already sorted in descending order)
    
    >>> ascending_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> best_case = insertion_sort(ascending_list)
    >>> print(ascending_list)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> print(best_case)
    9
    >>> descending_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    >>> worst_case = insertion_sort(descending_list)
    >>> print(descending_list)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> print(worst_case)
    45
    >>> random_list = [5, 2, 9, 3, 7, 8, 4, 6, 0, 1]
    >>> average_case = insertion_sort(random_list)
    >>> print(random_list)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    """ 

    comparisons = 0 
    
    # Outer Loop: ascend through unsorted sublist 
    for unsorted_key in range(1, len(sort_list)):  # begin one position higher than sorted sublist 
        
        unsorted_val = sort_list[unsorted_key] # next value in unsorted list     
        sorted_key = unsorted_key   # set the right bound of the sorted list at the left bound of the unsorted list 
        
        # count implicit comparison inherent in loop critera below
        if sort_list[sorted_key -1] <= unsorted_val:
            comparisons += 1

        else:                
            # Inner Loop: descend through sorted sublist until no greater value lies to the left 
            while sorted_key > 0 and sort_list[sorted_key -1] > unsorted_val: 
                comparisons += 1 
                
                # shift higher values up one place to fill the vacated position 
                sort_list[sorted_key] = sort_list[sorted_key -1] 

                # descend to the next place in the sorted sublist 
                sorted_key = sorted_key -1
                
        # Write the value into the correct position in the sorted sublist 
        sort_list[sorted_key] = unsorted_val 
        
    return comparisons 



if __name__ == "__main__":
    
    print("docstring test start ...")
    
    doctest.run_docstring_examples(insertion_sort, None, verbose=True)
    print("...docstring test end")
