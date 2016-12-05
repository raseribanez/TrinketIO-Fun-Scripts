# Ben Woodfield
# I was doing an online tutorial and wrote some of these little graphics scripts
# while following the lessons

import turtle 

painter = turtle.Turtle()

painter.pencolor("blue")

for i in range(50):
    painter.forward(50)
    painter.left(123) # Let's go counterclockwise this time 
    
painter.pencolor("red")
for i in range(50):
    painter.forward(100)
    painter.left(123)
    
turtle.done()
