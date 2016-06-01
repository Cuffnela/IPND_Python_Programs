# this program draws shapes

import turtle
# create a window to draw in
window = turtle.Screen()
window.bgcolor("black")

def draw_square(side_length):
    jeff = turtle.Turtle() # get a turtle
    jeff.shape("turtle") # make jeff a real turtle
    jeff.color("green") # make jeff a yellow turtle
    jeff.speed(20)
    # tell jeff where to to
    deg0 = 0
    while deg0 <360:
        deg1 = 0
        while deg1 <360:
            jeff.forward(side_length)
            jeff.right(90)
            deg1 += 90
        deg0 += 10
        jeff.right(10)


def draw_circle(radius):
    jody = turtle.Turtle() # get another turtle
    jody.shape('turtle')
    jody.color('blue')
    jody.setpos(0,-100)
    jody.circle(radius)

def draw_equilateral_triangle(side_length):
    betty = turtle.Turtle()
    betty.shape('turtle')
    betty.color('white')
    deg = 0
    while deg<360:
        betty.forward(side_length)
        betty.right(120)
        deg += 120

draw_square(100)
draw_circle(100)
draw_equilateral_triangle(100)

window.exitonclick()
