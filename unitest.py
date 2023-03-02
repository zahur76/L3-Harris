import unittest
from main import GetAirport


class SimpleTest(unittest.TestCase):

    def setUp(self):
        # southhampton coordinates
        self.latitude = 50.909698
        self.longitude = -1.404351
        self.airport = GetAirport(self.latitude, self.longitude)

        #  city airport coordinates
        self.airport_city = GetAirport(51.505278, 0.055278)

    def test_output_format(self):

        output = self.airport.nearest_airport()

        self.assertTrue(output, dict)

    def test_airport_name(self):
        # use city airport cooridnates to check nearest airport
        output = self.airport_city.nearest_airport()

        self.assertEqual(output['nearest airport'], 'CITY')

    def test_airport_distance(self):
        # use city airport to check distance
        output = self.airport_city.nearest_airport()
        
        self.assertEqual(int(output['distance'].strip('km')[0]), 0)


if __name__ == '__main__':
    unittest.main()
