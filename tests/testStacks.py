# -*- coding: utf-8 -*-
"""
Main module for  testing Stack class

"""

import unittest
from ddt import ddt, data, unpack
import logging

from stacks import TriangularStack, OverflowException, WRONG_INDEX_ERROR_STRING, WaterNotFilledException

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
        self.rows = 7
        self.unit_capacity = 0.250
        self.defaultStack = TriangularStack(size=self.rows,
                                            unit_capacity=self.unit_capacity)

    def test_triangular_stack_initialized_properly(self):
        "Base test"
        self.assertIsInstance(self.defaultStack, TriangularStack)
        self.assertEqual(self.rows, self.defaultStack.size)
        self.assertEqual(self.unit_capacity, self.defaultStack.unit_capacity)

    @data((4, 2), (5, 1), (2, 0.450), (1, 0.250))
    @unpack
    def test_pouring_water_in_stack_when_capacity_is_higher(self, size, k_liter_water):
        "Test pouring water"
        triangular_stack = TriangularStack(size=size,
                                           unit_capacity=self.unit_capacity)
        self.assertTrue(triangular_stack.pour(k_liter_water))


    @data((4, 1, 10), (5, 0.25,3.75), (0, 10, 0))
    @unpack
    def test_maximun_capacity_of_stack(self, size, capacity, max_size):
        "Test calculation of maximum size to throw sane errors"
        triangular_stack = TriangularStack(size=size,
                                           unit_capacity=capacity)
        self.assertEqual(triangular_stack.maximum_water_limit, max_size)


    @data((4, 6), (5, 9), (2, 7), (1, 1.250))
    @unpack
    def test_pouring_water_in_stack_when_capcity_is_lower_and_overflows(self, size, k_liter_water):
        "Test pouring water"
        triangular_stack = TriangularStack(size=size,
                                           unit_capacity=self.unit_capacity)
        with self.assertRaises(OverflowException):
            triangular_stack.pour(k_liter_water)

    @data(
        (4, 0.3, [(3,0)]),
        (10, 0.25, [(10, 0)])
    )
    @unpack
    def test_query_water_in_stack_insufficent_water_poured(self, size, k_liters_to_be_poured, row_column_tests):
        "Test querying for water in glass (row, column)"
        triangular_stack = TriangularStack(
            size=size, unit_capacity=self.unit_capacity)
        triangular_stack.pour(k_liters_to_be_poured)
        for (row, column) in row_column_tests:

            with self.assertRaises(WaterNotFilledException):
                triangular_stack.get_water_at(row, column)

    @data(
        (4, 2, [(0, 0, 0.250), (1, 0, 0.250)]),
        (1, 0.25, [(0, 0, 0.250)]),
        (1, 0.2, [(0, 0, 0.2)])
    )
    @unpack
    def test_query_water_in_stack(self, size, k_liters_to_be_poured, row_column_tests):
        "Test querying for water in glass (row, column)"
        triangular_stack = TriangularStack(
            size=size, unit_capacity=self.unit_capacity)
        triangular_stack.pour(k_liters_to_be_poured)
        for (row, column, expected_value) in row_column_tests:
            self.assertEqual(triangular_stack.get_water_at(
                row, column), expected_value)

    @data((4, 2, [
        (0, -1, ValueError(WRONG_INDEX_ERROR_STRING)),
        (-1, -1, ValueError(WRONG_INDEX_ERROR_STRING)),
        (-1, 0, ValueError(WRONG_INDEX_ERROR_STRING))
    ]),)
    @unpack
    def test_query_water_in_stack_with_wrong_index(self, size, k_liters_to_be_poured, row_column_tests):
        "Test querying for water in glass (row, column)"
        triangular_stack = TriangularStack(
            size=size, unit_capacity=self.unit_capacity)
        triangular_stack.pour(k_liters_to_be_poured)
        for (row, column, expected_error) in row_column_tests:
            try:
                triangular_stack.get_water_at(row, column)
            except ValueError as value_error:
                self.assertEqual(str(value_error), str(expected_error) )
