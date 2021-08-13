import random
import turtle
wn = turtle.Screen()

def random_walk(t,steps):
    for x in range(steps):
        r = random.randint(1,50)
        r2 = random.randint(10,180)
        t.forward(r)
        t.left(r2)
        x += 1
    t.hideturtle()    

random_walk(turtle.Turtle(), 50)
wn.mainloop()

    
