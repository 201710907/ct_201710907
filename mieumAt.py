import turtle

wn = turtle.Screen() 
t1 = turtle.Turtle()

def giyuk(size):
    f1.fd(size)
    t1.right(90)
    t1.fd(size)
    
def nieun(size):
    t1.right(90)
    t1.fd(size)
    t1.left(90)
    t1.fd(size)
    
def mieum(size):
    giyuk(size)
    nieun(size)
    
def giyukAt(size, at):
    t1.penup
    t1.goto(at, 0)
    t1.setheading(0)
    t1.pendown()
    t1.pos()
    t1.write(t1.pos())
    giyuk(size)
    
def nieunAt(size, at):
    t1.penup
    t1.goto(at, 0)
    t1.setheading(0)
    t1.pendown()
    t1.pos()
    t1.write(t1.pos())
    nieun(size)
    
def mieumAt(size, at):
    t1.penup
    t1.goto(at, 0)
    t1.setheading(0)
    t1.pendown()
    t1.pos()
    t1.write(t1.pos())
    mieum(size)

