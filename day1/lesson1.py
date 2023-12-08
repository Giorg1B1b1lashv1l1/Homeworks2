from turtle  import*
#we want to paint house

#step 1: draw a square
speed(20)
width(7)
begin_fill()
color("yellow")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#step2: draw a door
forward(75)
color("black")
left(90)
forward(100)
right(90)
forward(50)
right(90)
forward(100)
right(90)
color("yellow")
forward(90)
left(90)

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#now we should draw a windows
penup()
goto(130,130)
pendown()
color("white")
begin_fill()
left(120)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()


penup()
goto(20,130)
pendown()
color("white")
begin_fill()
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()



exitonclick() 