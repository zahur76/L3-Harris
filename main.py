from api.utils import haversine_distance
import pandas as pd
from colorama import Fore


class GetAirport:
    def __init__(self, latitude: float, longitude: float) -> dict:
        self.latitude = latitude
        self.longitude = longitude

    def nearest_airport(self):

        df = pd.read_csv("docs/uk_airport_coords.csv")

        def calculate_distance(row): return haversine_distance(
            (row.Latitude, row.Longitude), (self.latitude, self.longitude))

        df["Distance"] = df.apply(calculate_distance, axis=1)

        index = df[["Distance"]].idxmin()

        output = {
            'input latitude': self.latitude,
            'input longitude': self.longitude,
            'nearest airport': df["NAME"].values[index][0],
            'latitude': df["Latitude"].values[index][0],
            'longitude': df["Longitude"].values[index][0],
            'icao code': df["ICAO"].values[index][0],
            'distance': f'{round(df["Distance"].values[index][0], 3)} km',
        }

        for key, value in output.items():
            print(" ")
            print(Fore.WHITE + f'{key}: {value}')

        return output


if __name__ == "__main__":

    while True:
        try:
            latitude = float(input(Fore.GREEN + "Please enter latitude: "))
            longitude = float(input(Fore.GREEN + "Please enter longitude: "))
            break
        except ValueError as e:
            print(f'Input Error: {e}')
            print(' Please Try Again')

    airport = GetAirport(latitude, longitude)

    airport.nearest_airport()
