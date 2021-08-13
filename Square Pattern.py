import turtle

def drawSquare(t, size):
    for x in range(10):
        for x in range(4):
            t.forward(size)
            t.right(90)
        t.penup()
        t.backward(10)
        t.left(90)
        t.forward(10)
        t.pendown()
        t.right(90)
        size += 20
        
        
wn = turtle.Screen()
t = turtle.Turtle()
drawSquare(t, 5)

wn.mainloop()
