import turtle
import time

def draw_heart(pen, color, pos, size):
    pen.penup()
    pen.goto(pos)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    pen.setheading(140)  # Reset to starting angle
    pen.forward(size * 1.13)
    for _ in range(100):
        pen.right(2)
        pen.forward(size * 0.02)  # Adjust size scaling
    pen.left(120)
    for _ in range(100):
        pen.right(2)
        pen.forward(size * 0.02)
    pen.forward(size * 1.12)
    pen.end_fill()
    pen.setheading(0)  # Reset heading to avoid affecting subsequent drawing

def draw_line(pen, start_pos, end_pos, color):
    pen.penup()
    pen.goto(start_pos)
    pen.pendown()
    pen.color(color)
    pen.width(2)
    x1, y1 = start_pos
    x2, y2 = end_pos
    steps = 100
    for i in range(steps + 1):
        x = x1 + (x2 - x1) * i / steps
        y = y1 + (y2 - y1) * i / steps
        pen.goto(x, y)
        time.sleep(0.02)

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Romantic Animation")

# Setup turtle objects
pen_man = turtle.Turtle()
pen_woman = turtle.Turtle()
pen_man_red = turtle.Turtle()  # New man in red
pen_heart = turtle.Turtle()
pen_line = turtle.Turtle()
pen_text = turtle.Turtle()

for pen in [pen_man, pen_woman, pen_man_red, pen_heart, pen_line, pen_text]:
    pen.hideturtle()
    pen.speed(10)

# Draw the original man
pen_man.color("blue")
pen_man.penup()
pen_man.goto(-200, -100)
pen_man.pendown()
pen_man.circle(50)  # Head
pen_man.penup()
pen_man.goto(-200, -150)
pen_man.pendown()
pen_man.goto(-200, -250)  # Body
pen_man.goto(-250, -300)  # Left leg
pen_man.penup()
pen_man.goto(-200, -250)
pen_man.pendown()
pen_man.goto(-150, -300)  # Right leg
pen_man.penup()
pen_man.goto(-200, -200)
pen_man.pendown()
pen_man.goto(-250, -150)  # Left arm
pen_man.penup()
pen_man.goto(-200, -200)
pen_man.pendown()
pen_man.goto(-150, -150)  # Right arm

# Draw heart on original man
pen_heart.color("red")
draw_heart(pen_heart, "red", (-200, -180), 10)  # Increased size to 10

# Draw the woman
pen_woman.color("pink")
pen_woman.penup()
pen_woman.goto(200, -100)
pen_woman.pendown()
pen_woman.circle(50)  # Head
pen_woman.penup()
pen_woman.goto(200, -150)
pen_woman.pendown()
pen_woman.goto(200, -250)  # Body
pen_woman.goto(250, -300)  # Left leg
pen_woman.penup()
pen_woman.goto(200, -250)
pen_woman.pendown()
pen_woman.goto(150, -300)  # Right leg
pen_woman.penup()
pen_woman.goto(200, -200)
pen_woman.pendown()
pen_woman.goto(250, -150)  # Left arm
pen_woman.penup()
pen_woman.goto(200, -200)
pen_woman.pendown()
pen_woman.goto(150, -150)  # Right arm

# Draw connecting line between original man and woman
pen_line.speed(1)
draw_line(pen_line, (-200, -180), (200, -180), "red")

# Draw heart on woman (before breakup)
pen_heart.speed(1)
draw_heart(pen_heart, "red", (200, -180), 10)  # Increased size to 10

# Write romantic text (before breakup)
pen_text.color("white")
pen_text.penup()
pen_text.goto(0, 180)
pen_text.write("You Complete My Heart", align="center", font=("Arial", 24, "bold"))
pen_text.goto(0, 140)
pen_text.write("(Kau Lengkapi Hatiku)", align="center", font=("Arial", 18, "italic"))
pen_text.goto(0, 100)
pen_text.write("Will You Be My Forever Love?", align="center", font=("Arial", 18, "italic"))
pen_text.goto(0, 60)
pen_text.write("(Maukah Kau Menjadi Cinta Sejatiku?)", align="center", font=("Arial", 18, "italic"))

# Wait for a while before breakup
time.sleep(5)

# Change text for breakup
pen_text.clear()  # Clear previous text
pen_text.color("pink")
pen_text.penup()
pen_text.goto(0, 180)
pen_text.write("No, I can't stay with you.", align="center", font=("Arial", 26, "bold"))
pen_text.goto(0, 140)
pen_text.write("(Tidak, aku tidak bisa tinggal bersamamu)", align="center", font=("Arial", 20, "italic"))
pen_text.goto(0, 100)
pen_text.write("Because I already love another man, Who is better, richer, and more handsome than you", align="center", font=("Arial", 20, "italic"))
pen_text.goto(0, 60)
pen_text.write("(Karena aku sudah mencintai pria lain, Yang lebih baik, lebih kaya, dan lebih tampan darimu)", align="center", font=("Arial", 20, "italic"))

# Change hearts to show breakup
pen_heart.color("black")
draw_heart(pen_heart, "black", (-200, -180), 10)  # Man's heart turns black
draw_heart(pen_heart, "pink", (200, -180), 10)   # Woman's heart stays pink (but connected to new man)

# Change connecting line to black
draw_line(pen_line, (-200, -180), (200, -180), "black")

# Draw new man (in red) after the breakup
pen_man_red.color("red")
pen_man_red.penup()
pen_man_red.goto(100, -100)
pen_man_red.pendown()
pen_man_red.circle(50)  # New man's head
pen_man_red.penup()
pen_man_red.goto(100, -150)
pen_man_red.pendown()
pen_man_red.goto(100, -250)  # Body
pen_man_red.goto(50, -300)  # Left leg
pen_man_red.penup()
pen_man_red.goto(100, -250)
pen_man_red.pendown()
pen_man_red.goto(150, -300)  # Right leg
pen_man_red.penup()
pen_man_red.goto(100, -200)
pen_man_red.pendown()
pen_man_red.goto(50, -150)  # Left arm
pen_man_red.penup()
pen_man_red.goto(100, -200)
pen_man_red.pendown()
pen_man_red.goto(150, -150)  # Right arm

# Draw heart on new man
draw_heart(pen_heart, "red", (100, -180), 10)  # New man's heart in red

# Draw connecting line from woman to new man
pen_line.color("red")
draw_line(pen_line, (200, -180), (100, -180), "red")

# Keep the window open
turtle.done()
