import unittest
import math
from geometry import Circle


class MyTestCase(unittest.TestCase):
    def test_something(self):
        circ = Circle(5.2)
        print(circ)
        circ_string = str(circ)
        self.assertGreaterEqual(circ_string.find("5.2"), 0)

     def test_area_zero_radius(self):
            circ = Circle(0)
            area = circ.area()
            self.assertEqual(0, area)

     def test_area(self):
         circ = Circle(1)
         self.assertEqual(math.pi, circ.area())



