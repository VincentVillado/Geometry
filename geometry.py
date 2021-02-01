"""
Geometry module provides classes to help determine geometric calclations
"""
import math

class Circle:
    def __init__(self, radius: float):
        """
        Constructer
        ;param radius: a non-negative number (if a negative number is passed it will be converted to a posotive number
        :param radius:
        """
        self.radius = abs(radius)

    def __str__(self) -> str:
        """
        Formats a string showing the attributes of the circle
        :return: formatted string
        """
        return f"Circle with radius {self.radius}"
    pass

    def area(self) -> float:
        """
        Calculates the area of the circle
        :return: non-negative number
        """
        return math.pi * (self.radius ** 2)
    def circumference(self) -> float:
        """
        Calculates the perimeter of the circle
        :return: non-negative number
        """
        pass

class Rectangle:
    pass
