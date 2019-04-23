# -*- coding: utf-8 -*-
"""
Main module for Table class

"""
import logging
import logging.config
import argparse

from stacks import TriangularStack

__author__ = "tanmay.datta86@gmail.com"
logging.config.fileConfig('logging.config',
                          disable_existing_loggers=False)

LOGGER = logging.getLogger("MainRunnerWaterOverflow")


def solveWaterOverFlowFor(jth_glass: int, ith_row: int, k_liter: float) -> float:
    """
    Function to solve water
    """
    LOGGER.debug("j => {}, i => {}, k => {}".format(
        jth_glass, ith_row, k_liter))
    unit_capacity = 0.250
    triangular_stack = TriangularStack(size=ith_row,
                                       unit_capacity=unit_capacity)
    triangular_stack.pour(k_liter)
    return triangular_stack.get_water_at(ith_row, jth_glass)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("jth_glass", help="The Jth glass J is on x axis",
                        type=int)

    parser.add_argument("ith_row", help="The Ith row I is on y axis",
                        type=int)

    parser.add_argument("k_liter", help="K liter of water is poured",
                        type=float)

    args = parser.parse_args()
    LOGGER.debug("j => {}, i => {}, k => {}".format(
        args.jth_glass, args.ith_row, args.k_liter))

    print(solveWaterOverFlowFor(args.jth_glass, args.ith_row, args.k_liter))
