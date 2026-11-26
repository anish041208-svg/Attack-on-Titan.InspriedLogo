
import turtle

screen = turtle.Screen()
screen.setup(900, 700)
screen.bgcolor("#151515")
screen.title("Attack on Titan - Inspired Emblem")

t = turtle.Turtle()
t.speed(0)
t.pensize(4)
t.hideturtle()

def polygon(points, color, outline="#d6c6a2"):
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.color(outline, color)
    t.begin_fill()
    for p in points[1:]:
        t.goto(p)
    t.goto(points[0])
    t.end_fill()

# Left wing
polygon([
    (-30, 30), (-100, 110), (-210, 170),
    (-180, 105), (-300, 145), (-240, 65),
    (-350, 65), (-250, 0), (-120, -35),
    (-30, -20)
], "#e8e2d0")

# Right wing
polygon([
    (30, 30), (100, 110), (210, 170),
    (180, 105), (300, 145), (240, 65),
    (350, 65), (250, 0), (120, -35),
    (30, -20)
], "#e8e2d0")

# Central shield
polygon([
    (-30, 100), (30, 100), (55, 35),
    (35, -65), (0, -125),
    (-35, -65), (-55, 35)
], "#8b3029")

# Central sword
t.color("#e8e2d0")
t.pensize(7)
t.penup()
t.goto(0, 80)
t.pendown()
t.goto(0, -75)

t.pensize(5)
t.goto(-38, -20)
t.penup()
t.goto(0, -75)
t.pendown()
t.goto(38, -20)

# Title
t.penup()
t.goto(0, -230)
t.color("#d6c6a2")
t.write("ATTACK ON TITAN",
        align="center",
        font=("Times New Roman", 32, "bold"))

t.goto(0, -270)
t.color("#999999")
t.write("SHINZOU WO SASAGEYO",
        align="center",
        font=("Arial", 13, "bold"))

screen.mainloop()
