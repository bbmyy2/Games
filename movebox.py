#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: MartinMa
# time:2023/8/10 11:54
# File:movebox.py
import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Move the Box Game")
screen.bgcolor("white")
screen.setup(width=800, height=600)

# Create the player box
player = turtle.Turtle()
player.shape("square")
player.color("blue")
player.penup()
player.speed(0)

# Create boxes and targets
boxes = []
targets = []


def create_box(x, y):
    box = turtle.Turtle()
    box.shape("square")
    box.color("red")
    box.penup()
    box.goto(x, y)
    boxes.append(box)


def create_target(x, y):
    target = turtle.Turtle()
    target.shape("circle")
    target.color("green")
    target.penup()
    target.goto(x, y)
    targets.append(target)


# Create level layout
level_layout = [
    "#####T##",
    "#B     #",
    "#   B  #",
    "#  BP  #",
    "########"
]

for y, row in enumerate(level_layout):
    for x, char in enumerate(row):
        screen_x = -350 + x * 50
        screen_y = 250 - y * 50

        if char == "B":
            create_box(screen_x, screen_y)
        elif char == "T":
            create_target(screen_x, screen_y)


# Function to move the player
def move_left():
    player.setheading(180)
    player.forward(50)
    check_push()


def move_right():
    player.setheading(0)
    player.forward(50)
    check_push()


def move_up():
    player.setheading(90)
    player.forward(50)
    check_push()


def move_down():
    player.setheading(270)
    player.forward(50)
    check_push()


def check_push():
    player_x, player_y = player.pos()

    for box in boxes:
        if player.distance(box) < 50:
            box_x, box_y = box.pos()
            dx = box_x - player_x
            dy = box_y - player_y

            new_box_x = box_x + dx
            new_box_y = box_y + dy

            if (new_box_x, new_box_y) not in [(box.xcor(), box.ycor()) for box in boxes]:
                box.goto(new_box_x, new_box_y)


# Keyboard bindings
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")

# Main game loop
screen.mainloop()

