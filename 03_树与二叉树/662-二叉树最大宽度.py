"""
middle 2022-06-20 bfs
https://leetcode.cn/problems/maximum-width-of-binary-tree/solution/662-er-cha-shu-zui-da-kuan-du-by-jue-qia-djxn/
"""
# 满二叉树下标性质
# 1.对于满二叉树，从根节点开始可以对节点编号1，2，...，某节点p的左子节点的序号为2p，右子节点的序号为2p+1；
# 2.若令根节点的序号p为0，且左子节点的序号为2p，右子节点的序号为2p+1，则每层节点中，节点的序号即代表节点在这一层中的位置索引。

class Solution:
    def widthOfBinaryTree(self, root):# Optional[TreeNode]) -> int:
        # bfs，队列中记录每个节点的root，pos，按层更新max_width
        if not root:return 0
        max_width=0
        queue=[(root,1)] # 记录每个节点的（root.val，pos）
        while queue:
            width=queue[-1][1]-queue[0][1]+1
            if width>max_width:max_width=width
            
            for _ in range(len(queue)):
                node,pos=queue.pop(0)
                if node.left:
                    queue.append((node.left, pos*2))
                if node.right:
                    queue.append((node.right, pos*2+1))
        return max_width
        