# a121_catch_a_turtle.py
#-----import statements-----

import turtle as trtl
import random as rand
import leaderboard as lb

#-----game configuration----

spotColor = "black"
spotSize = 2
spotShape = "circle"

score = 0
font_setup = ("Arial", 20, "normal")

timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

colors = ("red", "blue", "green", "orange", "pink")
sizes = (1, 2, .5, 1.5, 2.5)

leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("Player name: ")
#-----initialize turtle-----

spot = trtl.Turtle()
spot.shape(spotShape)
spot.shapesize(spotSize)
spot.fillcolor(spotColor)

scoreWriter = trtl.Turtle()
scoreWriter.penup()
scoreWriter.goto(335, 285)
scoreWriter.pendown()
scoreWriter.hideturtle()

counter =  trtl.Turtle()
counter.penup()
counter.goto(-335, 285)
counter.pendown()
counter.hideturtle()


#-----game functions--------
def spotClicked(x, y):
    #print("Spot was clicked")
    global timer_up
    if (not timer_up):
      spot.penup()
      updateScore()
      changeColor()
      changeSize()
      changePosition()
    else:
      spot.hideturtle()

def changePosition():
    newXpos = rand.randint(-400, 400)
    newYpos = rand.randint(-300, 300)
    spot.goto(newXpos, newYpos)

def updateScore():
    global score
    score += 1
    scoreWriter.clear()
    scoreWriter.write(score, font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

def changeColor():
  spot.color(rand.choice(colors))
  spot.stamp()
  spot.color(spotColor)

def changeSize():
  spot.shapesize(rand.choice(sizes))

def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global spot

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, score)

#-----events----------------

spot.onclick(spotClicked)
wn = trtl.Screen()
wn.bgcolor("purple")
wn.ontimer(countdown, counter_interval)
wn.mainloop()