import turtle

def setup_turtle(color, speed):
    t = turtle.Turtle()
    t.speed(speed)
    t.color(color)
    return t

def draw_circles(t, size, steps):
    for _ in range(steps):
        t.circle(size)
        size -= 4

def draw_special(t, size, repeat):
    for _ in range(repeat):
        draw_circles(t, size, 10)
        t.right(360 / repeat)

wn = turtle.Screen()
wn.bgcolor('black')

albert = setup_turtle('white', 0)
draw_special(albert, 100, 10)

steve = setup_turtle('yellow', 0)
draw_special(steve, 100, 10)

barry = setup_turtle('blue', 0)
draw_special(barry, 100, 10)

terry = setup_turtle('orange', 0)
draw_special(terry, 100, 10)

will = setup_turtle('pink', 0)
draw_special(will, 100, 10)

wn.mainloop()
