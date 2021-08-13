import turtle
import random

w = turtle.Screen()
t = turtle.Turtle();
t.shape("arrow");
t.color("brown")

x = -250
y = 150
for a in range (0,6):
    y = y-50
    t.penup()
    t.setpos(x,y)
    t.pendown()
    t.forward(500)


x = -250
y = 75
pink = turtle.Turtle()
pink.shape("turtle")
pink.color('pink')
pink.penup()
pink.setpos(x,y)
pink.pendown()

px = -250
py = 25
purple = turtle.Turtle()
purple.shape("turtle")
purple.color('purple')
purple.penup()
purple.setpos(px,py)
purple.pendown()

rx = -250
ry = -25
red = turtle.Turtle()
red.shape("turtle")
red.color('red')
red.penup()
red.setpos(rx,ry)
red.pendown()

ox = -250
oy = -125
orange = turtle.Turtle()
orange.shape("turtle")
orange.color('orange')
orange.penup()
orange.setpos(ox,oy)
orange.pendown()

bx = -250
by = -75
blue = turtle.Turtle()
blue.shape("turtle")
blue.color('blue')
blue.penup()
blue.setpos(bx,by)
blue.pendown()

while x <= 230 and px <= 230 and rx <= 230 and ox <= 230 and bx <= 230:
    rp = random.randrange(1,7)
    pink.forward(rp)
    x = x+rp
    rpu = random.randrange(1,7)
    purple.forward(rpu)
    px = px+rpu
    rr = random.randrange(1,7)
    red.forward(rr)
    rx = rx+rr
    ro = random.randrange(1,7)
    orange.forward(ro)
    ox = ox+ro
    rb = random.randrange(1,7)
    blue.forward(rb)
    bx = bx+rb
    
# I have move the pink turtle forward until its x coordinate is 250.
