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
        self.defaultStack = TriangularStack(size=ith_row,
                                            unit_capacity=unit_capacity)
