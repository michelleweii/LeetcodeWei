"""
middle 2021-12-23 优先队列(堆)+哈希表
https://leetcode-cn.com/problems/top-k-frequent-words/solution/gong-shui-san-xie-xiang-jie-shi-yong-ha-8dxt2/
前K个高频单词，就是TopK问题，只能用小根堆找最大的K个元素啊，用大根堆找的就是最小的K个元素了
题目：词频hashmap高的前，词频一样的情况下，字典序小的前
总结（本题可以学习的点）：
1、sort的进一步使用
2、heapq,priority_queue在python中的使用
3、自定义排序函数的比较> or <符号
4、使用import collections统计词频
"""
class Solution:
    """
    tok问题->降序->构建小顶堆
    1.使用「哈希表」来统计所有的词频
    2.构建大小为 k 按照「词频升序 + (词频相同)字典序倒序」的优先队列
    3.对所有元素进行遍历，尝试入堆
    4.输出堆内元素，并翻转
    """
    def topKFrequent(self, words, k):# -> List[str]:
        import heapq

        hashmap = {}
        for s in words:
            hashmap[s] = hashmap.setdefault(s, 0) + 1

        heap = []
        for key, value in hashmap.items():
            # print(key, value, (-value, key))
            heapq.heappush(heap, (-value, key))
        res = []
        for _ in range(k):
            # headq默认先弹小的数
            res.append(heapq.heappop(heap)[1])
        return res

    def py_api(self, words, k):
        import collections
        # https://leetcode-cn.com/problems/top-k-frequent-words/solution/an-zhao-duo-ge-guan-jian-zi-pai-xu-by-ae-rd32/
        hash = collections.Counter(words)
        res = sorted(hash, key=lambda word:(-hash[word], word)) #词频 倒序排列, 若词频相同，按字母顺序排序 正序排列
        return res[:k]

# 解法2
class Cmp:
    def __init__(self, fre, word):
        self.fre = fre
        self.word = word

    def __lt__(self, other):
        if self.fre != other.fre:
            return self.fre > other.fre  # 按照期望的前后顺序
        return self.word < other.word

class Solution2:
    def topKFrequent(self, words, k):
        import heapq
        import collections
        C, CQ, ans = collections.Counter(words), [], []
        for c in C.items():
            heapq.heappush(CQ, Cmp(c[1], c[0]))
        while CQ and k > 0:
            ans.append(heapq.heappop(CQ).word)
            k -= 1
        return ans

"""
python
from collections import Counter # 用于后面调用哈希计数表
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        Count_words=Counter(words)  #对单词列表进行计数
        result=self.inorder(Count_words)    #按规则排序的列表
        return result[0:k]

    def inorder(self,d):
        compare=lambda x,y:-1 if d[x]>d[y] or (d[x]==d[y] and x<y) else 1
        #x的次数比y多或者次数相等字母顺序小，不交换x,y位置//y的次数比x多，排序时交换位置
        res=sorted(d.keys(),key=functools.cmp_to_key(compare))
        return res
"""

"""
优先队列demo
from queue import PriorityQueue

q = PriorityQueue()

q.put((2, 'code'))
q.put((1, 'eat'))
q.put((3, 'sleep'))

while not q.empty():
    next_item = q.get()
    print(next_item)

# Result:
#   (1, 'eat')
#   (2, 'code')
#   (3, 'sleep')
"""
if __name__ == '__main__':
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    # 输出: ["i", "love"]
    # 解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
    #     注意，按字母顺序 "i" 在 "love" 之前。
    print(Solution().topKFrequent(words, k))