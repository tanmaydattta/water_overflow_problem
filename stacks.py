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
    def pour(n_liters:float):
        pass
    
    @abstractclassmethod
    def get_water_at_glass(row:int, column:int):
        pass

class TriangularStack(WaterStack):
    "Implementation for required water stack"
    pass

