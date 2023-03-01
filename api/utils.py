import math
from numpy import arcsin
import pandas as pd


def haversine_distance(coord1: tuple, coord2: tuple):
    lon1, lat1 = coord1
    lon2, lat2 = coord2

    R = 6371000
    phi_1 = math.radians(lat1)
    phi_2 = math.radians(lat2)

    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    distance_meters = (
        2
        * R
        * arcsin(
            math.sqrt(
                math.sin(delta_phi / 2.0) ** 2
                + math.cos(phi_1) * math.cos(phi_2) *
                math.sin(delta_lambda / 2.0) ** 2
            )
        )
    )

    return distance_meters / 1000
