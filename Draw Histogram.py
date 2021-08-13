def draw_histogram(t,dataList):
    '''draw_histogram(t,dataList) -> None
    uses turtle t to draw a histogram of dataList
    dataList must contain integers from 0-10'''
    for x in range(11):
        num = dataList.count(x) # counts how many of that number there are in the datalist
        bob.write(x)                      # numbers the bars
        # draws the rectangle
        bob.forward(20)
        bob.left(90)
        bob.forward(20*num)
        bob.left(90)
        bob.forward(20)
        bob.left(90)
        bob.forward(20*num)
        bob.left(90)
        # moves to the next one
        bob.penup()
        bob.forward(40)
        bob.pendown()

# test suite
import turtle
turtle.setup(600,300) # Change the width of the drawing to 600px and the height to 300px.
wn = turtle.Screen()
bob = turtle.Turtle()
dataList = [6,8,0,7,7,9,2,9,10,4,8,7,6,9,1,4,6,7,5,7,2,10,4,5,5,6,8]
# move bob back a little bit so he has room
bob.penup()
bob.back(200)
bob.pendown()
# draw the histogram
draw_histogram(bob,dataList)
bob.hideturtle()
wn.mainloop()
