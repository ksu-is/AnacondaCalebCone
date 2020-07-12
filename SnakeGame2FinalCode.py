# Simple Snake Game in Python 3 for Beginners
# By @TokyoEdTech

import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game by @TokyoEdTech")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Gerbil
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

## Add second eatable character
# Hamster
food2 = turtle.Turtle()
food2.speed(0)
food2.shape("circle")
food2.color("blue")
food2.penup()
food2.goto(0,100) 

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
##change font size and align to not block scoreboard
pen.write("Score: 0      High Score: 0", align="right", font=("Courier", 12, "normal"))


## Add obstacle
#Log 
log = turtle.Turtle()
log.speed(0)
log.shape("square")
log.color("brown")
log.penup()
log.goto(100, 50)
log.shapesize(200,1,1)



## Add gateway
#Gate 
gate = turtle.Turtle()
gate.speed(0)
gate.shape("square")
gate.color("yellow")
gate.penup()
gate.goto(100, -280)
gate.shapesize(2,1,1)



# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()
    ## Check if winner
    ## score check
    if score > 500:
        pen.goto(0, 240)
        pen.write(" \n WINNER!!!", align="center", font=("Courier", 36, "normal"))


    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="right", font=("Courier", 12, "normal")) 
    
    ##Check for a collision with the log
    if head.xcor()<101 and head.xcor()>99 and head.ycor()>-275 and head.ycor()<290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        ##
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="right", font=("Courier", 12, "normal")) 

    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 90)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
         ## Add a double segment
        new_segment2 = turtle.Turtle()
        new_segment2.speed(0)
        new_segment2.shape("square")
        new_segment2.color("grey")
        new_segment2.penup()
        segments.append(new_segment2)

        #make it move faster
        # Shorten the delay
        delay -= 0.0033

        # Increase the score
        score += 3

        if score > high_score:
            high_score = score
        
        pen.clear()
        ##
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="right", font=("Courier", 12, "normal")) 

    ##Check for collision with second food 
    if head.distance(food2) < 20:
        # Move the food to a random spot
        x = random.randint(110, 290)
        y = random.randint(-290, 290)
        food2.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
       
        # Shorten the delay
        delay -= 0.001

        ## Add double score
        # Increase the score
        score += 2

        if score > high_score:
            high_score = score
        
        pen.clear()
        ##
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="right", font=("Courier", 12, "normal")) 

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            pen.clear()
            ##
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="right", font=("Courier", 12, "normal"))

    time.sleep(delay)

wn.mainloop()
