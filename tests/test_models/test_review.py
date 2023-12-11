#!/usr/bin/python3
"""
Test Review class
"""

import unittest
from models.review import Review


class TestBaseModel(unittest.TestCase):
    """
    Testing my Review class
    """

    def test_creation(self):
        """
        Test instance creation with kwargs and without it
        """
        my_model2 = Review()
        my_model2.place_id = "63464"
        my_model2.user_id = "6964543"
        my_model2.text = "99746423"
        self.assertEqual(my_model2.place_id, "63464")
        self.assertEqual(my_model2.user_id, "6964543")
        self.assertEqual(my_model2.text, "99746423")
        self.assertIs(hasattr(my_model2, "id"), True)
        self.assertIs(hasattr(my_model2, "created_at"), True)
        self.assertIs(hasattr(my_model2, "updated_at"), True)
