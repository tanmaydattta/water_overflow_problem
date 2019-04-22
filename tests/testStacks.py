# -*- coding: utf-8 -*-
"""
Main module for  testing Stack class

"""

import unittest
from ddt import ddt, data, unpack
import logging

from stacks import TriangularStack

__author__ = "tanmay.datta86@gmail.com"
LOGGER = logging.getLogger(__name__)


@ddt
class TriangularStackTests(unittest.TestCase):
    """
    Testing class for TriangularStack class
    """

    def setUp(self):
        """
        setup of default stack
        """
        self.ith_row = 7
        self.unit_capacity = 0.250
        self.defaultStack = TriangularStack(size=self.ith_row,
                                            unit_capacity=self.unit_capacity)

    def test_triangular_stack_initialized_properly(self):
        "Base test"
        self.assertIsInstance(self.defaultStack, TriangularStack)
        self.assertEqual(self.ith_row, self.defaultStack.size)
        self.assertEqual(self.unit_capacity, self.defaultStack.unit_capacity)

    @data((4, 2), (5, 1), (2, 0.450), (1, 0.250))
    @unpack
    def test_pouring_water_in_stack_when_capcity_ishigher(self, size, k_liter_water):
        "Test pouring water"
        triangular_stack = TriangularStack(size=size,
                                           unit_capacity=self.unit_capacity)
        self.assertTrue(triangular_stack.pour(k_liter_water))

