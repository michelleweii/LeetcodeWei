"""
middle 2021-12-14 bi-tree(dfs)+前缀和（字节）
区别：不用从root节点开始、也不用叶子节点结束的路径，任意的节点都可以当做路径的start; 输出有几条路径，不用打印明细；
相关题：112、113
https://leetcode-cn.com/problems/path-sum-iii/solution/gong-shui-san-xie-yi-ti-shuang-jie-dfs-q-usa7/

|朴素版：2个dfs
dfs1让每个节点都当作根节点（前序遍历），dfs2对新的树进行遍历（回溯），退化到lc112；

|优化版：dfs+前缀和
朴素版的求解思路：以每个节点为「路径开头」的所有合法路径。
统计以每个节点为「路径结尾」的合法数量的话，（反过来想）
配合原本「从上往下」进行的树的遍历（最完整的路径必然是从原始根节点到当前节点的唯一路径），
* 相当于只需要在完整路径中找到：有多少个节点到当前节点的路径总和为 targetSum。

=>求解从原始起点（根节点）到当前节点b的路径中，有多少节点 a 满足 sum[a...b] = targetSum，
由于从原始起点（根节点）到当前节点的路径唯一，因此这其实是一个「一维前缀和」问题。
具体的，我们可以在进行树的遍历时，记录下从原始根节点 root 到当前节点 cur 路径中，
从 root 到任意中间节点 x 的路径总和，配合哈希表，快速找到满足以 cur 为「路径结尾」的、
使得路径总和为 targetSum 的目标「路径起点」有多少个。

一些细节：由于我们只能统计往下的路径，但是树的遍历会同时搜索两个方向的子树。因此我们应当在搜索完以某个节点为根的左右子树之后，
应当回溯地将路径总和从哈希表中删除，防止统计到跨越两个方向的路径。
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 【朴素版】ac，时间复杂度：O(n^2)
    def pathSum_native(self, root: TreeNode, targetSum): #int) -> int:
        if not root: return 0
        self.target = targetSum
        self.count = 0
        self.dfs1(root)
        return self.count

    def dfs1(self, root):
        if not root:return
        # 操作根节点
        self.dfs2(root, root.val)
        # 遍历左、右子树
        self.dfs1(root.left)
        self.dfs1(root.right)

    def dfs2(self, root, val):# val当前和
        # 出口
        if val==self.target:
            self.count += 1
        if root.left:
            self.dfs2(root.left, val+root.left.val)
            # val+root.left.val 值传递，自带回溯效果
        if root.right:
            self.dfs2(root.right, val+root.right.val)

    # ----------------------------------------------------------
    def pathSum(self, root: TreeNode, targetSum):
        if not root: return 0
        self.count = 0
        self.target = targetSum
        self.hashmap = {}
        self.hashmap[0] = 1 # # 前缀和为0的数量有1个。默认nums[-1]=0
        self.dfs(root, root.val)
        return self.count

    # 具体操作细节退化到lc560
    # key: 前缀和
    # value: key 对应的前缀和的个数
    # 快速找到满足以 cur=b 为「路径结尾」的、使得路径总和为 targetSum的目标「路径起点」有多少个。
    def dfs(self, root, sums):
        # 为啥子没有出口？ if left, if right, 就会结束dfs
        # if not root:return # 加不加都会过？为什么？前序遍历不加会报错
        # 以 当前节点 b 为 终点
        self.count += self.hashmap.get(sums-self.target, 0)
        # 有多少节点 a 满足 sum[a...b] = targetSum，
        # b 是当前的sums, 结尾节点的值
        # 维护，这个节点值共出现几次
        self.hashmap[sums] = self.hashmap.get(sums, 0) + 1
        # 开始回溯 ; 以 当前节点 b 为路径的一部分
        if root.left:self.dfs(root.left, sums+root.left.val) # 以root.left为结尾，更新路径上的值
        # sums+root.left.val 自带回溯效果
        if root.right:self.dfs(root.right, sums+root.right.val)
        # 当子树结束时，应当把子树从哈希表中移除 (回溯：将一切复原，然后结束)
        self.hashmap[sums] = self.hashmap.get(sums,0)-1

    #### 2022-04 递推关系
    # presum[a..b]=target
    #             =nums[b]-nums[a-1]
    # => target=cur当前结尾的值-nums[a-1]
    # => nums[a-1]=cur当前结果的值-target
    # => 求nums[a-1]共出现几次？

if __name__ == '__main__':
    pass