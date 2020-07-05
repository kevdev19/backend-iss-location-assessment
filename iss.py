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


def main():
    astros_url = "http://api.open-notify.org/astros.json"
    response = requests.get(astros_url)
    people = response.json()["people"]
    total_astronauts = response.json()["number"]

    header = people[0].keys()
    rows = [x.values() for x in people]
    table = tabulate(rows, header)

    print(f'{table}\n\nTotal Astronauts: {total_astronauts}\n')

    iss_now_url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(iss_now_url)
    coordinates = response.json()["iss_position"]
    time_stamp = response.json()["timestamp"]
    time_stamp_convert = datetime.fromtimestamp(time_stamp)
    latitude = coordinates["latitude"]
    longitude = coordinates["longitude"]
    lat_new = float(latitude)
    long_new = float(longitude)
    print(
        f'Latitude: {lat_new} Longitude: {long_new} Timestamp: {time_stamp_convert}')

    screen = turtle.Screen()
    screen.setup(width=713, height=353)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.register_shape("iss.gif")
    screen.bgpic("map.gif")

    # ISS icon shape
    iss_shape = turtle.Turtle()
    iss_shape.shape("iss.gif")
    iss_shape.setheading(90)
    iss_shape.penup()

    iss_shape.goto(lat_new, long_new)
    # Must run last
    screen.mainloop()


if __name__ == '__main__':
    main()
