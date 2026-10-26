import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for city_country function."""

    def test_city_country(self):
        """Does city_country work correctly without population?"""
        location = city_country("Paris", "France")
        self.assertEqual(location, "Paris, France")

    def test_city_country_population(self):
        """Does city_country work correctly with population?"""
        location = city_country("New York", "USA", 8000000)
        self.assertEqual(location, "New York, USA - population 8000000")

    def test_city_country_population_country(self):
        """Does city_country work correctly with population and language?"""
        location = city_country("Tokyo", "Japan", 500000, "Japanese")
        self.assertEqual(location, "Tokyo, Japan - population 500000, Japanese")

if __name__ == "__main__": 
    unittest.main()
    