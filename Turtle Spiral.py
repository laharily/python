import turtle
wn = turtle.Screen()
alex = turtle.Turtle()

forward = 10

for x in range(50):
    alex.forward(forward)
    alex.left(90)
    forward += 10

wn.mainloop()
