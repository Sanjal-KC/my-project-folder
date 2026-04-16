import turtle
import random

# This is the UTOPIA VISUALISER PARKING SYSTEM
# IT CONTAINS TOTAL 6 SECTIONS CONTAINING 2 ROWS , EACH CONTAINING 6 COLUMNS OF SQUARE
# EACH SQUARE REPRESENTS THE PARKING SPOT
turtle.setup(width=3000, height=3000)
turtle.speed(0)
STEP_SIZE = 50
SECTION_GAP = 50


"""def legend():   # Graph Style Legend for the VISUALISER SYSTEM
    turtle.penup()
    turtle.goto(-400, 350 - 10 * 50)
    for x in range(1):
        turtle.pendown()
        turtle.fillcolor("Red")
        turtle.begin_fill()
        for side in range(4):
            turtle.forward(50)
            turtle.right(90)
        turtle.end_fill()
        """


def draw_square(STEP_SIZE, available):
    if available:
        turtle.fillcolor("Red")
    else:
        turtle.fillcolor("White")
    turtle.begin_fill()
    for side in range(4):
        turtle.forward(STEP_SIZE)
        turtle.right(90)
    turtle.end_fill()


def letterprint(code):
    turtle.forward(STEP_SIZE / 2)
    for x in range(6):
        turtle.write(chr(code + x))
        turtle.forward(STEP_SIZE)


def block(x_axis, code, availability):
    turtle.penup()
    y_axis = 350
    turtle.goto(x_axis, y_axis)
    turtle.pendown()
    for SECTION in range(3):
        for ROW in range(2):
            turtle.pendown()
            for COLUMN in range(6):
                available = random.random() < availability
                draw_square(STEP_SIZE, available)
                turtle.forward(STEP_SIZE)
            turtle.penup()
            next = y_axis - ((ROW + 1) * STEP_SIZE)
            turtle.goto(x_axis, next)

        y_axis = next - SECTION_GAP
        turtle.penup()
        turtle.goto(x_axis, y_axis)

    letterprint(code)


def menu():
    block1_x_axis = -400
    block2_x_axis = 150
    print("Check-in Hour\tSpot Avaibility")
    print("-" * 32)
    print("1) 7-11\t\t20%\n2) 12-17\t50%\n3) 18-23,0-6\t80%")
    u_inp = int(input("Please Enter your Choice: "))
    CODE_A = 65
    CODE_G = 71
    if u_inp == 1:
        availability = 0.2
        block(block1_x_axis, CODE_A, availability)
        block(block2_x_axis, CODE_G, availability)

    elif u_inp == 2:
        availability = 0.5
        block(block1_x_axis, CODE_A, availability)
        block(block2_x_axis, CODE_G, availability)
    elif u_inp == 3:
        availability = 0.8
        block(block1_x_axis, CODE_A, availability)
        block(block2_x_axis, CODE_G, availability)
    else:
        print("Invalid Input")


# legend()
menu()


turtle.exitonclick()
