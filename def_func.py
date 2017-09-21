# _*_ coding: utf-8 _*_
'''
请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
ax² + bx + c = 0 的两个解。
提示：计算平方根可以调用math.sqrt()函数。
'''
import math


def quadratic(a, b, c):
    temp = b**2 - 4*a*c
    x1 = (-b + math.sqrt(temp)) / (2 * a)
    x2 = (-b - math.sqrt(temp)) / (2 * a)
    return x1, x2

print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))

