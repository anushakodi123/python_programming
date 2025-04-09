from jupyturtle import penup, pendown, forward, left, make_turtle

def jump(length):
    """Move the turtle forward without drawing."""
    penup()
    forward(length)
    pendown()

jump(5)


# def rectangle(length, width):
#     for i in range(2):
#         forward(length)
#         left(90)
#         forward(width)
#         left(90)

# rectangle(80, 40)

# def rhombus(length, angle):
#     for i in range(2):
#         forward(length)
#         left(angle)
#         forward(length)
#         left(180 - angle)

# rhombus(50, 60)

def parallelogram(length, angle):
    for i in range(2):
        forward(length)
        left(angle)
        forward(length)
        left(180 - angle)

make_turtle()
parallelogram(50, 90)


def triangle(length):
    for i in range(3):
        forward(length)
        left(120)


