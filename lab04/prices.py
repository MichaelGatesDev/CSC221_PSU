#!/usr/bin/env python3

# Michael Gates
# 26 September 2017
# Graphs changes in prices using Turtle

import turtle
import random


def draw_raised_price(last, new):
    """
    Draws a raised price line (red)
    """
    t.color("red")
    t.left(90)
    t.forward(new - last)
    t.right(90)
    t.forward(10)

def draw_lowered_price(last, new):
    """
    Draws a lowered price line (blue)
    """
    t.color("blue")
    t.right(90)
    t.forward(last - new)
    t.left(90)
    t.forward(10)


s = turtle.Screen()
t = turtle.Turtle()


starting_price = 50
last_price = starting_price


# draw initial line
t.forward(10)


# Run loop 25 times
for i in range(0, 25):
    # Generate a random price between 20 and 99 (inclusive)
    random_price = random.randint(20, 99)
    #print("The generated price is " + str(random_price))

    if(random_price > last_price):
        draw_raised_price(last_price, random_price)
    else:
        draw_lowered_price(last_price, random_price)
    
    last_price = random_price


# Runs the Tkinter main loop to prevent window from closing on finish
s._root.mainloop()