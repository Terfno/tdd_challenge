from di_sample import MyMemory

class Calc_price():
    # def __init__(self, d_input, d_output):
    #      self.d_input = d_input
    #      self.d_output = d_output

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

if __name__ == '__main__':
    # シェル等から実行されたときに実行される内容
    # ここは他のモジュールから import された時等は実行されない
    while(True):
        try:
            line = input()
        except EOFError:
            break
        calc_price = Calc_price()
        ans = calc_price.calculater_price(values)
        print(ans)