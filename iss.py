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
from turtle import Screen, Turtle


def get_astronauts():
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)
    people = response.json()["people"]
    total_astronauts = response.json()["number"]

    # List Comprehension of astronauts
    astronauts = [astronaut["name"] for astronaut in people]
    space_crafts = [craft["craft"] for craft in people]

    # TODO for loop prints duplicates
    for astronaut in astronauts:
        for space_craft in space_crafts:
            print(f"{astronaut} : {space_craft}")

    print(f"Total # of astronauts: {total_astronauts}")


def get_coordinates():
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    coordinates = response.json()["iss_position"]
    time_stamp = response.json()["timestamp"]
    print(response.text)
    print(
        f'Latitude: {coordinates["latitude"]}\nLongitude: {coordinates["longitude"]}')
    # TODO - Format Timestamp
    print(f'Timestamp: {time_stamp}')


def create_turtle_graphic():
    print("Turtle Graphic function")
    s = turtle.getscreen()
    print(s)


def main():
    # print("This is method main")
    # print(get_astronauts())
    # print(get_coordinates())
    print(create_turtle_graphic())


if __name__ == '__main__':
    main()
