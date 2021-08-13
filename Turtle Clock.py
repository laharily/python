import turtle
wn = turtle.Screen()
tess = turtle.Turtle()

tess.penup()
tess.goto(0,-150)
tess.pendown()
tess.circle(150)
tess.penup()
tess.goto(0,0)
tess.left(90)

for x in range(12):
    tess.forward(130)
    tess.pendown()
    tess.forward(20)
    tess.penup()
    tess.goto(0,0)
    tess.right(30)

def moveHands(hour,minute):
    tess.right(hour*30)
    tess.right(minute*0.5)
    tess.pendown()
    tess.color("red")
    tess.forward(100)
    tess.penup()
    tess.goto(0,0)
    tess.left(hour*30)
    tess.left(minute*0.5)
    tess.right(minute*6)
    tess.pendown()
    tess.color("blue")
    tess.forward(115)
 

moveHands(12,30)
wn.mainloop()

