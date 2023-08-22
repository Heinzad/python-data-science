"""hashing.py
    Exercises from chapter 5 of 
    Miller &amp; Ranum "Problem Solving with Algoritms and Data Structrues Using Python" (second edition)
""" 

# cat as a sequence of ordinal values: 
c = ord("c") 
a = ord("a") 
t = ord("t") 

print(c)  
print(a)  
print(t)  

h_hash = (c + a + t) % 11 

print(h_hash)  
