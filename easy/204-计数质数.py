class Solution(object):
##
# 2. 一个合数必然能分解成质因子之积。因此我们每当找到一个素数，设它为 i，
# 那么对于2∗i,3∗i,4∗i,....,n。2∗i,3∗i,4∗i,....,n这些数来说肯定都是合数。删掉！

# so 只需遍历[2,sqrt(n)]，因为超过部分如果不是素数，则在前面的因子的倍数（cur_value）已经被删除了。
    def countPrimes(self, n):
        if n < 3:
            return 0
        primes = [True]*n
        # print(primes) # [True, True, True, True]
        primes[0] = primes[1] = False
        for i in range(2,int(n**0.5)+1):
            # if primes[i]: # 每当找到一个素数，ture
                # 素数的倍数都是合数
            # print(i) # i: 2,3,4,5...
            # primes[i*i:n:i] == [True, True, True]
            # [::i]取i的倍数
            primes[i*i:n:i]=[False]*len(primes[i*i:n:i])
            # ValueError: attempt to assign sequence of size 1 to extended slice of size 3
        # print(primes)
        # [False, False, True, True, False, True, False, True, False, False]
        return sum(primes)

    """
    def countPrimes(self, n):
        # 超时
        count = 0
        if n <= 1:
            return 0
        for num in range(2,n):
            count+=self.judgePrimes(num)
        return count

    def judgePrimes(self,n):
        tmp = int(n ** 0.5) + 1
        for i in range(2, tmp):
            if n % i == 0:
                return 0
        return 1
    """


if __name__ == '__main__':
    n = 10
    ans = Solution()
    print(ans.countPrimes(n))