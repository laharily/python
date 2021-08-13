import turtle

w = turtle.Screen()
t = turtle.Turtle();#def dir is East
t.shape("turtle");
t.color("green")
t.speed(1);
#drawing a triangle
t.left(45);
t.forward(100)
t.right(90);
t.forward(100)
t.left(-135);
t.forward(140)

t.penup();
t.forward(100);
t.pendown();
#drawing a square
t.forward(100);
t.left(90);
t.forward(100);
t.left(90);
t.forward(100);
t.left(90);
t.forward(100);

t.penup();
t.forward(100);
t.pendown();
#drawing a circle
t.circle(30);

t.penup();
t.forward(100)
t.pendown();
#drawing a pentagon
t.circle(50,360,5);

t.penup();
t.forward(100);
t.pendown();
#drawing an octagon
t.circle(60,360,8);

t.penup();
t.forward(100);
t.pendown();

