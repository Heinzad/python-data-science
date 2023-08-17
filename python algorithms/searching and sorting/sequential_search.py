"""sequential_search.py

Exercises from chapter 5 of 
Miller &amp; Ranum "Problem Solving with Algoritms and Data Structrues Using Python" (second edition)
""" 

def sequential_search(the_list, item): 
    """Starting at the first item in the list, 
        move from item to item in sequence, 
        until the item is found or the end is reached
    """
    postn = 0 
    is_found = False 

    while postn < len(the_list) and not is_found: 
        if the_list[postn] == item: 
            is_found = True 
        else: 
            postn += 1 

    return is_found 
