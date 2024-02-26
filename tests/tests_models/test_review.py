#!/usr/bin/python3
"""Unittest for review"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Class to test review module"""
    def test_review(self):
        """Test review class"""
        review_instance = Review()
        self.assertIsInstance(review_instance, Review)
        self.assertEqual(review_instance.__class__.__name__, "Review")


if __name__ == "__main__":
    unittest.main()
