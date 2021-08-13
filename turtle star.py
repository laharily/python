import turtle
wn = turtle.Screen()
alex = turtle.Turtle()

for x in range(5):
    alex.forward(50)
    alex.left(72)
    alex.forward(50)
    alex.right(144)
    alex.write(str(x))

wn.mainloop()
