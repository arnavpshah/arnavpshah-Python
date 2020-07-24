# using turtle library for graphics
# using random for location
# using time to slow down game
import turtle
import random
import time
# screen setup
# creating screen variable to set backround color and use keyboard controls
screen = turtle.Screen()
screen.bgcolor(150,200,200)
# important function to update screen
screen.tracer(0)
# draw boundary
# creating turtle to draw game boundaries
box = turtle.Turtle()
box.penup()
box.goto(-300,300)
box.pendown()
for i in range(4):
  box.forward(600)
  box.right(90)
box.ht()
# drop snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color(0,0,0)
head.penup()
head.goto(0,100)
# direction variable stands for the direction of the head
direction = "stop"
# functions to move snake
def up():
  global direction
  if direction != "down":
    direction = "up"
def down():
  global direction
  if direction != "up":
    direction = "down"
def left():
  global direction
  if direction != "right":
    direction = "left"
def right():
  global direction
  if direction != "left":
    direction = "right"
# event listeners
screen.onkey(up, "up")
screen.onkey(up, "w")
screen.onkey(down, "down")
screen.onkey(down, "s")
screen.onkey(right, "right")
screen.onkey(right, "d")
screen.onkey(left, "left")
screen.onkey(left, "a")
screen.listen()
# move
def move():
  if direction == "up":
    head.sety(head.ycor() + 20)
  elif direction == "down":
    head.sety(head.ycor() - 20)
  elif direction == "left":
    head.setx(head.xcor() - 20)
  elif direction == "right":
    head.setx(head.xcor() + 20)
# food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color(255,0,0)
food.penup()
# score
score = 0
s = turtle.Turtle()
s.speed(0)
s.penup()
s.goto(0,250)
s.color(255,255,255)
s.ht()
s.write("Score: 0", align = "center", font = ("Courier",24,"normal"))
# body of snake
body = []
# main game loop
# the while true will run until the user stops the program, it will never break
# everything in the while loop must be constantly run
while True:
  # updating screen graphics
  screen.update()
  # slowing down each while loop cycle by 0.1 seconds
  time.sleep(0.1)
  # code to check if apple is eaten
  # apple is eaten is head is 15 pixels away
  if head.distance(food) < 15:
    # moving apple to random location
    food.goto(random.randint(-280,280),random.randint(-280,280))
    # creating new body part for snake
    new = turtle.Turtle()
    new.speed(0)
    new.shape("square")
    new.color(200,200,200)
    new.penup()
    # adding new body part to list
    body.append(new)
    # increasing score by 1 each time the snake eats the apple
    score = score + 1
  # move snake body
  # moving each body segment to the location of the one before it in the list
  for b in range(len(body)-1,0,-1):
    body[b].goto(body[b-1].xcor(),body[b-1].ycor())
  # the first segment move to the position of the head# 
  if len(body) > 0:
    body[0].goto(head.xcor(), head.ycor())
  # moving head of snake
  move()

  hit = False
  for b in body:
    if b.distance(head) < 20:
      hit = True
      break
  if head.xcor() > 300 or head.xcor() < -300 or head.ycor() > 300 or head.ycor() < -300 or hit == True:
    time.sleep(0.5)
    head.goto(0,0)
    direction = "stop"
    # deleting body
    for b in body:
      b.ht()
      body.remove(b)
    score = 0
  s.clear()
  s.write("Score: " + str(score), align = "center", font = ("Courier",24,"normal"))

# d = turtle.Turtle()
# r = random.randint(0,225)
# g = random.randint(0,255)
# b = random.randint(0,255)
# d.color(r, g, b)
# for i in range(4):
#   d.forward(200)
#   d.right(90)
