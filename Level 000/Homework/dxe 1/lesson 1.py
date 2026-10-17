from turtle import *

width(3)
speed(20)
color('brown')

# walls
begin_fill()
for i in range(4):
    forward(200)
    left(90)
end_fill()

# door
color('black')
begin_fill()
forward(80)
left(90)
forward(90)
right(90)
forward(40)
right(90)
forward(90)
end_fill()

# windows
color('cyan')
begin_fill()
penup()
goto(30, 120)
setheading(0)
pendown()

begin_fill()
for i in range(4):
    forward(40)
    left(90)
end_fill()

penup()
goto(130, 120)
setheading(0)
pendown()

begin_fill()
for i in range(4):
    forward(40)
    left(90)
end_fill()

# roof
color('black')
begin_fill()
penup()
goto(200, 200)
setheading(0)
pendown()

left(135)
forward(140)
left(90)
forward(140)
left(135)
forward(200)
end_fill()

exitonclick()




