import turtle            # allows the use of turtles
wn = turtle.Screen()     # creates a screen for the turtle
lahari = turtle.Turtle() # creates a new turtle

lahari.penup()           # gives the turtle some space
lahari.back(200)
lahari.pendown()

for x in range(8):       # draws 8 squares
    lahari.forward(50)
    lahari.right(90)
    lahari.forward(50)
    lahari.right(90)
    lahari.forward(50)
    lahari.right(90)
    lahari.forward(50)
    lahari.right(90)
    lahari.forward(50)

wn.mainloop()
    
