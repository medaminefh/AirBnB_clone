#!/usr/bin/python3
"""
Test BaseModel class
"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Testing my BaseModel
    """

    def test_creation(self):
        """
        Test instance creation with kwargs and without it
        """
        my_model2 = BaseModel()
        my_model2.name = "Mohamed Amine"
        self.assertEqual(my_model2.name, "Mohamed Amine")
        self.assertIs(hasattr(my_model2, "id"), True)
        self.assertIs(hasattr(my_model2, "created_at"), True)
        self.assertIs(hasattr(my_model2, "updated_at"), True)
