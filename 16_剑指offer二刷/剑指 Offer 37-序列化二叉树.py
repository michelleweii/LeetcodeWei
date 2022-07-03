"""
hard 二叉树
2021-07-26
"""
from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    # 1,2,3,#,#,4,5
    def serialize(self, root): # 将树转为list(层次遍历)
        if not root:return "#"
        queue = [root]
        ans = []
        while queue:
            node = queue.pop(0)
            if not node:
                ans.append('#')
            else:
                ans.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        while ans and ans[-1] == '#':
            ans.pop()
        return ','.join(ans)

    def deserialize(self, data): # 还原树
        root_nums = data.split(',')
        if not root_nums or root_nums[0]=='#' or root_nums[0]=='':
            return None
        root = TreeNode(int(root_nums.pop(0)))
        is_left = True # 当前节点该连左子树or右子树
        cur_node = root # 当前节点
        tree_node = [] # 已经连接的节点，为了找到下一个最左节点
        while root_nums:
            num = root_nums.pop(0)
            if is_left:
                is_left = False
                if num != '#':
                    cur_node.left = TreeNode(int(num))
                    tree_node.append(cur_node.left)
            # 开始右节点
            else:
                is_left = True
                if num != '#':
                    cur_node.right = TreeNode(int(num))
                    tree_node.append(cur_node.right)
                cur_node = tree_node.pop(0)
        return root



if __name__ == '__main__':

    root = TreeNode(1)
    a = TreeNode(2)
    b = TreeNode(3)
    c = TreeNode(4)
    d = TreeNode(5)
    root.right = b
    root.left = a
    b.right = d
    b.left = c
    codec = Codec()
    print(codec.serialize(root)) # 树转为str
    print(codec.deserialize(codec.serialize(root)))

    # nums = [1, 2, 3, 4, 5]
    # print(nums.pop())