#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Test routine for Creator Python Client .
"""

import unittest
import os
import creator_python_client

CREATOR_ACCESS_KEY = os.environ['CREATOR_ACCESS_KEY']
CREATOR_ACCESS_SECRET = os.environ['CREATOR_ACCESS_SECRET']

class CreatorTest(unittest.TestCase):
    """
    Test Class.
    """
    def test_ds_connection(self):
        """
        Test connection against the device server.
        """
        self.assertEqual(type(creator_python_client.request(CREATOR_ACCESS_KEY, CREATOR_ACCESS_SECRET, \
method="get", steps=["versions"])), dict)

if __name__ == '__main__':
    unittest.main()
