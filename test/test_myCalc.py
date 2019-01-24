from unittest import TestCase
from src.MyCalc import MyCalc

class TestMyCalc(TestCase):
    def setUp(self):
        self.calc = MyCalc()

    def test_add(self):
        self.assertEqual(3, self.calc.add(1,2))
        self.assertAlmostEqual(15.0, self.calc.add(12.5, 2.5))
        self.assertAlmostEqual(8.0, self.calc.add(2, 6.0))

