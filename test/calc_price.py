import unittest
from calc_price import Calc_price

class TestCalculatePrice(unittest.TestCase):
    def test_calculater_price(self):
        calc_price = Calc_price()
        assert 24 == calc_price.calculater_price([10, 12])
        assert 62 == calc_price.calculater_price([40, 16])
        assert 160 == calc_price.calculater_price([100, 45])
        assert 171 == calc_price.calculater_price([50, 50, 55])
        assert 0 == calc_price.calculater_price([])
