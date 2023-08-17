""" ordered_sequential_search.py
    Exercises from chapter 5 of 
    Miller &amp; Ranum "Problem Solving with Algoritms and Data Structrues Using Python" (second edition)
""" 

def ordered_sequential_search(search_list, search_item): 
    """Sequential Search of an Ordered List"""
    postn = 0 
    is_found = False 
    halted = False 

    while postn < len(search_list) and not is_found and not halted: 
        if search_list[postn] == search_item: 
            is_found = True 
        else: 
            if search_list[postn] > search_item: 
                halted = True 
            else: 
                postn += 1 

    return is_found 


 