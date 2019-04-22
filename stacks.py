# -*- coding: utf-8 -*-
"""
Main module for Stack class

"""

from abc import ABC, abstractclassmethod
import logging

__author__ = "tanmay.datta86@gmail.com"
LOGGER = logging.getLogger(__name__)


class WaterStack(ABC):
    """
    Interface for water stack
    """
    @abstractclassmethod
    def pour(self, n_liters:float):
        pass
    
    @abstractclassmethod
    def get_water_at_glass(self, row:int, column:int):
        pass

class TriangularStack(WaterStack):
    "Implementation for required water stack"

    def __init__(self, size: int, unit_capacity: float):
        LOGGER.debug(
            "Triangular stack with size ==> {}, capacity/glass ==> {}".format(size,
                                                                             unit_capacity))
        self.size = size
        self.unit_capacity = unit_capacity
    
    def pour(self, n_liter:float)-> bool:
        pass
    
    def get_water_at_glass(self, row: int, column: int) -> float:
        pass



