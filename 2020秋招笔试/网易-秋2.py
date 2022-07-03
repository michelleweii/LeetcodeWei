"""
思路：

题意为找ai+aj=奇数就交换这两个数尽可能的是最后的序列字典序最小。
显然如果这个数列全是奇数或者全是偶数就没必要交换否则就直接sort。
"""

# python
n = int(input())
a = list(map(int,input().split()))
odd = 0
even = 0
for i in a:
          if i%2: odd=1
          else:even=1
if odd and even:
          print(*sorted(a))
else:print(*a)