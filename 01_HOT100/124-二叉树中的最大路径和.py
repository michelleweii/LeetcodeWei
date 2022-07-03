"""
hard 2021-11-14 递归遍历（字节/虾皮/美团）
任意节点出发到任意节点结束所构成的最大路径。
图解有助于理解 https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/solution/shou-hui-tu-jie-hen-you-ya-de-yi-dao-dfsti-by-hyj8/
1、用这个node做根，它能不能成为答案的最大值？max(maxsum, inmax)
2、这个node不做根，当其他node的路径，那么它提供 它左or右子树的最大值。=》每个节点都有做根和不做根两种选择
【核心在于计算结果的时候要计算左右子树，递归返回的时候只能返回较大的一边】
"""
# 先理解 LC543二叉树的直接 更容易一点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max_sum = float("-inf") # 最大路径和

    # 返回经过root的单边分支最大和， 即Math.max(root, root+left, root+right)
    def maxPathSum(self, root):
        if not root:return 0
        # 返回当前子树能向父节点“提供”的最大路径和。
        # 即，一条从父节点延伸下来的路径，能在当前子树中捞取的最大收益。
        def dfs(root): # max_gain
            if not root:return 0 # 遍历到null节点(叶子节点)，收益0
            left_gain, right_gain = dfs(root.left), dfs(root.right) # 左\右子树提供的最大路径和
            # 【某子树内部最大值】
            in_maxsum = left_gain + root.val + right_gain # 当前子树内部的最大路径和
            #【某子树向外部提供的最大值】 innerMax 是当前node作为root的时候的最大值，也就是说只有在当前节点是root的时候才能够同时选左边和右边；
            # 不然的话，作为路径上的一份子，只能选择左边或者右边。【对外只能作为路径上的一份子】
            # 有很多节点都可以当根节点，比较一下哪个根能做结果。
            self.max_sum = max(self.max_sum, in_maxsum) # 挑战最大纪录
            #【全局最大值】
            out_sum = root.val + max(0, max(left_gain, right_gain)) # 当前子树对外提供的最大和,只能走左边or右边。（不要最外面的max也可以）
            return max(out_sum, 0) # 当前子树能向父节点“提供”的最大路径和

        dfs(root)
        return self.max_sum
"""
int max = Integer.MIN_VALUE;
    public int maxPathSum(TreeNode root) {
        if (root == null) {
            return 0;
        }
        dfs(root);
        return max;
    }

    /**
     * 返回经过root的单边分支最大和， 即Math.max(root, root+left, root+right)
     * @param root
     * @return
     */
    public int dfs(TreeNode root) {
        if (root == null) {
            return 0;
        }
        //计算左边分支最大值，左边分支如果为负数还不如不选择
        int leftMax = Math.max(0, dfs(root.left));
        //计算右边分支最大值，右边分支如果为负数还不如不选择
        int rightMax = Math.max(0, dfs(root.right));
        //left->root->right 作为路径与已经计算过历史最大值做比较
        max = Math.max(max, root.val + leftMax + rightMax);
        // 返回经过root的单边最大分支给当前root的父节点计算使用
        return root.val + Math.max(leftMax, rightMax);
    }
"""
if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.left = b
    a.right = c
    print(Solution().maxPathSum(a))
