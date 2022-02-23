#Tower of Hanoi visualization -guided by Dr. P. N. Singh
import turtle
peg_height = 290
def draw_line(x,y,heading,length,pensize,color):
    turtle.up()
    turtle.goto(x,y)
    turtle.seth(heading)
    turtle.down()
    turtle.color(color)
    turtle.pensize(pensize)
    turtle.fd(length)
    
def draw_scene():
    turtle.bgcolor('light blue')
    draw_line(-600,-170,0,1200,10,'brown')
    for i in range(-250,251,250):
        draw_line(i,-163,90,peg_height,5,'black')

from turtle import *

class Disc(Turtle):
    def __init__(self, n):
        Turtle.__init__(self, shape="square", visible=False)
        self.pu()
        self.shapesize(1.5, n*1.5, 2) # rectangle for disc shape
        self.fillcolor(n/6., 0, 1-n/6.)
        self.st()

class Tower(list):
    "Hanoi tower, a subclass of built-in type list"
    def __init__(self, x):
        "create an empty tower. x is x-position of peg"
        self.x = x
    def push(self, d):
        d.setx(self.x)
        d.sety(-150+34*len(self))
        self.append(d)
    def pop(self):
        d = list.pop(self)
        d.sety(150)
        return d

def hanoi(n, from_, with_, to_):
    if n > 0:
        hanoi(n-1, from_, to_, with_)
        to_.push(from_.pop())
        hanoi(n-1, with_, from_, to_)

def play():
    onkey(None,"space")
    clear()
    draw_scene()
    try:
        hanoi(disks, t1, t2, t3)
        write("Done",align="center", font=("Arial", 18, "bold"))
    except Terminator:
        pass  # turtledemo user pressed STOP

def parastoh():
    global t1, t2, t3
    ht(); penup(); goto(0, -225)   # writer turtle
    t1 = Tower(-250)
    t2 = Tower(0)
    t3 = Tower(250)
    for i in range(disks,0,-1):
        t1.push(Disc(i))
    write("Spacebar to solve the TOH puzzle",align="center", font=("Arial", 16, "bold"))
    onkey(play, "space")
    listen()
    
disks=4 # 1 to 6    
parastoh()


