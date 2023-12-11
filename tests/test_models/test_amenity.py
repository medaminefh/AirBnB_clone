#!/usr/bin/python3
"""
Test Amenity class
"""

import unittest
from models.amenity import Amenity


class TestAmenityModel(unittest.TestCase):
    """
    Testing my Amenity model
    """

    def test_creation(self):
        """
        Test instance creation with kwargs and without it
        """
        my_model2 = Amenity()
        my_model2.name = "Mohamed Amine"
        self.assertEqual(my_model2.name, "Mohamed Amine")
        self.assertIs(hasattr(my_model2, "id"), True)
        self.assertIs(hasattr(my_model2, "created_at"), True)
        self.assertIs(hasattr(my_model2, "updated_at"), True)
