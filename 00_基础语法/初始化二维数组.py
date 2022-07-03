# -*- coding:utf-8 -*-
import numpy as np
# 用列表生成m行n列的矩阵
m,n = map(int,input().split())
matrix = [[0]*(m)]*(n)
print(matrix)
# 2 3
# [[0, 0], [0, 0], [0, 0]]
# 这种方式生成的矩阵存在一定的问题，比如，无法给特定位置的元素赋值，例如：
matrix[1][1] = 9
print(matrix)
# [[0, 9], [0, 9], [0, 9]]
# 可见，第二列的元素全部被赋值为9了

# 采用numpy生成想要维度的矩阵
x,y = map(int,input().split())
a = np.ones((x+1,y+1))
print(a)
# [[1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]]
a[1][1] = 9
print(a)
# [[1. 1. 1. 1. 1.]
#  [1. 9. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]]

