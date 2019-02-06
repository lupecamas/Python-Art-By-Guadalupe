import turtle
import random
lupe = turtle.Turtle()
lupe.speed(0)

def newshape(length, angle,color):
    lupe.color(color)

    lupe.forward(length)
    lupe.right(angle)
    lupe.forward(length)
    lupe.right(angle)
    lupe.forward(length)
    lupe.right(angle)
    lupe.forward(length)
for i in range (25):
    lupe.goto(0,0)
    newshape(100 ,2090,"black")

lupe.up


def art2(length, angle, color):
    lupe.color(color)
    lupe.forward(length)
    lupe.right(angle)
    lupe.forward(length)
    lupe.right(angle)
    lupe.forward(length)
    lupe.right(angle)
    lupe.forward(length)
    lupe.forward(length)
    
for i in range (25):
    lupe.goto(0,0)
    art2 (100,50,"red")
    




    
          
          
