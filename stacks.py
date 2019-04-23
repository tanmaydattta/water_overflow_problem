# -*- coding: utf-8 -*-
"""
Main module for Stack class

"""

from abc import ABC, abstractclassmethod
import logging
from collections import namedtuple

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
    def get_water_at(self, row:int, column:int):
        pass

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
                water_volume -= delta
                self.water_distrubution_at_layers[current_layer] = Glass(capacity=glass.capacity, filled=glass.filled + delta)
            current_layer += 1
        if water_volume > 0: # layers finished and still water left ==> overflow !!
            raise ValueError("Overflow !!")
        return True
    
    def get_water_at(self, row: int, _column: int) -> float:
        """Get the water  row, column currently column has no function
        """
        print(self.water_distrubution_at_layers)
        glass = self.water_distrubution_at_layers[row]
        return glass.filled/(row + 1.0)



