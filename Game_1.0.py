import turtle as t
import random as r
import math as m
import os as o

# screen
w = t.Screen()
w.bgcolor('green')
w.title('Game1.0')
# w.bgpic('space.gif')

# boundary
p = t.Turtle()
p.color('black')
p.penup()
p.speed(0)
p.setposition(-660, -330)
p.pendown()
p.pensize(45)
p.fd(1320)
p.lt(90)
p.fd(670)
p.lt(90)
p.fd(1320)
p.lt(90)
p.fd(670)
p.lt(90)
p.hideturtle()


# player
s = t.Turtle()
s.shape('triangle')
s.color('purple')
s.penup()
s.speed(0)
s.setheading(90)
s.setposition(0, -250)
# s.pendown()

# elixir
e = t.Turtle()
e.penup()
e.shape('circle')
e.speed(0)
e.color('yellow')
e.setposition(0, 250)

# const speed
d = 1

# e=edible,s=player1
# collision
def col(s, e):
    n = m.sqrt(m.pow(s.xcor() - e.xcor(), 2) + m.pow(s.ycor() - e.ycor(), 2))
    if n < 20:
        s.color('purple')
        return True
    else:
        return False


# commands
def tl():
    s.left(30)


def tr():
    s.right(30)


def ut():
    s.color('blue')
    global d
    d -= 1


def up():
    s.color('red')
    global d
    d += 1


# keyboard keys
t.listen()
t.onkey(tl, 'Left')
t.onkey(tr, 'Right')
t.onkey(ut, 'Down')
t.onkey(up, 'Up')

g = 0
f = 2
# motion
while True:
    s.forward(d)

    if s.xcor() > 650 or s.xcor() < -650:
        s.right(r.randint(60, 180))
    if s.ycor() > 335 or s.ycor() < -335:
        s.right(r.randint(60, 180))

    if col(s, e):
        e.setposition(r.randint(-630, 630), r.randint(-310, 310))
        e.right(r.randint(0, 359))
        g += 10
        f += 1
        p.undo()
        p.up()
        p.hideturtle()
        p.setposition(-652,320)
        p.color('white')
        p.write(f'Score : {g}', font='Arial')


    e.forward(f)

    if e.xcor() > 650 or e.xcor() < -650:
        e.right(r.randint(60, 180))
    if e.ycor() > 335 or e.ycor() < -335:
        e.right(r.randint(60, 180))


# keeping screen window open until user respond
w.mainloop()
