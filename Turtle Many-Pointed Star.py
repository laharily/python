import turtle

n = int(input("Enter an odd number that is at least 3: "))
wn = turtle.Screen()
lahari = turtle.Turtle()
lahari.speed(10)

angle = 180 - 180/n
forlen = 200

for x in range(n):
    lahari.left(angle)
    lahari.forward(forlen)

lahari.hideturtle()
wn.mainloop()
