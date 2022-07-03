"""
middle 2022-05-22 （字节常考）
【时间复杂度】https://leetcode.cn/problems/k-th-smallest-prime-fraction/solution/gong-shui-san-xie-yi-ti-shuang-jie-you-x-8ymk/
# 优先队列，大顶堆（好理解），时间复杂度n^2log(k)
# k路归并，小顶堆，时间复杂度O(klogn)，k是n-1
"""
# 时间复杂度：O(klogn)，优先级队列的最大长度为n-1，每次入队出队的时间复杂度为O(log(n−1))，一共有 k 次操作，
# 去除常数项，所以，总的时间复杂度为 O(klogn)。
import heapq
# https://leetcode.cn/problems/k-th-smallest-prime-fraction/solution/pythonjavajavascriptgo-zui-xiao-dui-by-h-l2z3/
class Solution:
    def kthSmallestPrimeFraction(self, arr, k):# int) -> List[int]:
        pq=[] # 最小堆
        for i in range(1,len(arr)):
            # 分数、分母坐标、分子坐标
            heapq.heappush(pq,(1/arr[i],i,0)) # 1是最小素数
        # 维护容量为k的堆
        for _ in range(k):
            val, j, i=heapq.heappop(pq) # 弹出最小的元素
            # print('pop',arr[i],arr[j])
            if i+1<j: # if只做一次
                print(arr[i+1],arr[j],i+1,j)
                heapq.heappush(pq,(arr[i+1]/arr[j],j,i+1)) # 加入比最小元素稍微大一点的，即分母不动，分子+1
        # print(pq)
        return [arr[i],arr[j]]

if __name__ == '__main__':
    arr = [1,2,3,5] # i<j,arr[i]/arr[j]
    k = 3
    # 已构造好的分数,排序后如下所示:
    # 1/5, 1/3, 2/5, 1/2, 3/5, 2/3
    # 很明显第三个最小的分数是 2/5
    print(Solution().kthSmallestPrimeFraction(arr,k))