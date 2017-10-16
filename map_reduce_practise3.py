from functools import reduce

def str2float(s):
    # 字符转数字
    def char2num(s):
        return {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, '.' : '.'}[s]

    # 整数部分
    def fn(x, y):
        return x * 10 + y
   
    # 切割字符串并进行处理计算
    [s1, s2] = s.split('.')

    # 整数部分正常计算 [1, 2, 3]
    float_integer = reduce(fn, list(map(char2num, s1)))
    # 小数部分: [4, 5, 6]先按照整数部分计算得456，然后除以10^len(s2)，10^3=1000
    # 456/1000 = 0.456
    # ** 表示幂计算，乘方，10**3，即10的3次方
    float_decimal = reduce(fn, list(map(char2num, s2)))/(10**len(s2))
    return float_integer + float_decimal

print(str2float('123.456'))