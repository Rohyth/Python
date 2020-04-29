#for loops

import turtle
from time import sleep

nw = turtle.Turtle()
nw.speed(15)

def square():
    nw.forward(100)
    nw.right(90)
    

for x in range(10):
    square()
    nw.forward(50)
    square()
    
sleep(2)
turtle.bye()