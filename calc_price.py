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
        return [[10,12,3],[40,16],[100,45]]
        # lines = input.split('\n')
        # for line in lines:
        #     value_list = line.split(',')

#    def execute(self):


# def some_method():
#     calc_price = Calc_price()
#     test_file = open('input.txt')
#     lines = test_file.readlines()  # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
#     test_file.close()
#     for line in lines:
#         values = line.split(',')
#         ans = calc_price.calculater_price(values)



if __name__ == '__main__':
    # シェル等から実行されたときに実行される内容
    # ここは他のモジュールから import された時等は実行されない
    while(True):
        try:
            line = input()
        except EOFError:
            break
        values = line.split(',')
        calc_price = Calc_price()
        ans = calc_price.calculater_price(values)
        print(ans)