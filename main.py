import turtle
t=turtle.Turtle()
t.speed(5)

def circle1(r,c):
    t.color(c)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

t.penup()
t.goto(-30,-280)
t.pendown()

circle1(250,'red')
t.goto(-30,-240)
circle1(210,'white')
t.goto(-30,-200)
circle1(170,'red')
t.goto(-30,-160)
circle1(130,'blue')

t.goto(-153,11)
t.begin_fill()
t.color("white")
for i in range(5):
    t.forward(245)
    t.right(144)
t.end_fill()

t.hideturtle()
turtle.done()
