class Calc_price():
    def calculater_price(self, values):
        round=lambda x:(x*2+1)//2
        sum = 0

        for value in values:
            sum += value

        ans = sum * 1.1
        ans = int(round(ans))
        print(ans)
        return ans
