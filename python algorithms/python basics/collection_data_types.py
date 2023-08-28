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

# Initialise a list with repetition 
list_two = [0] * 6 
get_result(list_two, [0, 0, 0, 0, 0, 0], 3) 

## Note the repetition is of the references to the object in the sequence 
list_three = [1, 2, 3, 4] 
list_four = [list_three] * 3
get_result(list_four, [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])

list_three[2] = 45 
get_result(list_four, [[1, 2, 45, 4], [1, 2, 45, 4], [1, 2, 45, 4]])

# List Methods: 

lst_mthd = [1024, 3, True, 6.5] 
print(f"#lst expected [1024, 3, True, 6.5] got: {lst_mthd}")

lst_mthd.append(False) 
print(f"#lst expected [1024, 3, True, 6.5, False] got: {lst_mthd}")

lst_mthd.insert(2, 4.5) # insert at lst[2] 
print(f"#lst expected [1024, 3, 4.5, True, 6.5, False] got: {lst_mthd}")

print(f"#pop expected False got: {lst_mthd.pop()}") 
print(f"lst expected [1024, 3, 4.5, True, 6.5] got: {lst_mthd}")

print(f"#pop(1) expected 3 got: {lst_mthd.pop(1) }") 
print(f"#lst expected [1024, 4.5, True, 6.5] got: {lst_mthd}")

print(f"#pop(2) expected True got: {lst_mthd.pop(2) }") 
print(f"#lst expected [1024, 4.5, 6.5] got: {lst_mthd}")

lst_mthd.sort() 
print(f"#lst expected [4.5, 6.5, 1024] got: {lst_mthd}") 

lst_mthd.reverse() 
print(f"#lst expected [1024, 6.5, 4.5] got: {lst_mthd}") 

print(f"#count(6.5) expected 1 got: {lst_mthd.count(6.5)}") 
print(f"#index(4.5) expected 2 got: {lst_mthd.index(4.5)}") 

lst_mthd.remove(6.5) 
print(f"#lst expected [1024, 4.5] got: {lst_mthd}") 

del lst_mthd[0] 
print(f"#lst expected [4.5] got: {lst_mthd}") 



# Ranges 

print(f"range(10): {range(10)}") 

print(f"list(range(10)): {list(range(10))}")

print(f"range(5,10): {range(5,10)}") 

print(f"list(range(5,10)): {list(range(5,10))}") 

print(f"list(range(5,10,2)): {list(range(5,10,2))}") 

print(f"list(range(10,1,-1)): {list(range(10,1,-1))}") 
 

