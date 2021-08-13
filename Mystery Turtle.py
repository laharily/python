import turtle

turtle.setup(800,600) # Change the width of the drawing to 800px and the height to 600px.
wn = turtle.Screen()
sammy = turtle.Turtle()
sammy.ht()

inFile = open('mystery.txt','r')
for line in inFile:
    line = line.strip("\n")
    if line == "UP":
        sammy.penup()
    elif line == "DOWN":
        sammy.pendown()
    else:
        coord = line.split()
        sammy.goto(int(coord[0]),int(coord[1]))
inFile.close()
wn.mainloop()

