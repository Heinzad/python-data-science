""" selection_sort.py

""" 

import doctest 

def selection_sort(listicle): 
    """Sorts a given list in descending order from highest to lowest values 
    >>> test_list = [52, 25, 93, 39, 78, 87, 45, 51, 21, 12]
    >>> selection_sort(test_list)
    >>> print(test_list)
    [12, 21, 25, 39, 45, 51, 52, 78, 87, 93]

    """
    for i, item in enumerate(listicle): 
        idx = len(listicle) -1  # initialise minimum index position
        for j in range(i, len(listicle)): 
            if listicle[j] < listicle[idx]: 
                idx = j #swap them over 
        if idx != i: #swap them over 
            listicle[idx], listicle[i] = listicle[i], listicle[idx] 



if __name__ == "__main__":
    
    print("docstring test start ...")
    doctest.run_docstring_examples(selection_sort, None, verbose=False)
    print("...docstring test end")
