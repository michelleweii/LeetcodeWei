class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        result = n
        for i in range(1,n):
            result *= i
        count_0 = 0
        num = str(result)
        num = num[::-1]
        # print(num)
        for i in range(len(num)):
            if num[i] == '0':
                count_0 += 1
            else:
                return count_0



    # def factorial(self,n):
    #     if n==1:
    #         return 1
    #     else:
    #         return n*factorial(n-1)


def main():
    n = 3
    myResult = Solution()
    print(myResult.trailingZeroes(n))

if __name__ == '__main__':
    main()