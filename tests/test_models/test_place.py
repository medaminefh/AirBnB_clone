#!/usr/bin/python3
"""
Test Place class
"""

import unittest
from models.place import Place


class TestPlaceModel(unittest.TestCase):
    """
    Testing my Place model
    """

    def test_creation(self):
        """
        Test instance creation with kwargs and without it
        """
        my_model2 = Place()
        my_model2.name = "Zeramdine"
        my_model2.city_id = "city_id"
        my_model2.user_id = "user_id"

        self.assertEqual(my_model2.name, "Zeramdine")
        self.assertEqual(my_model2.city_id, "city_id")
        self.assertEqual(my_model2.user_id, "user_id")
        self.assertIs(hasattr(my_model2, "id"), True)
        self.assertIs(hasattr(my_model2, "created_at"), True)
        self.assertIs(hasattr(my_model2, "updated_at"), True)
