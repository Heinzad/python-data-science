
# Recursive List Sum 
def recursum(numbers): 
    # Escape Clause: 
    if len(numbers) == 1: 
        return numbers[0]
    else: 
        # calls itself 
        return numbers[0] + recursum(numbers[1:]) 
    