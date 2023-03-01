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

    meters = (
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

    return meters / 1000


# lat2 = 51.735711
# lon2 = -0.848769

# # coord1 = (lat1, lon1)
# coord2 = (lat2, lon2)

# df = pd.read_csv("docs/uk_airport_coords.csv")


# def calculate_distance(row): return haversine_distance(
#     (row.Latitude, row.Longitude), (coord2))


# df["Distance"] = df.apply(calculate_distance, axis=1)


# index = df[["Distance"]].idxmin()

# print(df["NAME"].values[index][0])
