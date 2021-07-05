#!/usr/bin/env python3

"""
Make a Cake
Command line tool for baking your own virtual birthday cake

Python module with the class Shapes
"""

__author__ = "Gerlinde van Ginkel"
__version__ = "2021.v1"

import sys
import turtle
import math

class Shapes:
    """
    class for drawing different shapes with turtle
    """
    def __init__(self, turtle, color, x, y):
        self.pencil = turtle
        self.color = color
        self.target = (x, y)
    
    def draw_cirkel(self):
        return 0

    

if __name__ == "__main__":
    SHAPES = Shapes()