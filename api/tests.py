from django.test import TestCase
from .models import Airport
# Create your tests here.


class AirportTest(TestCase):
    def setUp(self):
        # city airport coordinates for testing
        self.latitude = 51.505278
        self.longitude = 0.055278

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'api/index.html')

    def test_method_two_homepage(self):
        response = self.client.get('/method_two')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'api/method_two.html')

    def test_output_reponse(self):
        data = {'latitude': self.latitude, 'longitude': self.longitude}
        response = self.client.post("/", data)
        self.assertEqual(response.status_code, 200)

    def test_output_airport_name(self):
        data = {'latitude': self.latitude, 'longitude': self.longitude}
        response = self.client.post("/", data)
        self.assertEqual(response.context['airport'], 'CITY')

    def test_output_airport_distance(self):
        data = {'latitude': self.latitude, 'longitude': self.longitude}
        response = self.client.post("/", data)
        self.assertEqual(response.context['distance'], 0)
