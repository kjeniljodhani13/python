import turtle

def draw_sky():
    turtle.penup()
    turtle.goto(-400, 200)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("sky blue")
    for _ in range(2):
        turtle.forward(800)
        turtle.right(90)
        turtle.forward(400)
        turtle.right(90)
    turtle.end_fill()

turtle.shape("turtle")
turtle.speed(3)

draw_sky()

def draw_grass(): 
 turtle.penup()
 turtle.goto(-1000, 800)
 turtle.pendown()
 turtle.begin_fill()
 turtle.color("green")
for _ in range(2):
        turtle.forward(800)
        turtle.right(90)
        turtle.forward(400)
        turtle.right(90)
turtle.end_fill()

turtle.done()

