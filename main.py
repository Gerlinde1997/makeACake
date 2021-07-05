#!/usr/bin/env python3

"""
Make a Cake

Command line tool for baking your own virtual birthday cake
"""

__author__ = "Gerlinde van Ginkel"
__version__ = "2021.v1"

import sys
import argparse
import turtle

FLAVOURS = {"strawberry": (255, 59, 59)}

def main(args):

    #set pencil
    pencil = turtle.Turtle()
    pencil.speed(0)
    pencil.hideturtle()

    #set screen/window
    window = turtle.Screen()
    window.bgcolor("orange")
    window.exitonclick()

if __name__ == "__main__":
    sys.exit(main(sys.argv))
