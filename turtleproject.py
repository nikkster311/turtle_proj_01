import turtle

#draw basic shapes
#use those to make more complex shapes
#run whole thing in a function


def tri(name): # draws individual triangle
    name.begin_fill()
    for i in range(3):
        name.speed(1)
        name.forward(50)
        name.left(120)
    name.end_fill()

def tri_cubed(name):    #draws set of three individual triangles
    turn = 0
    for i in range(3):
        tri(name)
        name.forward(50)
        name.left(turn)
        if turn == 120:
            name.forward(50)
        turn += 120


def triforce(name): # draws 3 sets of 3 small triangles
    for i in range(3):
        tri_cubed(name)
        name.left(120)
    name.forward(100)
    name.right(120)
    name.forward(100)



def final(name):
    for i in range(3):
        triforce(name)



def run():
    window = turtle.Screen()
    window.bgcolor('gold') # changes background color

    tri = turtle.Turtle()
    tri.fillcolor('blue') # changes the fill color of the triangles (in tri())
    final(tri)

    window.exitonclick() # exit turtle when clicking on window


run()