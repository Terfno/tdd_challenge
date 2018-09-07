import math
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

class Calc_price():
    def calculater_price(self, values):
        sum = 0
        for value in values:
            sum += value

        flo = sum * 1.1
        return Decimal(str(flo)).quantize(Decimal('1'), rounding=ROUND_HALF_EVEN)