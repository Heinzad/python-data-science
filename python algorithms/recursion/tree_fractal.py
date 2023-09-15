"""tree_fractal.py""" 

from turtle import * 
tree = Turtle() 
windo = tree.getscreen()

def grow(distance, tree): 
    if distance > 5: 
        tree.forward(distance) 
        tree.right(20) 
        grow(distance - 15, tree) 
        tree.left(40) 
        grow(distance - 10, tree) 
        tree.right(20) 
        tree.backward(distance) 

 
tree.left(90) 
tree.up() 
tree.backward(300) 
tree.down() 
tree.color('green') 

grow(110,tree) 

windo.exitonclick() 

