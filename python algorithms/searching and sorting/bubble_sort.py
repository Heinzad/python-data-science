""" bubble_sort.py 
    Pairs and sorts neighbouring items. 
    Takes repeated trawls to sort through an entire list. 

    Exercises from chapter 5 of 
    Miller &amp; Ranum "Problem Solving with Algorithms and Data Structures Using Python" (second edition) 
    [5.7. The Bubble Sort](https://runestone.academy/ns/books/published/pythonds3/SortSearch/TheBubbleSort.html)
""" 

import doctest 

def bubble_sort(listing): 
    """Returns a sorted list using pairwise comparisons 
    >>> test_list = [52, 25, 81, 18, 78, 87, 45, 54, 31, 13] 
    >>> bubble_sort(test_list) 
    >>> print(test_list) 
    [13, 18, 25, 31, 45, 52, 54, 78, 81, 87]
    """
    for i in range( 
        len(listing) -1, # start 
        0, #stop 
        -1 #step 
    ): 
        for j in range (i): 
            if listing[j] > listing[j + 1]: # swap them
                temp = listing[j] 
                listing[j] = listing[j + 1] 
                listing[j + 1] = temp 


""" 
test_list = [52, 25, 81, 18, 78, 87, 45, 54, 31, 13] 
bubble_sort(test_list) 
print(test_list)

""" 


if __name__ == "__main__":
    
    print("docstring test start ...")
    doctest.run_docstring_examples(bubble_sort, None, verbose=False)
    print("...docstring test end")

