import turtle
sides = input ("Enter the number of sides.")
length = input ("Enter the length of the sides.")
color = input ("Enter a color.")

w = turtle.Screen()
t = turtle.Turtle();
t.shape("turtle")
t.color(color)
t.speed(1)
angle = sides/360
for x in range (0,sides):
    t.forward(length)
    t.left(angle)
