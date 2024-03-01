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

    def test_review_attributes(self):
        """Test review attributes"""
        review_instance = Review()
        self.assertEqual(review_instance.place_id, "")
        self.assertEqual(review_instance.user_id, "")
        self.assertEqual(review_instance.text, "")


if __name__ == "__main__":
    unittest.main()
