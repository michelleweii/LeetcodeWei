"""
easy 2021-12-17 贪心入门
https://programmercarl.com/0455.%E5%88%86%E5%8F%91%E9%A5%BC%E5%B9%B2.html
"""
class Solution(object):
    def findContentChildren(self, g, s):
        g = sorted(g) # 胃口需求，升序
        s = sorted(s) # 糖果，升序
        child = 0 # 已满足几个孩子
        cookie = 0 # 尝试了几个糖果
        # 思路1：优先考虑饼干，小饼干先喂饱小胃口
        while cookie < len(s) and child < len(g):
            if g[child] <= s[cookie]: # 孩子的胃口<饼干大小
                child += 1 # 满足孩子数+1
            cookie += 1 # 尝试下一个饼干
        return child

    # 超出时间限制，自己写的
    def findContentChildren1(self, g, s):
        g = sorted(g) # 需求
        s = sorted(s)  # 糖果
        cnt = 0
        flag = []
        for index_g,val_g in enumerate(g):
            for index_s, val_s in enumerate(s):
                if val_s >= val_g and index_s not in flag:
                    cnt += 1
                    flag.append(index_s)
                    break
        return cnt

if __name__ == '__main__':
    g = [1,2]
    s = [1,2,3]
    print(Solution().findContentChildren(g,s))