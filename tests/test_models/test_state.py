#!/usr/bin/python3
"""
Test State class
"""

import unittest
from models.state import State


class TestBaseModel(unittest.TestCase):
    """
    Testing my State class
    """

    def test_creation(self):
        """
        Test instance creation with kwargs and without it
        """
        my_model2 = State()
        my_model2.name = "Monastir"
        self.assertEqual(my_model2.name, "Monastir")
        self.assertIs(hasattr(my_model2, "id"), True)
        self.assertIs(hasattr(my_model2, "created_at"), True)
        self.assertIs(hasattr(my_model2, "updated_at"), True)
