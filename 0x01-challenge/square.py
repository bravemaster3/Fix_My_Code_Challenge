#!/usr/bin/python3
"""
square class definition
"""


class Square():
    """square class definition"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """instanciation method"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """Perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """method for nice representation of a square"""
        return "{}/{}".format(self.width, self.height)
