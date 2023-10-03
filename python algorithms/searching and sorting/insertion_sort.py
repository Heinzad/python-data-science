""" insertion_sort.py 
    Exercises from chapter 5 of 
    Miller & Ranum "Problem Solving with Algorithms and Data Structures Using Python" (second edition) 
    [5.9. The Insertion Sort](https://runestone.academy/ns/books/published/pythonds3/SortSearch/TheInsertionSort.html)
""" 

import doctest 

def insertion_sort(listicle): 
    """Sorts a given list using a sorted sublist
    
    >>> test_list = [52, 25, 93, 39, 78, 87, 45, 51, 21, 12]
    >>> insertion_sort(test_list)
    >>> print(test_list)
    [12, 21, 25, 39, 45, 51, 52, 78, 87, 93]

    """
    
    for i in range(1, len(listicle)): 
        val = listicle[i]               # current value 
        idx = i                         # current position 

        while idx > 0 and listicle[idx -1] > val: 
            listicle[idx] = listicle[idx -1] 
            idx = idx -1 
        
        listicle[idx] = val 



if __name__ == "__main__":
    
    print("docstring test start ...")
    doctest.run_docstring_examples(insertion_sort, None, verbose=True)
    print("...docstring test end")
