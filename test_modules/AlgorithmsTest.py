import unittest

from scripts.Algorithm0 import make as make0
from scripts.Algorithm1 import make as make1
from scripts.Algorithm2 import make as make2
from scripts.Algorithm3 import make as make3


class AlgorithmsTest(unittest.TestCase):
    
    def test_0_algorithm(self):
        self.assertAlmostEqual(make0(200.0, 15, 0.12, 0.02, 0.04, 0.01, 0.14, 24), 714.29) 
        self.assertAlmostEqual(make0(20000.0, 15, 0.12, 0.02, 0.04, 0.01, 0.14, 17), 57142.86)
        
    def test_1_algorithm(self):
        self.assertAlmostEqual(make1(200.0, 15, 0.12, 0.02, 0.04, 0.01, 0.14, 24), 606.21)
        self.assertAlmostEqual(make1(20000.0, 15, 0.12, 0.02, 0.04, 0.01, 0.14, 17), 50000.12)
        
    def test_2_algorithm(self):
        self.assertAlmostEqual(make2(200.0, 15, 0.12, 0.02, 0.04, 0.01, 0.14, 24), 625.12)
        self.assertAlmostEqual(make2(20000.0, 15, 0.12, 0.02, 0.04, 0.01, 0.14, 17), 51282.15)
        
    def test_3_algorithm(self):
        self.assertAlmostEqual(make3(200.0, 15, 0.12, 0.02, 0.04, 0.01, 0.14, 24), 689.69)
        self.assertAlmostEqual(make3(20000.0, 15, 0.12, 0.02, 0.04, 0.01, 0.14, 17), 55555.58)