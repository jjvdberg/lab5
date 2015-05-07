#!/usr/bin/python3

class Triangle():
    
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
    
    def height(self):
        height = 2 * (self.side_a / self.side_b)
        return height
    
    def area(self):
        area = (self.height() * self.side_b) / 2
        return area