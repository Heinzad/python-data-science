"""sierpinski_triangle.py""" 

from turtle import * 

def tri_draw(points, colour, turtel): 
    turtel.fillcolor(colour) 
    turtel.up() 
    turtel.goto(points[0]) 
    turtel.down() 
    turtel.begin_fill() 
    turtel.goto(points[1]) 
    turtel.goto(points[2]) 
    turtel.goto(points[0]) 
    turtel.end_fill() 

def get_mid(point_one, point_two): 
    return ( (point_one[0] + point_two[0]) / 2, (point_one[1] + point_two[1]) / 2) 

def sierpinski(points, degree, turtel): 
    colours = ["blue", "red", "green", "white", "yellow", "violet", "orange"] 
    tri_draw(points, colours[degree], turtel) 

    if degree > 0: 
        sierpinski(
            [points[0], get_mid(points[0], points[1]), get_mid(points[0], points[2])],
            degree -1, 
            turtel 
        ) 
        sierpinski(
            [points[1], get_mid(points[0], points[1]), get_mid(points[0], points[2])],
            degree -1, 
            turtel 
        ) 
        sierpinski(
            [points[2], get_mid(points[2], points[1]), get_mid(points[0], points[2])],
            degree -1, 
            turtel 
        ) 


turtel = Turtle() 
windo = turtel.getscreen() 
pointy = [(-500, -250), (0, 500), (500, -250)] 
sierpinski(pointy, 5, turtel) 
windo.exitonclick() 

