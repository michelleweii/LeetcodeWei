import itertools
# from itertools import permutations
# permutations返回list的全排列
print(list(itertools.permutations([1, 2, 3])))
# 后一位2
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
# 后一位3
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
# 不填默认是list的长度
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# 在实际使用过程中，将元组变为list
resultpermu = [list(i) for i in itertools.permutations([1, 2, 3])]
# print(resultpermu)
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

# 需要注意的是函数是根据他们的位置来计算组合的，而不是他们的值，所以有重复的结果。
# print(list(itertools.permutations([1,1,2])))
# [(1, 1, 2), (1, 2, 1), (1, 1, 2), (1, 2, 1), (2, 1, 1), (2, 1, 1)]
rs = []
# 去重
for i in itertools.permutations([1, 1, 2]):
    if list(i) not in rs:
        rs.append(list(i)[:])
# print(rs)
# [[1, 1, 2], [1, 2, 1], [2, 1, 1]]

print('-----combinations-------')
nums1 = [1,2,3]
nums2 = [1,1,2]
print(list(itertools.combinations(nums1,3)))
# [(1, 2, 3)] # 三个数字三三组合当然只有一个
print(list(itertools.combinations(nums1,2)))
# [(1, 2), (1, 3), (2, 3)] 三个数字量量组合，有多少的结果
print(list(itertools.combinations(nums2,2)))
# [(1, 1), (1, 2), (1, 2)]

print('----------product---------------')
print(list(itertools.product(nums1,repeat=2)))
# [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
# 如果repeat=3
# 在=2的基础上，每一项再找一遍
# [(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 2, 1), (1, 2, 2), (1, 2, 3), (1, 3, 1), (1, 3, 2), (1, 。。。
print(list(itertools.product('abc','134')))
# [('a', '1'), ('a', '3'), ('a', '4'), ('b', '1'), ('b', '3'), ('b', '4'), ('c', '1'), ('c', '3'), ('c', '4')]
# repeat默认=2

print('-------------groupby-------------------')
str1 = "cataaaaa"
str2 = "aaabbbbcccc"
for key,group in itertools.groupby(str1):
    print(key,list(group))
# c ['c']
# a ['a']
# t ['t']
# a ['a', 'a', 'a', 'a', 'a']
for key,group in itertools.groupby(str2):
    print(key,list(group))
# a ['a', 'a', 'a']
# b ['b', 'b', 'b', 'b']
# c ['c', 'c', 'c', 'c']
aftergroupby = itertools.groupby(str2)
print(aftergroupby) # <itertools.groupby object at 0x10e0fbe58>
# 需要通过for取出来值


import collections
# trydict = collections.defaultdict(str2) # TypeError: first argument must be callable or None
# 这里str2不是空的，所以报错
# for key,value in trydict:
#     print(key,value)