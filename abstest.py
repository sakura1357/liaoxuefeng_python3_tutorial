# _*_ coding: utf-8 _*_
def my_abs(x):
    # 参数类型检查 isinstance(x, DataType)
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
