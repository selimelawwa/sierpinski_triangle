# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 23:08:47 2018

@author: selem
"""

import turtle

def draw_triangle(vertices,turtle,color):
    turtle.penup()#remove pen in beginning to move to location of 1st vertex of triangle to be drawn
    turtle.goto(vertices[0][0],vertices[0][1]) #go to first point in triangle
    turtle.fillcolor(color)
    turtle.pendown() #put pen to start drawing
    turtle.begin_fill()
    turtle.goto(vertices[1][0],vertices[1][1])
    turtle.goto(vertices[2][0],vertices[2][1])
    turtle.goto(vertices[0][0],vertices[0][1])
    turtle.end_fill()
    
#function to get midpoint between 2 coordinates
def mid_point(p1,p2):
    midpoint = [(p1[0]+p2[0])/2,(p1[1]+p2[1])/2]
    return midpoint
    
def draw_sierpinski_triangle(vertices,level,turtle):
    color = ['blue','green','red','brown','yellow']
    draw_triangle(vertices,turtle,color[level])
    if level > 0:
        draw_sierpinski_triangle([vertices[0],mid_point(vertices[0],vertices[1]),mid_point(vertices[0],vertices[2])],level-1,turtle)
        draw_sierpinski_triangle([vertices[1],mid_point(vertices[0],vertices[1]),mid_point(vertices[1],vertices[2])],level-1,turtle)
        draw_sierpinski_triangle([vertices[2],mid_point(vertices[0],vertices[2]),mid_point(vertices[1],vertices[2])],level-1,turtle)
    
    
    
vertices = [[0,-100],[200,300],[400,-100]]
#vertices1 = [[0,0],[100,200],[-100,200]]
#vertices2 = [[200,0],[100,200],[300,200]]

selim = turtle.Turtle()
window = turtle.Screen()
window.setup( width = 1024, height = 768, startx = None, starty = None)
selim.speed(0)
draw_sierpinski_triangle(vertices,4,selim)
selim.penup()
selim.goto(0,-250)
selim.pendown()
selim.write("Output with 4 levels",font=("Arial", 36, "bold"))
#window.bgcolor("red")
#draw_sierpinski_triangle(vertices1,3,selim)
#draw_sierpinski_triangle(vertices2,3,selim)
window.exitonclick()