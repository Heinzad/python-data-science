""" recursive_binary_search.py
    Exercises from chapter 5 of 
    Miller &amp; Ranum "Problem Solving with Algoritms and Data Structrues Using Python" (second edition)
""" 

def binary_search(search_list, search_item): 
    """Performs a recursive binary search""" 

    if len(search_list) == 0: 
        return False 
    else: 
        mid = len(search_list)//2 
        if search_list[mid] == search_item: 
            return True
        else: 
            if search_item < search_list[mid]: 
                return binary_search(search_list[:mid], search_item) 
            else: 
                return binary_search(search_list[mid+1:], search_item)

