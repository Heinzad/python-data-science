""" infix_prefix_postfix.py 
    # Exercises from [4.9. Infix, Prefix and Postfix Expressions](https://runestone.academy/ns/books/published/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html) 

    # Prefix: operators precede operands 
    # Postfix: operators after operands  

    

""" 
import doctest 

from stack import Stack 

def infix2postfix(infix): 
    """ Returns a postfix expression for given infix expression 
    
    #Algorithm: 
    0 Create a dictionary for operator precedence (bodmas)
    1 Create a stack for operators and a list for outputs 
    2 Split infix input string to a list 
    3 Iterate through the list: 
        - operands: append to output list 
        - left parentheses: push to operator stack 
        - right parentheses: pop operator stack until left parentheses is removed, 
            ... appending operators to output list
        - other operators '*/+-' : 
            ... if higher precedence operators on stack: append them to output list
            ... then push operator to stack 
        - at end of input: append operators from stack to output list 

    >>> infix_one = "A * B + C * D"  
    >>> postfix_one = infix2postfix(infix_one)
    >>> postfix_one
    'A B * C D * +'
    >>> infix_two = "( A + B ) * C - ( D - E ) * ( F + G )"  
    >>> postfix_two = infix2postfix(infix_two)
    >>> postfix_two
    'A B + C * D E - F G + * -'
    >>> infix_three = "( A + B ) * ( C + D )"
    >>> postfix_three = infix2postfix(infix_three)
    >>> postfix_three
    'A B + C D + *'
    >>> infix_four = "( A + B ) * C"
    >>> postfix_four = infix2postfix(infix_four)
    >>> postfix_four
    'A B + C *'
    >>> infix_five = "A + B * C"
    >>> postfix_five = infix2postfix(infix_five)
    >>> postfix_five
    'A B C * +'

    """ 

    # operator precedence rankings 
    bodmas = {} 
    bodmas["*"] = 3 # multiplication 
    bodmas["/"] = 3 # division 
    bodmas["+"] = 2 # addition 
    bodmas["-"] = 2 # subtraction 
    bodmas["("] = 1 # left parenthesis 

    operators = Stack() 
    postfix = [] 

    tokens = infix.split() 

    for token in tokens: 
        
        # operands 
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789": 
            postfix.append(token) 

        # left parenthesis 
        elif token == "(": 
            operators.push(token)

        # right parenthesis: 
        elif token == ")": 
            operator = operators.pop() # de-stack
            while operator != "(": 
                postfix.append(operator) # listing 
                operator = operators.pop() 
        
        else: 
            while (not operators.is_empty()) and \
            (bodmas[operators.peek()] >= bodmas[token]): 
                postfix.append(operators.pop())
            operators.push(token)

    while not operators.is_empty(): 
        postfix.append(operators.pop())
    
    separator = chr(32) # space 

    return separator.join(postfix) 


if __name__ == '__main__': 
    """ run all the doc tests"""
    doctest.testmod()












