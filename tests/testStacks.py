# -*- coding: utf-8 -*-
"""
Main module for  testing Stack class

"""

import unittest
from ddt import ddt, unpack
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
        self.ith_row = 3
        self.unit_capacity = 0.250
        self.defaultStack = TriangularStack(size=self.ith_row,
                                            unit_capacity=self.unit_capacity)

    def test_triangular_stack_initialized_properly(self):
        self.assertIsInstance(TriangularStack, self.defaultStack)
        self.assertEquals