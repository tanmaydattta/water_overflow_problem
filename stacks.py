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
        self.water_distrubution_at_layers  = {}
    
    def pour(self, water_volume:float)-> bool:
        """
        Method to pour n liters into the stack
        """
        current_layer = 0
        unit_capacity = self.unit_capacity
        while water_volume > 0 and current_layer < self.size:
            (capacity, filled) = self.water_distrubution_at_layers.get(
                current_layer, (current_layer*unit_capacity, 0.0))
            if filled < capacity:
                delta = capacity-filled
                water_volume -= delta
                self.water_distrubution_at_layers[current_layer] = (capacity, filled+delta)
            current_layer += 1
        return True
    
    def get_water_at_glass(self, row: int, column: int) -> float:
        pass



