# Ben Woodfield
# A lotof these Turtle Graphics were done using a tutorial so I can't say they are
# my own work - I did rewrite them but I didn't design them originally

import turtle 

seurat = turtle.Turtle()

dot_distance = 25
width = 5
height = 7

seurat.penup()

for y in range(height):
    for i in range(width):
        seurat.dot()
        seurat.forward(dot_distance)
    seurat.backward(dot_distance * width)
    seurat.right(90)
    seurat.forward(dot_distance)
    seurat.left(90)
    
turtle.done()
