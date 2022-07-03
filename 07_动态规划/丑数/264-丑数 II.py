"""
middle 2022-01-28 dp（字节）
https://leetcode-cn.com/problems/ugly-number-ii/solution/gong-shui-san-xie-yi-ti-shuang-jie-you-x-3nvs/
要求返回第n个丑数。
思路：
1. 1 是最小的丑数。
2. 对于任意一个丑数 x，其与任意的质因数（2、3、5）相乘，结果（2x、3x、5x）仍为丑数。
https://leetcode-cn.com/problems/ugly-number-ii/solution/gong-shui-san-xie-yi-ti-shuang-jie-you-x-3nvs/
"""
# 优先队列（小根堆）
# 起始先将最小丑数 1 放入队列
# 每次从队列取出最小值 x，然后将 x 所对应的丑数 2x、3x 和 5x 进行入队。
# 对步骤 2 循环多次，第 n 次出队的值即是答案。
# 时间复杂度：从优先队列中取最小值为 O(1)，往优先队列中添加元素复杂度为 O(logn)。整体复杂度为O(nlogn)。

# 多路归并（三指针）解法
# 使用三个指针来指向目标序列 arr 的某个下标（下标 0 作为哨兵不使用，起始都为 1），
# 使用 arr[下标] * 质因数 代表当前使用到三个有序序列中的哪一位，同时使用 idx 表示当前生成到 arr 哪一位丑数。
class Solution:
    def nthUglyNumber_heap(self, n):
        import heapq
        nums = [2,3,5]
        # 为了防止同一丑数多次进队，我们需要使用数据结构 Set 来记录入过队列的丑数。
        visited = {1}
        pq = [1]
        for i in range(1, n+1):
            x = heapq.heappop(pq) # 每次弹出来的都是当前最小元素
            if i == n:
                return x
            for num in nums:
                tmp = num*x
                if tmp not in visited:
                    visited.add(tmp)
                    heapq.heappush(pq, tmp)
        return -1

    def nthUglyNumber_pointers(self, n):
        ans = [0]*(n+1) # 用作存储已有丑数（从下标 1 开始存储，第一个丑数为 1）
        ans[1] = 1
        # 由于三个有序序列都是由「已有丑数」*「质因数」而来
        # i2、i3 和 i5 分别代表三个有序序列当前使用到哪一位「已有丑数」下标（起始都指向 1）
        i2 = i3 = i5 = 1
        idx = 2
        # 归并
        while idx<=n:
            # 由 ans[iX] * X 可得当前有序序列指向哪一位
            a, b, c = ans[i2] * 2, ans[i3] * 3, ans[i5] * 5
            # 将三个有序序列中的最小一位存入「已有丑数」序列，并将其下标后移
            m = min(a, b, c)
            # 由于可能不同有序序列之间产生相同丑数，因此只要一样的丑数就跳过（不能使用 else if ）
            if m == a:
                i2 += 1
            if m == b:
                i3 += 1
            if m == c:
                i5 += 1
            ans[idx] = m
            idx += 1
        return ans[n]

if __name__ == '__main__':
    n = 10 #12
    ans = Solution()
    print(ans.nthUglyNumber_heap(n))
