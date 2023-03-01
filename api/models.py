from django.db import models

# Create your models here.
class Airport(models.Model):

    """
    Model to Airport Coordinates
    """

    class Meta:
        verbose_name_plural = "Airport Details"

    name = models.CharField(max_length=254)
    icao_code = models.CharField(max_length=254)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name