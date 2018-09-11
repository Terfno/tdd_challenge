import sys

class Calc_price():
    def calculater_price(self, values):
        round=lambda x:(x*2+1)//2
        sum = 0
        for value in values:
            sum += int(value)
        ans = sum * 1.1
        ans = int(round(ans))
        return ans

    def input_to_data(self, input):
        result = []
        lines = []
        input = input.read()
        input = input.split('\n')
        for i in input:
            i = i.split(',')
            lines.append(i)
        lines.pop(-1)
        for i in lines:
            if i == [''] :
                result.append([])
                continue
            result.append(list(map(lambda x: int(x), i)))
        return result

    def calculater(self,input):
        result = []
        input = self.input_to_data(input)
        for i in input:
            result.append(self.calculater_price(i))
    
        return result

if __name__ == '__main__':
    calc_price = Calc_price()
    print(calc_price.calculater(sys.stdin))
