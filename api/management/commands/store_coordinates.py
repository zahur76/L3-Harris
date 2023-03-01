from django.core.management.base import BaseCommand
from api.models import Airport
import csv


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        with open('docs/uk_airport_coords.csv') as file:
            reader = csv.reader(file)
            next(reader)  # Advance past the header

            for row in reader:

                Airport.objects.update_or_create(
                    name=row[0], defaults=dict(
                        name=row[0],
                        icao_code=row[1],
                        latitude=row[2],
                        longitude=row[3]
                    )
                )
