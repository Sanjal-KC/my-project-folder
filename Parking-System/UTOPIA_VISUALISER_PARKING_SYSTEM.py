import turtle
import random

# This is the UTOPIA VISUALISER PARKING SYSTEM
# IT CONTAINS TOTAL 6 SECTIONS CONTAINING 2 ROWS , EACH CONTAINING 6 COLUMNS OF SQUARE
# EACH SQUARE REPRESENTS THE PARKING SPOT

# CONSTRAINT - Cannot USE LIST,TUPLE , DICTIONARY AND SET
turtle.setup(width=3000, height=3000)
turtle.speed(0)
STEP_SIZE = 50
SECTION_GAP = 50


def legend_item(x_axis, available):
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(x_axis, -150)
    draw_square(STEP_SIZE / 2, available)
    turtle.forward(STEP_SIZE / 2)
    turtle.right(90)
    turtle.forward(STEP_SIZE / 4)
    turtle.left(90)
    turtle.forward(STEP_SIZE / 4)
    if available:
        turtle.write("Available", align="left", font=("Arial", 10, "bold"))
    else:
        turtle.write("Unavailable", align="left", font=("Arial", 10, "bold"))


def legend():  # Graph Style Legend for the VISUALISER SYSTEM which draws each individual Legend item
    legend_item(-400, True)
    legend_item(-300, False)


def draw_square(step_size, available):
    turtle.pendown()
    if available:
        turtle.fillcolor("white")
    else:
        turtle.fillcolor("red")
    turtle.begin_fill()
    for side in range(4):
        turtle.forward(step_size)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()


def letterprint(code):
    turtle.setheading(0)
    turtle.forward(STEP_SIZE / 2)
    for i in range(6):
        turtle.write(chr(code + i), align="left", font=("Arial", 10, "bold"))
        turtle.forward(STEP_SIZE)


def block(x_axis, code, availability):
    turtle.penup()
    y_axis = 350
    turtle.goto(x_axis, y_axis)
    turtle.pendown()
    for SECTION in range(3):
        for ROW in range(2):
            for COLUMN in range(6):
                available = random.random() < availability
                draw_square(STEP_SIZE, available)
                turtle.forward(STEP_SIZE)
            next_y = y_axis - ((ROW + 1) * STEP_SIZE)
            turtle.goto(x_axis, next_y)

        y_axis = next_y - SECTION_GAP
        turtle.goto(x_axis, y_axis)
    letterprint(code)


def block_caller(availability):
    block1_x_axis = -400
    block2_x_axis = 150
    CODE_A = 65
    CODE_G = 71
    block(block1_x_axis, CODE_A, availability)
    block(block2_x_axis, CODE_G, availability)


def menu():
    print("Check-in Hour\tSpot Avaibility")
    print("-" * 32)
    while True:
        try:
            print("1) 7-11\t\t20%\n2) 12-17\t50%\n3) 18-23,0-6\t80%")
            u_inp = int(input("Please Enter your Choice(1-3): "))
            break
        except ValueError:
            print("Invalid Input.")

    legend()
    if u_inp == 1:
        availability = 0.2
        block_caller(availability)

    elif u_inp == 2:
        availability = 0.5
        block_caller(availability)
    elif u_inp == 3:
        availability = 0.8
        block_caller(availability)

    else:
        print("Invalid Input")


menu()


turtle.exitonclick()
