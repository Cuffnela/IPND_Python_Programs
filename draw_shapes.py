# this program draws shapes

import turtle
# create a window to draw in
window = turtle.Screen()
window.bgcolor("black")

def draw_square(artist_turtle, side_length):
    artist_turtle.speed(20)
    deg0 = 0
    while deg0 <360:
        deg1 = 0
        while deg1 <360:
            artist_turtle.forward(side_length)
            artist_turtle.right(90)
            deg1 += 90
        deg0 += 10
        artist_turtle.right(10)


def draw_circle(artist_turtle, radius):
    artist_turtle.setpos(0,-100)
    artist_turtle.circle(radius)

def draw_equilateral_triangle(artist_turtle, side_length):
    deg = 0
    while deg<360:
        artist_turtle.forward(side_length)
        artist_turtle.right(120)
        deg += 120

def create_art():
    # Create jeff the turtle
    jeff = turtle.Turtle() # get a turtle
    jeff.shape("turtle") # make jeff a real turtle
    jeff.color("green") # make jeff a yellow turtle

    # Create betty the turtle
    betty = turtle.Turtle()
    betty.shape('turtle')
    betty.color('white')

    # Create jody the turtle
    jody = turtle.Turtle() # get another turtle
    jody.shape('turtle')
    jody.color('blue')

    draw_square(jeff, 100)
    draw_circle(jody, 100)
    draw_equilateral_triangle(betty, 100)

create_art()

window.exitonclick()
