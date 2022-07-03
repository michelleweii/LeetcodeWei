"""
easy 2021-12-28 bst遍历
https://www.programmercarl.com/0700.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E6%90%9C%E7%B4%A2.html#%E9%80%92%E5%BD%92%E6%B3%95
# 为什么要有返回值:
#   因为搜索到目标节点就要立即return，
#   这样才是找到节点就返回（搜索某一条边），如果不加return，就是遍历整棵树了。
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root or root.val==val:return root
        if val>root.val: return self.searchBST(root.right, val)
        # 这里可能会疑惑，在递归遍历的时候，什么时候直接return 递归函数的返回值，什么时候不用加这个 return呢。
        # 如果要搜索一条边，递归函数就要加返回值，这里也是一样的道理。
        # 因为搜索到目标节点了，就要立即return了，这样才是找到节点就返回（搜索某一条边），如果不加return，就是遍历整棵树了。
        elif val<root.val: return self.searchBST(root.left, val)
        # return None

if __name__ == '__main__':
    pass