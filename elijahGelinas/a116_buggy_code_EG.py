#   a116_buggy_image.py
import turtle as trtl

#Create spider body
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)

#Configure spider legs
numLegs = 8
legLength = 70
angle = (360 / numLegs) - 20
spider.pensize(5)

#Draw legs
loop = 0
while (loop < numLegs):
  spider.goto(0,20)
  spider.pendown()
  if (loop <= 3):
      spider.setheading(angle*loop - 45)
      spider.forward(75)
      spider.right(45)
      spider.forward(45)
  else:
      spider.setheading(angle*loop +45)
      spider.forward(75)
      spider.left(45)
      spider.forward(45)

  spider.penup()
  loop += 1

#Draws head
spider.goto(-12,-20)
spider.pensize(30)
spider.pendown()
spider.circle(10)

#Changes variables to draw eyes
spider.penup()
spider.pensize(1)
spider.pencolor("violet")
spider.fillcolor("violet")

#Eye one
spider.goto(-12, -25)
spider.begin_fill()
spider.pendown()
spider.circle(3)
spider.end_fill()

#Eye two
spider.penup()
spider.goto(2, -25)
spider.begin_fill()
spider.pendown()
spider.circle(3)
spider.end_fill()

spider.hideturtle()

wn = trtl.Screen()
wn.mainloop()