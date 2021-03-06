#!/usr/bin/env python3

"""
Make a Cake
Command line tool for baking your own virtual birthday cake

Copyright (C) 2021 Gerlinde van Ginkel
SPDX-License-Identifier: GPL-3.0-or-later
"""

__author__ = "Gerlinde van Ginkel"
__version__ = "2021.v1"

import sys
import argparse
import textwrap
from turtle import *
from shapes import Shapes

FLAVORS = {"strawberry": "#D93447", 
    "vanille": "#F5EBBC", 
    "chocolate": "#301D01",
    "lemon": "#FCFF9E",
    "raspberry": "#FFABDF",
    "pistachio": "#D5FFAB"}

ICING = {"sugar": "#F0EDE6", "caramel": "#B57F00", "chocolate": "#291900"}


def get_available_flavors(type):
    available = ""
    for flavor in type.keys():
        available += flavor + "\n"
    return available


def valid_cake_flavor(flavor):
    #cake_flavours = str(FLAVORS.keys())
    if flavor not in FLAVORS:
        raise argparse.ArgumentTypeError("Unavailable flavor, please choose one of these: \n"
                                         + get_available_flavors(FLAVORS))
    return flavor


def valid_icing_flavor(flavor):
    #icing_flavors = str(ICING.keys())
    if flavor not in ICING:
        raise argparse.ArgumentTypeError("Unavailable flavor, please choose one of these: \n"
                                         + get_available_flavors(ICING))
    return flavor


def set_window():
    window = Screen()
    window.title("Enjoy!")
    window.screensize(500, 500)
    window.setworldcoordinates(0, 100, 100, 0)
    window.tracer(0)
    window.bgcolor("#9EECF0")

    return window

def draw_wick(pencil):
    pencil.penup()
    pencil.goto(50, 12)
    pencil.pensize(2)
    pencil.color("#000000")
    pencil.pendown()    
    pencil.forward(4)
    pencil.getscreen().update()


def main(args):
    # argparse given 2 flavours and  1 icing (3 args)
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, 
    description=textwrap.dedent('''\
...         Create your own virtual birthday cake!
...         --------------------------------------
...         options for cake flavors:
...         - vanille
...         - strawberry
...         - lemon
...         - chocolate
...         - raspberry
...         - pistachio
...
...         options for icing flavor:
...         - sugar
...         - caramel
...         - chocolate
...        '''))

    parser.add_argument("-f", '--cake_flavors', nargs='+', type=valid_cake_flavor, required=True,
                        help="Fill in three flavors for the cake.", dest='cakeflavors')
    parser.add_argument("-i", '--icing_flavor', type=valid_icing_flavor,
                        required=True, help="Fill in one flavor for the icing.", dest='icingflavor')

    args = parser.parse_args()

    #set pencil
    pencil = Turtle()
    pencil.speed(0)
    pencil.hideturtle()

    #set screen/window
    window = set_window()

    # plate
    plate = Shapes(pencil, "#E4F6F7", 10, 90)
    plate.draw_rectangle(80, 4)

    # bottom layer
    bottom_layer = Shapes(pencil, FLAVORS[args.cakeflavors[0]], 20, 70)
    bottom_layer.draw_rectangle(60, 19.9)
    bottom_icing = Shapes(pencil, ICING[args.icingflavor], 19, 70)
    bottom_icing.draw_icing(80)
    
    # middle layer
    middle_layer = Shapes(pencil, FLAVORS[args.cakeflavors[1]], 30, 50)
    middle_layer.draw_rectangle(40, 19.9)
    middle_icing = Shapes(pencil, ICING[args.icingflavor], 29, 50)
    middle_icing.draw_icing(70)

    # upper layer
    upper_layer = Shapes(pencil, FLAVORS[args.cakeflavors[2]], 40, 30)
    upper_layer.draw_rectangle(20, 19.9)

    # candle
    wax = Shapes(pencil, "#FF734D", 48, 16)
    wax.draw_rectangle(4, 14)
    flame = Shapes(pencil, "orange", 52, 12)
    flame.draw_flame(2)
    flame = Shapes(pencil, "yellow", 51, 12)
    flame.draw_flame(1)
    draw_wick(pencil)

    # upper icing
    upper_icing = Shapes(pencil, ICING[args.icingflavor], 39, 30)
    upper_icing.draw_icing(60)

    cream = Shapes(pencil, "white", 20, 82)
    cream.draw_cream(80)
    cream = Shapes(pencil, "white", 30, 62)
    cream.draw_cream(70)
    cream = Shapes(pencil, "white", 40, 42)
    cream.draw_cream(60)

    window.exitonclick()


if __name__ == "__main__":
    sys.exit(main(sys.argv))
