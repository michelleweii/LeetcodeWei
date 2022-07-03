# -*- coding:utf-8 -*-
import numpy as np
"""
2020/12/21 重新整理
"""
nums1 = [1,2,3]
nums2 = []
print(nums1+nums2) # [1, 2, 3]

n = 1
print(n//3) # 0
ii = 5
print(ii//2+1) # 3

print("------list排序---------")
"""
list.sort() 排序后改变了原本的list
sorted(list) 排序后不会改变原list，默认升序
"""
nums = [10,3,8,9,4]
nums.sort() # 改变了原本的nums列表
print("sort: ", nums) # [3, 4, 8, 9, 10]
a = [5, 2, 3, 1, 4]
print("sorted: ", sorted(a)) # 升序 # [1, 2, 3, 4, 5]
print(a) # [5, 2, 3, 1, 4] sorted不改变原list
print(sorted(a,reverse=True)) # 实现降序 # [5, 4, 3, 2, 1]



print("--------求幂----------")
print(np.arange(3,6)) # [3 4 5]
scales = 2**np.arange(3,6)
print(scales) # [8 16 32]

for i in range(4):
    print(i) # 0,1,2,3
bb = [i for i in range(4)]
print(bb) # [0, 1, 2, 3]

for i in range(0):
    print(i) # 啥也不输出


# 取不存在的下标也无所谓
sss = "abc"
print(sss[2:3]) #c
print(sss[2:4]) #c
print(sss[2:5]) #c

# 求均值
L = [1,2,3,4,5]
print(np.mean(L))

print("---------- 删除元素 ----------------")
# del[1:3]删除指定区间
L2 = [1,2,3,4,5]
del L2[1:3]
print(L2) # [1, 4, 5]，删除1，2下标
del L2[0]
print(L2) # [4, 5],删除0下标
# del L2
# print(L2) # NameError: name 'L2' is not defined

a = [0, 2, 2, 3]
a.remove(2)
print(a) # [0, 2, 3],删除指定元素

b = [4, 3, 5]
print(b.pop(1)) # 3
print(b) # [4, 5]

s = "abcdefs"
print(s[0:3]) # abc

# 字符串用完sorted(0)之后会转为list
c = "acbed"
print(sorted(c)) # ['a', 'b', 'c', 'd', 'e']

seats = [0,1,1,0,0,0]
print(seats.index(1)) # 1 取出第一个值为1的下标

print("-----------切片--------------")
alist = [1,2,3,4]
print(alist[0:3:2]) # [1, 3]
print(alist[1:]) # [2, 3, 4]
print(alist[2:]) # [2, 3, 4]
print(alist[3:]) # [4]
print(alist[4:]) # []

a = "loveleetcode"
print(a[:-1]) # loveleetcod
print(a[-5::-1]) # octeelevol

# 翻转列表
listNode = [1,2,3]
print(listNode[::-1])  # [3, 2, 1]


A = [1,2,3]
print("origin A:{}".format(A)) # origin A:[1, 2, 3]
A[0] = A[2]
print("changed A:{}".format(A)) # changed A:[3, 2, 3]


a = [0 for _ in range(3)]
# b = [a for _ in range(3)]
# print(b) # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
b = [list(a) for _ in range(3)]
print(b) # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


print('')
print('-----------------2019/1/3--------------------------')
print("二维数组相关")
n1 = list(np.full((1,3),2))
n2 = list(np.full((1,3),3))
n3 = list(np.full((1,3),4))
m = n1+n2+n3
print(n1, n2, n3) # [array([2, 2, 2])] [array([3, 3, 3])] [array([4, 4, 4])]
print(m) # [array([2, 2, 2]), array([3, 3, 3]), array([4, 4, 4])]

A = [[1,2,3,4,5,6],
[7,8,9,10,11,12],
[13,14,15,16,17,18]]
A = np.mat(A)
print(A[0,:]) # [[1 2 3 4 5 6]]
print(A[0,:1]) #[[1]]
print(A[0,:4]) # [[1 2 3 4]]
print(A[0,:5]) # [[1 2 3 4 5]]



x,y = 2,4
A = np.ones((3, 5))
print("A: ", A) # 3行5列
#  [[1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]]
for i in range(0, x+1):
    A[i][0] = i
    for j in range(1,y+1):
        A[i][j] = A[i][j-1]+1
print(A)
# [[0. 1. 2. 3. 4.]
#  [1. 2. 3. 4. 5.]
#  [2. 3. 4. 5. 6.]]