import turtle
from time import sleep

nw = turtle.Turtle()
def square():
    for i in range(4):
        nw.forward(100)
        nw.right(90)

'''    
square()
nw.forward(100)
square()
sleep(5)
turtle.bye()
'''

a = 10
b = 5

if a < b:
    square()
    sleep(3)
    turtle.bye()
else:
    nw.forward(50)    
    sleep(3)
    turtle.bye()
    




    