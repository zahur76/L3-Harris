import math
from numpy import arcsin # used for sign inverse
import pandas as pd


def haversine_distance(coord1: tuple, coord2: tuple):
    """
    Function to calculate distance between 2 sets of coordinates using Haversine Formula
    """
    lon1, lat1 = coord1
    lon2, lat2 = coord2

    R = 6371000
    # convert degree's into radians
    radian_1 = math.radians(lat1)
    radian_2 = math.radians(lat2)

    delta_latitude = math.radians(lat2 - lat1)
    delta_longitude = math.radians(lon2 - lon1)

    # apply haversine formula
    distance_meters = (
        2
        * R
        * arcsin(
            math.sqrt(
                math.sin(delta_latitude / 2.0) ** 2
                + math.cos(radian_1) * math.cos(radian_2) *
                math.sin(delta_longitude / 2.0) ** 2
            )
        )
    )

    return distance_meters / 1000
