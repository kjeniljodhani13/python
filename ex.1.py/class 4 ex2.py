import turtle

def draw_square():
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
def draw_circle():
    turtle.circle(100)

def draw_triangle():
    for _ in range(3):
        turtle.forward(100)
        turtle.right(120)

turtle.shape("turtle")
turtle.speed(3)

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

turtle.penup()
turtle.goto(-200,-200)
turtle.pendown()
draw_square()


turtle.penup()
turtle.goto(+200,+200)
turtle.pendown()
draw_circle()

turtle.penup()
turtle.goto(-50,-50)
turtle.pendown()
draw_triangle()

turtle.done()





