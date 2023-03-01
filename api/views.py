from django.shortcuts import render
from .forms import addCoordinatesForm
from .utils import haversine_distance
import pandas as pd
from .models import Airport
from django.http import JsonResponse

# Create your views here.


def index(request):
    """A view to return the home page with ipout form"""

    form = addCoordinatesForm()

    if request.method == 'POST':

        latitude = float(request.POST.get('latitude'))
        longitude = float(request.POST.get('longitude'))

        input_coord2 = (latitude, longitude)

        df = pd.read_csv("docs/uk_airport_coords.csv")

        def calculate_distance(row): return haversine_distance(
            (row.Latitude, row.Longitude), (input_coord2))

        df["Distance"] = df.apply(calculate_distance, axis=1)

        index = df[["Distance"]].idxmin()

        context = {
            'input_latitude': latitude,
            'input_longitude': longitude,
            'airport': df["NAME"].values[index][0],
            'latitude': df["Latitude"].values[index][0],
            'longitude': df["Longitude"].values[index][0],
            'icao_code': df["ICAO"].values[index][0],
            'distance': round(df["Distance"].values[index][0], 3),
            'form': form
        }
        return render(request, "api/index.html", context)

    context = {
        'form': form,
    }
    return render(request, "api/index.html", context)


# Create your views here.
def method_two(request):
    """A view to return the method 2 input form"""

    form = addCoordinatesForm()

    if request.method == 'POST':

        latitude = float(request.POST.get('latitude'))
        longitude = float(request.POST.get('longitude'))

        input_coord2 = (latitude, longitude)

        airport = Airport.objects.all().values()

        df = pd.DataFrame(list(airport))

        def calculate_distance(row): return haversine_distance(
            (row.latitude, row.longitude), (input_coord2))

        df["Distance"] = df.apply(calculate_distance, axis=1)

        index = df[["Distance"]].idxmin()

        context = {
            'input_latitude': latitude,
            'input_longitude': longitude,
            'airport': df["name"].values[index][0],
            'latitude': df["latitude"].values[index][0],
            'longitude': df["longitude"].values[index][0],
            'icao_code': df["icao_code"].values[index][0],
            'distance': f'{round(df["Distance"].values[index][0], 3)} km',
        }
        return JsonResponse(context)

    context = {
        'form': form,
    }
    return render(request, "api/method_two.html", context)
