# Turtle color names obtained from https://cs111.wellesley.edu/labs/lab01/colors

import turtle as trtl
import random as rand

# game variable section
number_walls = 25
path_width = 15
wall_length = path_width
angle = 90
wall_thickness = 3
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'limegreen', 'skyblue']

# initialize Turtle
maze_writer = trtl.Turtle()
maze_writer.pensize(wall_thickness)
maze_writer.color(rand.choice(colors)) # randomly change color from my list each time the code runs
maze_writer.speed('fastest')

maze_runner = trtl.Turtle()
maze_runner.hideturtle()
maze_runner.color("white")
maze_runner.penup()
maze_runner.goto(-20, -20)
maze_runner.pendown()

runner_move_speed = 2
keypressed = False

# Move maze_runner functions
def move_up():
    maze_runner.setheading(90)
    

def move_down():
    maze_runner.setheading(270)
    

def move_left():
    maze_runner.setheading(180)
    

def move_right():
    maze_runner.setheading(0)
    

def move_runner():
    
        maze_runner.forward(runner_move_speed)

# Draw Maze
for side in range(number_walls):
    wall_length += path_width
    maze_writer.color(rand.choice(colors))
    maze_writer.left(angle)
    
    if side > 4:
        # randomly select starting location for door and barrier
        door = rand.randint(path_width * 2, (wall_length - path_width * 2))
        barrier = rand.randint(path_width * 2, (wall_length - path_width * 2))
        while abs(door - barrier) < path_width:
            door = rand.randint(path_width * 2, (wall_length - path_width * 2))
        
        if door < barrier:

            # draw door
            maze_writer.forward(door)
            maze_writer.penup()
            maze_writer.forward(path_width * 2)
            maze_writer.pendown()

            # draw barrier
            maze_writer.forward(barrier - door - path_width * 2)
            maze_writer.left(angle)
            maze_writer.forward(path_width * 2)
            maze_writer.back(path_width * 2)
            maze_writer.right(angle)

            maze_writer.forward(wall_length - barrier)
        else:
            # draw barrier
            maze_writer.forward(barrier)
            maze_writer.left(angle)
            maze_writer.forward(path_width * 2)
            maze_writer.back(path_width * 2)
            maze_writer.right(angle)


            # draw door
            maze_writer.forward(door - barrier)
            maze_writer.penup()
            maze_writer.forward(path_width * 2)
            maze_writer.pendown()

            maze_writer.forward(wall_length - door - path_width * 2)

maze_writer.hideturtle() # hide turtle only leaving nice, clean maze drawing
maze_runner.showturtle()


#Create screen and keep it open listening for events
wn = trtl.Screen()
wn.bgcolor("black")

# Keypress check
wn.listen()
wn.onkeypress(move_up, "w")
wn.onkeypress(move_left, "a")
wn.onkeypress(move_down, "s")
wn.onkeypress(move_right, "d")

wn.onkeypress(move_up, "Up")
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_down, "Down")
wn.onkeypress(move_right, "Right")

wn.onkeypress(move_runner, "space")

wn.mainloop()