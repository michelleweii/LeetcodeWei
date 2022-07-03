"""
hard 2021-12-22 贪心(没有考过,先放弃了)
https://programmercarl.com/0968.%E7%9B%91%E6%8E%A7%E4%BA%8C%E5%8F%89%E6%A0%91.html#%E6%80%9D%E8%B7%AF
https://leetcode-cn.com/problems/binary-tree-cameras/solution/968-jian-kong-er-cha-shu-di-gui-shang-de-zhuang-ta/
题目：节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。计算监控树的所有节点所需的最小摄像头数量。
分析：从上到下？or从下到上？
从下往上看，局部最优：让叶子节点的父节点安摄像头，所用摄像头最少，整体最优：全部摄像头数量所用最少！
头结点放不放摄像头也就省下一个摄像头， 叶子节点放不放摄像头省下了的摄像头数量是指数阶别的。

-- 确定遍历顺序，在二叉树中如何从低向上推导呢？使用后序遍历也就是左右中的顺序，这样就可以在回溯的过程中从下到上进行推导了。

-- 如何隔两个节点放一个摄像头
0：该节点无覆盖
1：本节点有摄像头
2：本节点有覆盖

明确1：叶子节点不放摄像头，所以空节点也不能是无覆盖0--->想不通，再说吧-。-||
明确2：空节点的状态只能是有覆盖，这样就可以在叶子节点的父节点放摄像头了
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        # Greedy Algo:
        # 从下往上安装摄像头：跳过leaves这样安装数量最少，局部最优 -> 全局最优
        # 先给leaves的父节点安装，然后每隔两层节点安装一个摄像头，直到Head
        # 0: 该节点未覆盖
        # 1: 该节点有摄像头
        # 2: 该节点有覆盖

        result = 0

        # 从下往上遍历：后序（左右中）
        def traversal(curr: TreeNode) -> int:
            nonlocal result

            if not curr: return 2
            left = traversal(curr.left)
            right = traversal(curr.right)

            # Case 1:
            # 左右节点都有覆盖
            if left == 2 and right == 2:
                return 0

            # Case 2:
            # left == 0 && right == 0 左右节点无覆盖
            # left == 1 && right == 0 左节点有摄像头，右节点无覆盖
            # left == 0 && right == 1 左节点有无覆盖，右节点摄像头
            # left == 0 && right == 2 左节点无覆盖，右节点覆盖
            # left == 2 && right == 0 左节点覆盖，右节点无覆盖
            elif left == 0 or right == 0:
                result += 1
                return 1

            # Case 3:
            # left == 1 && right == 2 左节点有摄像头，右节点有覆盖
            # left == 2 && right == 1 左节点有覆盖，右节点有摄像头
            # left == 1 && right == 1 左右节点都有摄像头
            elif left == 1 or right == 1:
                return 2

            # 其他情况前段代码均已覆盖

        if traversal(root) == 0:
            result += 1

        return result


if __name__ == '__main__':
    pass
    # root = [0,0,None,0,0]
    # print(Solution().minCameraCover(root))