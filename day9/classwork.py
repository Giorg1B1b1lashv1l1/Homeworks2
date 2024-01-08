from turtle import*
def drow_square():
    for i in range(4):
        forward(100)
        left(90)

def kalmis_wageba(x,y):
    penup()
    goto(x,y)
    pendown()

drow_square()
kalmis_wageba(0,200)

drow_square()
kalmis_wageba(-200,200)

drow_square()
kalmis_wageba(-200,0)

drow_square()
exitonclick()