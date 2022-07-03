# * 将首字符移到末尾并记录所得的字符串，不断重复该操作，虽然记录了无限个字符串，
# * 但其中不同字符串的数目却是有限的，那么一共记录了多少个不同的字符串？
# * 样例输入
# * abab
# * 样例输出
# * 2
# * 样例解释
# * 记录了abab和baba这2个不同的字符串。

# a = "abab"
a = input()
res = set()
res.add(a)
for i in range(1,len(a)):
    k=0
    tmp = a[k+1:]+a[k]
    a = tmp
    # print(a)
    res.add(a)
print(len(res))

# 答案是使用KMP算法，求出字符串的最小循环周期T