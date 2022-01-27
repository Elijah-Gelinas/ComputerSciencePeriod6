#   a114_nested_loops_2.py 
# Elijah Gelinas, 6th period, 10/12/2021
import turtle as trtl

painter = trtl.Turtle()
painter.shape("circle")
painter.hideturtle()
painter.penup()

x = -200
while (x < 200): 
  x = x + 50
  y = -200
  painter.goto(y, x)
  painter.color("purple")
  painter.stamp()

  while (y < 100):
      y += 50
      painter.goto(y, x)
      painter.color("yellow")
      painter.stamp()
      


wn = trtl.Screen()
wn.mainloop()