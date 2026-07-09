import turtle

screen = turtle.Screen()
screen.title("Olympic Rings")


pen = turtle.Turtle()
pen.pensize(5)


def draw_circle(x, y, color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.pencolor(color)
    pen.circle(50)


draw_circle(-120, 0, "blue")
draw_circle(0, 0, "black")
draw_circle(120, 0, "red")
draw_circle(-60, -60, "yellow")
draw_circle(60, -60, "green")


turtle.done()
