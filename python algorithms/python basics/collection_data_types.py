"""collection_data_types.py
    Exercises from Chaper 1 of Miller & Ranum "Problem Solving With Algorithms and Data Structures Using Python" 
""" 


import doctest 

def get_result(answer, expected, label='_'): 
    """ displays if answer matches what was expected 
    
    # doctests 
    >>> test = get_result(1+1,2,'(a)')
    question (a) expected: 2, got: 2, result: Pass
    >>> test
    'Pass'

    """ 
    result = 'Fail'
    if expected == answer: 
        result = 'Pass' 
    print(f"question {label} expected: {expected}, got: {answer}, result: {result}")
    return result 

print("----- lists -----") 

get_result([1.3, True, 6.5], [1.3, True, 6.5], 1)

list_one = [1.3, True, 6.5] 
get_result(list_one, [1.3, True, 6.5], 2)

list_two = [0] * 6 
get_result(list_two, [0, 0, 0, 0, 0, 0], 3) 

list_three = [1, 2, 3, 4] 
list_four = [list_three] * 3
get_result(list_four, [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])

list_three[2] = 45 
get_result(list_four, [[1, 2, 45, 4], [1, 2, 45, 4], [1, 2, 45, 4]])

