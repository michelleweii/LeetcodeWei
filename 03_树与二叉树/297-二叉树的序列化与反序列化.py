"""
hard 2021-12-23 bi-tree
https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/solution/shou-hui-tu-jie-gei-chu-dfshe-bfsliang-chong-jie-f/
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# dfs思路
class Codec:
    # 选择前序遍历，是因为 根|左|右根∣左∣右 的打印顺序，在反序列化时更容易定位出根节点的值。
    # 遇到 null 节点也要翻译成特定符号，反序列化时才知道这里是 null
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root: return 'x' # 遍历到 null 节点
        left = self.serialize(root.left)
        right  = self.serialize(root.right)
        return str(root.val)+','+str(left)+','+str(right) # 按  根,左,右  拼接字符串
        # return str(root.val)+','+left+','+right
        # 看图,前序遍历序列化 1,2,x,x,3,4,x,x,5,x,x

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        nodelist = data.split(',')
        return self.build_tree(nodelist)

    def build_tree(self, data):
        root = data.pop(0)

        if root=='x': # 是X，返回null节点
            return None

        root = TreeNode(root)
        root.left = self.build_tree(data)
        root.right = self.build_tree(data)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))