# -*- coding: utf-8 -*-
"""
Main module for Stack class

"""

from abc import ABC, abstractclassmethod
import logging
from collections import namedtuple

__author__ = "tanmay.datta86@gmail.com"
LOGGER = logging.getLogger(__name__)


WRONG_INDEX_ERROR_STRING = "You selected wrong index"
WATER_NOT_FILLED = "The row column does not have water as of now"
OVERFLOW_ERROR_STRING = "Overflow occured for a stack of height {}, you can only pour maximum of {} unit water"
class WaterStack(ABC):
    """
    Interface for water stack
    """
    @abstractclassmethod
    def pour(self, n_liters:float):
        pass
    
    @abstractclassmethod
    def get_water_at(self, row:int, column:int):
        pass

class OverflowException(ValueError):
    """
    For raising overflow exception
    """
    def __init__(self, message = OVERFLOW_ERROR_STRING):
        self.message = message

class WaterNotFilledException(ValueError):
    """
    For raising exception, when water is not filled in the glass
    """
    def __init__(self, message = WATER_NOT_FILLED):
        self.message = message

class TriangularStack(WaterStack):
    "Implementation for required water stack"

    Glass = namedtuple('Glass', 'capacity filled')
    def __init__(self, size: int, unit_capacity: float):
        LOGGER.debug(
            "Triangular stack with size ==> {}, capacity/glass ==> {}".format(size,
                                                                             unit_capacity))
        self.size = size
        self.unit_capacity = unit_capacity
        self.water_distrubution_at_layers  = {}
        self.maximum_water_limit = TriangularStack.max_sum(unit_capacity, size)

    @staticmethod
    def max_sum(unit_capacity: float, size: int) -> float:
        """
        Just a helper function to calculate maximum volume of water a given Triangle stack can hold
        """
        sum = 0
        for l in range(1,size + 1):
            for n in range(1, l+1):
                sum += 1
        return sum * unit_capacity

    
    def pour(self, water_volume:float)-> bool:
        """
        Method to pour n liters into the stack
        """
        Glass = self.Glass
        current_layer = 0
        unit_capacity = self.unit_capacity
        while water_volume > 0 and current_layer < self.size:
            glass = self.water_distrubution_at_layers.get(
                current_layer, Glass(capacity=(current_layer+1)*unit_capacity, filled=0.0))
            if glass.filled < glass.capacity:
                delta = glass.capacity-glass.filled
                if delta < water_volume:
                    water_volume -= delta
                    self.water_distrubution_at_layers[current_layer] = Glass(capacity=glass.capacity, filled=glass.filled + delta)
                else:
                    self.water_distrubution_at_layers[current_layer] = Glass(capacity=glass.capacity, filled=glass.filled + water_volume)
                    water_volume = 0

            current_layer += 1
        if water_volume > 0: # layers finished and still water left ==> overflow !!
            raise OverflowException(OVERFLOW_ERROR_STRING.format(self.size, self.maximum_water_limit))
        return True
    
    def get_water_at(self, row: int, _column: int) -> float:
        """Get the water  row, column currently column has no function
        """
        LOGGER.debug("row => {}, column => {}".format(row, _column))
        if row < 0 or _column < 0:
            raise ValueError(WRONG_INDEX_ERROR_STRING)
        try:
            LOGGER.debug(self.water_distrubution_at_layers)
            glass = self.water_distrubution_at_layers[row]
            return glass.filled/(row + 1.0)
        except:
            if(row<=self.size and _column < row):
                raise WaterNotFilledException()
            raise ValueError(WRONG_INDEX_ERROR_STRING)



