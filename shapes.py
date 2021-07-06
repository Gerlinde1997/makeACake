#!/usr/bin/env python3

"""
Make a Cake
Python module with the class Shapes

Copyright (C) 2021 Gerlinde van Ginkel
SPDX-License-Identifier: GPL-3.0-or-later
"""

__author__ = "Gerlinde van Ginkel"
__version__ = "2021.v1"

import turtle
import math

class Shapes:
    """
    class for drawing different shapes with turtle
    """
    def __init__(self, turtle, color, x, y):
        self.pencil = turtle
        self.color = color
        self.x = x
        self.y = y
    
    # rectangle for layers (width, height)
    # icing (width, height)
    # whipped cream (width, height)
    # candle -> rectangle, line and flame
    
    def draw_rectangle(self, width, height):
        pencil = self.pencil
        pencil.hideturtle()
        pencil.penup()
        pencil.color(self.color)
        pencil.fillcolor(self.color)
        pencil.goto(self.x, self.y)
        pencil.pendown()
        pencil.begin_fill()

        for side in range(2):
            pencil.forward(width)
            pencil.left(90)
            pencil.forward(height)
            pencil.left(90)

        pencil.end_fill()
        pencil.setheading(0)  
        pencil.getscreen().update()
    

    def draw_icing(self, ru):
        pencil = self.pencil
        pencil.penup()
        pencil.color(self.color)
        pencil.fillcolor(self.color)
        pencil.goto(self.x, self.y)
        pencil.pendown()
        pencil.begin_fill()

        for x in range(self.x, ru+2):
            pencil.goto(x, self.y+5 + 2*math.cos((x/10)*2*math.pi))
        
        pencil.goto(ru+1, self.y)
        pencil.goto(self.x, self.y)
        pencil.end_fill()
        pencil.getscreen().update()
    
    def draw_cream(self, rux):
        pencil = self.pencil
        pencil.penup()
        pencil.color(self.color)
        pencil.pensize(20)
        pencil.goto(self.x, self.y)
        pencil.pendown()

        for x in range(self.x, rux+1):
            pencil.goto(x, self.y + math.sin((x/10)*2*math.pi))
        
        pencil.end_fill()
        pencil.getscreen().update()
    

    def draw_flame(self, size):
        pencil = self.pencil
        pencil.penup()
        pencil.color(self.color)
        pencil.goto(self.x, self.y)
        pencil.pendown()
        pencil.seth(-270)
        pencil.begin_fill()
        pencil.circle(size, 180)
        pencil.circle(2*size, 45)
        pencil.circle(size*0.586, 90)
        pencil.circle(2*size, 45)
        pencil.end_fill()
        pencil.getscreen().update()


if __name__ == "__main__":
    SHAPES = Shapes(turtle.Turtle(), "orange", 50, 50)