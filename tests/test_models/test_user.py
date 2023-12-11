#!/usr/bin/python3
"""
Test User class
"""

import unittest
from models.user import User


class TestBaseModel(unittest.TestCase):
    """
    Testing my User class
    """

    def test_creation(self):
        """
        Test instance creation with kwargs and without it
        """
        my_model2 = User()
        my_model2.email = "root@gmail.com"
        my_model2.password = "123456"
        my_model2.first_name = "Mohamed Amine"
        my_model2.last_name = "Fhal"
        self.assertEqual(my_model2.email, "root@gmail.com")
        self.assertEqual(my_model2.password, "123456")
        self.assertEqual(my_model2.first_name, "Mohamed Amine")
        self.assertEqual(my_model2.last_name, "Fhal")
        self.assertIs(hasattr(my_model2, "id"), True)
        self.assertIs(hasattr(my_model2, "created_at"), True)
        self.assertIs(hasattr(my_model2, "updated_at"), True)
