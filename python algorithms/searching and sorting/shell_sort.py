""" shell_sort.py 
    'Dont sell shell sort short' 
    
    Exercises from chapter 5 of 
    Miller & Ranum "Problem Solving with Algorithms and Data Structures Using Python" (second edition) 
    [5.10. The Shell Sort](https://runestone.academy/ns/books/published/pythonds3/SortSearch/TheShellSort.html)
""" 

import doctest 

def shell_sort(listicle): 
    """Sorts a given list using sublists picked via an increment of n items 
    
    >>> test_list = [52, 25, 93, 39, 78, 87, 45, 51, 21, 12]
    >>> shell_sort(test_list)
    >>> print(test_list)
    [12, 21, 25, 39, 45, 51, 52, 78, 87, 93]

    """ 
    shard = 2 
    sublist_count = len(listicle) // shard 
    while sublist_count > 0: 
        for posn in range(sublist_count): 
            gap_insertion_sort(listicle, posn, sublist_count) 
        sublist_count = sublist_count // shard 

def gap_insertion_sort(listing, start, gap): 
    """does something here """ 
    for i in range(
        start + gap,        # start 
        len(listing),       # stop 
        gap                 # step 
    ): 
        val = listing[i]    # current value 
        pos = i 

        while pos >= gap and listing[pos - gap] > val: 
            listing[pos] = listing[pos - gap] 
            pos = pos - gap 
        
        listing[pos] = val 



if __name__ == "__main__":
    
    print("docstring test start ...")
    doctest.run_docstring_examples(shell_sort, None, verbose=True)
    print("...docstring test end")
