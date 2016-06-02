# This program draws the nth generation of the Dragon Curve L-System.
#
# Rules:
# turn right = 0
# turn left = 1

import turtle
# create a window to draw in
window = turtle.Screen()
window.bgcolor("black")

def create_complement(move_list):
    middle_index = len(move_list)/2
    middle = move_list[middle_index]
    complement = (middle+1)%2
    move_complement = list(move_list)
    move_complement[middle_index] = complement
    return move_complement

def iterate(dragon, stop_iteration):
    iteration = 0
    while iteration <= stop_iteration:
        append_moves = create_complement(dragon)
        dragon = dragon + [1] + append_moves
        iteration +=1
    return dragon

def draw_dragon(artist_turtle, dragon_initial, stop_iteration):
    dragon = iterate(dragon_initial, stop_iteration)
    n= 1 # segment length
    artist_turtle.forward(n)
    for move in dragon:
        if move == 0:
            artist_turtle.right(90)
            artist_turtle.forward(n)
        else:
            artist_turtle.left(90)
            artist_turtle.forward(n)

def create_dragon():
    # initial conditions for dragon
    dragon_initial = [1]
    stop_iteration = 13

    # create artist turtle
    mushu = turtle.Turtle()
    mushu.shape('turtle')
    mushu.color('white')
    mushu.speed(400)

    draw_dragon(mushu, dragon_initial, stop_iteration)

create_dragon()

window.exitonclick()
