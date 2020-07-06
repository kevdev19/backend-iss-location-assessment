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
import urllib
import json
import importlib
import json

importlib.reload(turtle)
importlib.reload(requests)


def main():
    astros_url = "http://api.open-notify.org/astros.json"
    astros_response = requests.get(astros_url)
    people = astros_response.json()["people"]
    total_astronauts = astros_response.json()["number"]

    header = people[0].keys()
    rows = [x.values() for x in people]
    table = tabulate(rows, header)

    print(f'{table}\n\nTotal Astronauts: {total_astronauts}\n')

    iss_now_url = "http://api.open-notify.org/iss-now.json"
    iss_now_response = requests.get(iss_now_url)
    coordinates = iss_now_response.json()["iss_position"]
    time_stamp = iss_now_response.json()["timestamp"]
    time_stamp_convert = datetime.fromtimestamp(time_stamp)
    latitude = coordinates["latitude"]
    longitude = coordinates["longitude"]
    lat_new = float(latitude)
    long_new = float(longitude)
    print(
        f'Latitude: {lat_new} Longitude: {long_new} Timestamp: {time_stamp_convert}')

    screen = turtle.Screen()
    screen.setup(720, 360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.register_shape("iss.gif")
    screen.bgpic("map.gif")

    # ISS icon shape
    iss_shape = turtle.Turtle()
    iss_shape.shape("iss.gif")
    iss_shape.setheading(90)
    iss_shape.penup()

    iss_shape.goto(long_new, lat_new)

    # Indianapolis, Indiana ISS
    lat = float(39.7684)
    lon = float(-86.1581)

    i_iss = turtle.Turtle()
    i_iss.penup()
    i_iss.color('yellow')
    i_iss.goto(lon, lat)
    i_iss.dot(5)
    i_iss.hideturtle()
    # Must run last

    # iss_pass_url and response lines provided by Faciliator JT
    iss_pass_url = "http://api.open-notify.org/iss-pass.json?lat={}&lon={}"
    iss_pass_response = requests.get(iss_pass_url.format(lat, lon))
    iss_pass_result = iss_pass_response.json()

    rise_time = iss_pass_result['response'][1]['risetime']
    rise_time_convert = time.ctime(rise_time)
    i_iss.write(rise_time_convert)
    screen.mainloop()


if __name__ == '__main__':
    main()
