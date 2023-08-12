""" atomic_data_types.py 
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


def run_tests():  
    """run through docstring tests """ 
    doctest.run_docstring_examples(get_result, None) 
     
if __name__ == "__main__": 
    run_tests() 
    

# numeric data types 


print("----- integer -----")
get_result(2+3*4, 14, 1) 
get_result((2+3)*4, 20, 2) 
get_result(2**10, 1024, 3) 

print("----- floating point -----") 
get_result(6/3, 2.0, 4)
get_result(7/3, 2.3333333333333335, 5) 
get_result(7//3, 2,6) # floor 
get_result(7%3, 1, 7) # modulo 
get_result(3/6, 0.5, 8) 
get_result(3//6, 0, 9) # __floordiv__() 
get_result(3%6, 3, 10) 
get_result(2**100, 1267650600228229401496703205376, 11) # exponentiation 

print("----- boolean -----")  
get_result(True, True, 1)
get_result(False,False, 2) 
get_result(False or True, True, 3) 
get_result(not (False or True), False, 4) 
get_result(True and True, True, 5) 





