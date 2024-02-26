#!/usr/bin/python3
"""Unittest for console"""
import unittest
from console import SysConsole


class TestConsole(unittest.TestCase):
    """TestConsole class to test  console module"""

    def test_quit(self):
        """Test quit method"""
        self.assertTrue(SysConsole().do_quit(''))

    def test_EOF(self):
        """Test EOF method"""
        self.assertTrue(SysConsole().do_EOF(''))

    def test_emptyline(self):
        """Test emptyline method"""
        self.assertFalse(SysConsole().emptyline())

    def test_help(self):
        """Test help method"""
        self.assertIsNone(SysConsole().do_help(''))


if __name__ == "__main__":
    unittest.main()
