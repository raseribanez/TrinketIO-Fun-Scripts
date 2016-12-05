# Ben Woodfield
# Nice and simple, draws a star in a spiral fashion
# Also from a tutorial 

import turtle 

spiral = turtle.Turtle()

for i in range(20):
    spiral.forward(i * 10)
    spiral.right(144)
    
turtle.done()
