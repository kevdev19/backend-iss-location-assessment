#!/usr/bin/env python

"""
Part A
List of astronauts - full names, spacecraft, total # of astronauts in
Use this API - http://api.open-notify.org/astros.json

Part B
Obtain current geographic coordinates(lat/lon) of space station and
time stamp.
Use this API - http://api.open-notify.org/iss-now.json

Part C
With turtle library, create graphics screen with the world map
background image, map.gif.
Use turtle methods such Screen(), setup(), bgpic(), and setworldcoordinates()
Register an icon image for the ISS within the turtle screen context.
Create a turtle.Turtle() to move the ISS ot its current lat/lon on the map -
use methods such as shape(), setheading(), penup(). amd goto()
Python.org Turtle Documentation - https://docs.python.org/3/library/turtle.html

Part D
Find out the next time that the ISS will be overhead of Indianapolis, Indiana
Use geographic lat/lon of Indianapolis, Indiana to plot a yellow dot on the map.
Use this API to query the next pass - http://api.open-notify.org/iss-pass.json
"""

__author__ = 'Kevin Blount'

import requests
from tabulate import tabulate
from datetime import datetime
import time
import turtle


def get_astronauts():
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)
    people = response.json()["people"]
    total_astronauts = response.json()["number"]

    header = people[0].keys()
    rows = [x.values() for x in people]
    table = tabulate(rows, header)

    return f'{table}\n\nTotal Astronauts: {total_astronauts}\n'

    # List Comprehension of astronauts
    # astronauts = [astronaut["name"] for astronaut in people]
    # space_crafts = [craft["craft"] for craft in people]

    # TODO for loop prints duplicates
    # for astronaut in astronauts:
    #     for space_craft in space_crafts:
    #         print(f"{astronaut} : {space_craft}")

    # print(people)
    # print(f"Total # of astronauts: {total_astronauts}")


def get_coordinates():
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    coordinates = response.json()["iss_position"]
    time_stamp = response.json()["timestamp"]
    time_stamp_format = datetime.fromtimestamp(time_stamp)
    latitude = coordinates["latitude"]
    longitude = coordinates["longitude"]
    lat_new = float(latitude)
    long_new = float(longitude)

    return lat_new, long_new, time_stamp_format


def create_turtle_graphics():

    screen = turtle.Screen()

    # Turtle screen setup, graphics, and turtle icon
    screen_setup = screen.setup(width=713, height=353)
    world_coord = screen.setworldcoordinates(-180, -90, 180, 90)
    iss_icon = screen.register_shape("iss.gif")
    bg_graphic = screen.bgpic("map.gif")

    # ISS icon image shape
    iss_shape = turtle.Turtle()
    iss_shape.shape("iss.gif")
    iss_shape.setheading(90)
    iss_shape.penup()

    turtle.goto(-25, -25)
    # Must run last
    loop = screen.mainloop()
    turtle_list = [screen_setup, world_coord, iss_icon, bg_graphic,
                   bg_graphic, t_shape, loop]
    return turtle_list


def main():

    astronauts = get_astronauts()
    # Unpacks return values from get_coordinates() function
    lat, lon, t_stamp = get_coordinates()
    coordinates = get_coordinates()
    turtle_screen = create_turtle_graphics(lat, lon, t_stamp)

    print(astronauts)
    print(coordinates)
    print(turtle_screen)


if __name__ == '__main__':
    main()
