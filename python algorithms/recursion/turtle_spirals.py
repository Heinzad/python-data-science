
# Drawin a spiral with turtle graphics 

from turtle import * 

turtie = Turtle() 
winnie = turtie.getscreen() 

def spiralizer(turtie, distance): 
    if distance > 0: 
        turtie.forward(distance) 
        turtie.right(90) 
        spiralizer(turtie, distance - 5) 

spiralizer(turtie, 100) 
winnie.exitonclick() 
