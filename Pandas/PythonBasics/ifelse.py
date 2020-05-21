import turtle
from time import sleep

nw = turtle.Turtle()
def square():
    for i in range(4):
        nw.forward(100)
        nw.right(90)


for y in range(4):
    square()
    nw.right(90)
    nw.forward(100)


sleep(5)
turtle.bye()


a = 5
b = 7

if a > b:
    print('A is grater')
else:
    print('B is greater')
    
    
usr = ''
pwd = ''

if ((usr == '') & (pwd == '')):
    print('incorrect')
else:
    print('correct')



l = [1,2,3]

for x in range(3,100):
    l.append(x)











