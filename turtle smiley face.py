# A smiley face, by DPatrick
import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
dave = turtle.Turtle()    # Create a turtle, assign to dave

# draw the head
dave.circle(100)
# draw the eyes in blue
dave.penup()
dave.fillcolor('blue')
dave.goto(-50,120)
dave.begin_fill()
dave.circle(20)
dave.end_fill()
dave.goto(50,120)
dave.begin_fill()
dave.circle(20)
dave.end_fill()
# draw the nose
dave.pensize(15)
dave.goto(0,120)
dave.setheading(270)
dave.pendown()
dave.forward(40)
dave.penup()
# draw the mouth in red
dave.pensize(10)
dave.color('red')
dave.goto(-80,60)
dave.pendown()
dave.setheading(-30)
for i in range(11):
    dave.forward(15)
    dave.left(6)

wn.mainloop()
