import turtle

class SpecialTurtle(turtle.Turtle):
    # handler methods
    def move_forward(self):
        self.forward(50)
    def turn_left(self,x,y):
        self.left(45)
    def turn_right(self,x,y):
        self.right(45)

# initialize window and turtle
wn = turtle.Screen()
alex = SpecialTurtle()

# listeners
wn.onkey(alex.move_forward,"space") # spacebar press
wn.onclick(alex.turn_left)    # left button press
wn.onclick(alex.turn_right,2) # right button press (2-button mouse)
wn.onclick(alex.turn_right,3) # right button press (3-button mouse)

# have the window listen and wait
wn.listen()
wn.mainloop()
