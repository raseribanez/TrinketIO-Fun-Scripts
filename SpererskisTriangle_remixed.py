# Ben Woodfield
# This was originally a code I found in a forum
# The original made a triangle and kept adding a smaller one
# to the left corner

# I was just playing around with the positioning of some of the loops
# And watching the effect they have on the drawing...
# I nested the loop (3rd  function down) and it awesomely did this!


import turtle

def drawTriangle(points,color,myTurtle):
  myTurtle.fillcolor(color)
  myTurtle.up()
  myTurtle.goto(points[0][0],points[0][1])
  myTurtle.down()
  myTurtle.begin_fill()
  myTurtle.goto(points[1][0],points[1][1])
  myTurtle.goto(points[2][0],points[2][1])
  myTurtle.goto(points[0][0],points[0][1])
  myTurtle.end_fill()

def getMid(p1,p2):
  return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points,degree,myTurtle):
  colormap = ['blue','red','green','white','yellow',
  'violet','orange']
  drawTriangle(points,colormap[degree],myTurtle)
  if degree > 0:
      sierpinski([points[0],

      getMid(points[0], points[1]),
      getMid(points[0], points[2])],
      degree-1, myTurtle)
      sierpinski([points[1],
      getMid(points[0], points[1]),
      getMid(points[1], points[2])],
      degree-1, myTurtle)
      sierpinski([points[2],
      getMid(points[2], points[1]),
      getMid(points[0], points[2])],
      degree-1, myTurtle)

def main():
  myTurtle = turtle.Turtle()
  myWin = turtle.Screen()
  myPoints = [[-100,-50],[0,100],[100,-50]]
  sierpinski(myPoints,3,myTurtle)
  myWin.exitonclick()

main()
