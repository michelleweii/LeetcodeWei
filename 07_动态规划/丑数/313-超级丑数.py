"""
middle 2022-01-28 dp
# 和264的区别在于，264是给定primes的个数，求第n个丑数
# 本题事先不知道primes的个数，所以t1,t2,...tn无法确定。
https://leetcode-cn.com/problems/super-ugly-number/solution/dong-tai-gui-hua-java-by-liweiwei1419-1yna/
状态定义：dp[i] 表示第 i + 1 个超级丑数，第 1 个超级丑数是 dp[0]，第 2 个超级丑数是 dp[1]，
基于哪一个超级丑数，可以使用一个长度和 primes 相等的数组 indexes 记录下来，
indexes[i] 表示下一个丑数如果选择了 primes[i] 是基于哪一个下标的超级丑数得到的。
"""
class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        由primes中哪个num来的
        index计算到了哪一位
        """
        m = len(primes)
        # dp[i] 代表第i+1个丑数
        dp = [inf] * n
        dp[0] = 1
        # indexes代表每个质因子现在应该跟哪个丑数相乘
        indexes = [0] * m
        for i in range(1, n):
            # 哪个质因子相乘的丑数将会变化
            changeIndex = 0
            for j in range(m):
                # 如果当前质因子乘它的丑数小于当前的丑数，更新当前丑数并更新变化坐标
                if primes[j] * dp[indexes[j]] < dp[i]:
                    changeIndex = j
                    dp[i] = primes[j] * dp[indexes[j]]
                # 如果相等直接变化，这样可以去重复
                elif primes[j] * dp[indexes[j]] == dp[i]:
                    indexes[j] += 1
            # 变化的坐标+1
            indexes[changeIndex] += 1
        return dp[-1]

    # 超过时间限制
    def nthSuperUglyNumber_heap(self, n, primes):
        import heapq
        pq = [1]
        visited = {1}
        for i in range(1, n+1):
            x = heapq.heappop(pq) # 每次弹出来的都是当前最小元素
            if i == n:
                return x
            for num in primes:
                tmp = num*x
                if tmp not in visited:
                    visited.add(tmp)
                    heapq.heappush(pq, tmp)
        return 1

if __name__ == '__main__':
    n = 12
    primes = [2,7,13,19]
    ans = Solution()
    print(ans.nthSuperUglyNumber(n, primes))
    # print(ans.nthSuperUglyNumber_heap(n,primes))
