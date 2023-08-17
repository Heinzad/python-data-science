"""binary_search.py
    Exercises from chapter 5 of 
    Miller &amp; Ranum "Problem Solving with Algoritms and Data Structrues Using Python" (second edition)
""" 

def binary_search(the_list, item): 
    """Binary search of an ordered list"""
    first = 0 
    last = len(the_list)-1 
    found = False 

    while first <= last and not found: 
        mid = (first + last)//2 
        if the_list[mid] == item: 
            found = True 
        else: 
            if item < the_list[mid]: 
                last = mid -1 
            else: 
                first = mid + 1 
    
    return found 


