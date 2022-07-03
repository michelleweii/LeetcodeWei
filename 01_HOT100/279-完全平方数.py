"""
middle 2022-05-13 最短路径BFS遍历/DP
BFS的做法，比较巧妙。每一次是原数字减去了一个平方数，直到出现第一个0，此时走过的层数就是最小数量，即为答案
https://leetcode-cn.com/problems/perfect-squares/solution/python3zui-ji-chu-de-bfstao-lu-dai-ma-gua-he-ru-me/
【理解】https://leetcode.cn/problems/perfect-squares/solution/cpython3-1bfs-2bei-bao-wen-ti-by-hanxin_-sfk2/
# 假设数字为7，就是下面这个树，可以等价最短路径(7-1^2,7-2^2)
        7
       / \
      6   3
    / \    \
   5   2    2
  / \   \    \
 4   1   1    1
"""
class Solution(object):
    def numSquares(self, n):
        # python开根号 num_sqrt = n**0.5
        # 对图中所有的点进行预处理，全都没被访问过，设置为false.
        nums = [i * i for i in range(1, int(n ** 0.5) + 1)]

        visited = set()
        queue=[n] # 起始点
        step=1
        while queue:
            # 求当前层有多少个元素
            for _ in range(len(queue)):
                x = queue.pop(0)
                for sq in nums:
                    tmp=x-sq
                    if tmp==0:return step
                    if tmp not in visited:
                        queue.append(tmp)
                        visited.add(tmp)
            step+=1
        return step

if __name__ == '__main__':
    n = 7
    print(Solution().numSquares(n))