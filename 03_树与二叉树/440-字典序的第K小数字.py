"""
hard 2022-05-22 dfs（字节跳动常考题）前序遍历
类似386
https://leetcode.cn/problems/k-th-smallest-in-lexicographical-order/solution/ben-ti-shi-shang-zui-wan-zheng-ju-ti-de-shou-mo-sh/
"""
# 怎么确定一个前缀下所有子节点的个数？
# 如果第 k 个数在当前的前缀下，怎么继续往下面的子节点找？ 往子树里面去看prefix *= 10；
# 如果第 k 个数不在当前的前缀，即当前的前缀比较小，如何扩大前缀，增大寻找的范围？当前的前缀小了prefix++；
#
# 第一层个数，next-cur=2-1=1
# 第二层个数，next*10-cur*10=20-10=10
# 第三层个数，next*10*10-cur*10*10=100，如果该范围超过了n，所以要与n值取min。

# count+=min(next,n+1)-cur的理解？
class Solution:
    def findKthNumber(self, n: int, k: int):# -> int:
        # 计算以数字 i 开头且不超过最大数字 n 的数字个数
        def get_cnt(prefix, n):
            cur=prefix
            next=prefix+1 # 下一个前缀
            count=0
            # 当前的前缀不能大于上界n
            while cur<=n:
                # 下一峰头减去此峰头
                # count+=next-cur, 当 next 的值大于上界的时候，那以这个前缀为根节点的十叉树就不是满十叉树了
                count+=min(next,n+1)-cur # 下一个前缀的起点减去当前前缀的起点，目前位置所拥有的个数
                # n+1是因为 假若现在上界 n为 12，算出以 1 为前缀的子节点数，首先 1 本身是一个节点，接下来要算下面 10，11，12，一共有 4 个子节点。
                cur*=10
                next*=10
#             // 如果说刚刚prefix是1，next是2，那么现在分别变成10和20
#             // 1为前缀的子节点增加10个，十叉树增加一层, 变成了两层
#
#             // 如果说现在prefix是10，next是20，那么现在分别变成100和200，
#             // 1为前缀的子节点增加100个，十叉树又增加了一层，变成了三层
            return count

        prefix=1
        p=1 # 第一字典序小的(就是1) # 当前已经走了多少个字典序了,p：第几个数，<=>  k:第k个数
        while p<k:
            count=get_cnt(prefix,n)
            print('count',count) # 5 (1, 10, 11, 12, 13)
            if p+count>k: # 第 k 个数在当前的前缀下
                prefix*=10
                p+=1
            elif p+count<=k: # 第 k 个数不在当前的前缀，即当前的前缀比较小，如何扩大前缀，增大寻找的范围
                prefix+=1
                p+=count
        return prefix


if __name__ == '__main__':
    n=13
    k=3 # 解释: 字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。
    print(Solution().findKthNumber(n,k))