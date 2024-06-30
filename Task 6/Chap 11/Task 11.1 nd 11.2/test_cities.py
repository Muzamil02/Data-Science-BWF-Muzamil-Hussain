# test_cities.py
import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted_string = city_country('santiago', 'chile')
        self.assertEqual(formatted_string, 'Santiago, Chile')

    def test_city_country_population(self):
        formatted_string = city_country('santiago', 'chile', 5000000)
        self.assertEqual(formatted_string, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':
    unittest.main()