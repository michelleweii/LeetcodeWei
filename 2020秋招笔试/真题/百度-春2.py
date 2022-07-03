# 第一行一个字符串A
# 第二行一个字符串B
# 第三行一个正整数Q，表示训练次数
# 接下来m行，每行两个整数L和R，表示一段区间
# comeonmandontconconnect
# on
# 5
# 1 5
# 1 6
# 1 23
# 11 16
# 11 23

# count函数用于统计字符串或列表中某个字符出现的次数
# str.count(str, start= 0, end=len(string))
# #str为字符串，start和end分别为字符串搜索的起始和结束位置

s = input()
target = input()
Q = input()
Q = int(Q)
# print(Q)

for i in range(Q):
    value = input().split()
    start = int(value[0])
    end = int(value[1])
    print(s.count(target,start,end))


# start = input().split()# ['2', '15']
# print(value) # ['2', '15']
# print(start)
# print(end)


# 0
# 1
# 4
# 1
# 2

# 正确答案
# 0
# 1
# 4
# 2
# 3