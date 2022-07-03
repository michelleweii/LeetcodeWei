# 利用pow(a, b)函数即可。需要开a的r次方则pow(a, 1/r)。
# 用取余！ python除法/都保留小数点后的数字的

# 不知道为什么leetcode上报错
# class Solution(object):
#     def isPowerOfThree(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         if n==0:
#             return False
#         else:
#             rs = pow(n,1/3)
#             if 3**int(rs) == n:
#                 return True
#             return False

class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 1 :
            l = list(map(int, str(n))) # 妙！
            if sum(l) % 3 == 0:
                n = n // 3
            else:
                return False
        if n <= 0:
            return False
        return True


def main():
    n= 27
    myResult = Solution()
    print(myResult.isPowerOfThree(n))

if __name__ == '__main__':
    main()