""" merge_sort.py 
    
    Exercises from chapter 5 of 
    Miller & Ranum "Problem Solving with Algorithms and Data Structures Using Python" (second edition) 
    [5.11. The Merge Sort](https://runestone.academy/ns/books/published/pythonds3/SortSearch/TheMergeSort.html)
""" 

import doctest 

def merge_sort(listicle): 
    """Sorts a given list using a recursive divide and conquer approach 
    
    >>> test_list = [52, 25, 93, 39, 78, 87, 45, 51, 21, 12]
    >>> merge_sort(test_list)
    >>> print(test_list)
    [12, 21, 25, 39, 45, 51, 52, 78, 87, 93]

    """ 
    
    if len(listicle) > 1: 
        mid_point = len(listicle) // 2 
        left_sublist = listicle[:mid_point] 
        right_sublist = listicle[mid_point:] 

        merge_sort(left_sublist) 
        merge_sort(right_sublist) 

        l, r, p = 0, 0, 0 # indexes for left, right, and parent lists 

        # both 
        while l < len(left_sublist) and r < len(right_sublist): 
            if left_sublist[l] <= right_sublist[r]: 
                listicle[p] = left_sublist[l] 
                l += 1 
            else: 
                listicle[p] = right_sublist[r] 
                r += 1 
            p += 1 

        # leftwards 
        while l < len(left_sublist): 
            listicle[p] = left_sublist[l] 
            l += 1
            p += 1 

        # rightwards
        while r < len(right_sublist): 
            listicle[p] = right_sublist[r] 
            r += 1 
            p += 1 


if __name__ == "__main__":
    
    print("docstring test start ...")
    doctest.run_docstring_examples(merge_sort, None, verbose=True)
    print("...docstring test end")
