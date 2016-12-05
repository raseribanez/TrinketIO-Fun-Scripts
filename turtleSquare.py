import turtle

def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)
    for i in range(4):
        t.forward(sz)
        t.right(90)
    for i in range(8):
        t.forward(sz)
        t.back(45)
    

wn = turtle.Screen()
wn.bgcolor("blue")

ben = turtle.Turtle()
drawSquare(ben,50)

wn.exitonclick()
