
import turtle
from time import sleep

nw = turtle.Turtle()

def square():
    for p in range(4):
        nw.forward(100)
        nw.right(90)
        print(p)

square()

'''
for x in range(4):
    square()
    nw.forward(100)
'''

sleep(5)
turtle.bye()

'''
nw = turtle.Turtle()
def square():
    for i in range(4):
        nw.forward(100)
        nw.right(90)

square()
nw.forward(100)
square()
sleep(5)
turtle.bye()

'''

