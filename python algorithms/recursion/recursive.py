
# Recursive List Sum 
def recursum(numbers): 
    # Escape Clause: 
    if len(numbers) == 1: 
        return numbers[0]
    else: 
        # calls itself 
        return numbers[0] + recursum(numbers[1:]) 
    

# Convert an integer to a string 

 

def nbase(n, base): 
    """
    Algorithm: 
    1. Reduce the original number to a series of single-digit numbers. 
    2. Convert the single-digit number ot a string using a lookup. 
    3. Concatenate the single-digit strings for the final result.
    """
    stringer = "0123456789ABCDEF" 
    if n < base: 
        return stringer[n]
    else: 
        return nbase(n//base, base) + stringer[n%base] 

x = nbase(789, 10) 
print(x) 

y = nbase(10,2) 
print(y) 
