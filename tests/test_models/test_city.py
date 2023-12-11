#!/usr/bin/python3
"""
Test City class
"""

import unittest
from models.city import City


class TestCityModel(unittest.TestCase):
    """
    Testing my City model
    """

    def test_creation(self):
        """
        Test instance creation with kwargs and without it
        """
        my_model2 = City()
        my_model2.name = "Mohamed Amine"
        my_model2.state_id = "656456312"
        self.assertEqual(my_model2.name, "Mohamed Amine")
        self.assertEqual(my_model2.state_id, "656456312")
        self.assertIs(hasattr(my_model2, "id"), True)
        self.assertIs(hasattr(my_model2, "created_at"), True)
        self.assertIs(hasattr(my_model2, "updated_at"), True)
