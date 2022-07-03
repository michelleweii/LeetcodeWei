"""
easy 2021-12-02 二叉树属性
计算每个子树的高度，再+1。
有关于二叉树深度与高度概念区别：https://programmercarl.com/0110.%E5%B9%B3%E8%A1%A1%E4%BA%8C%E5%8F%89%E6%A0%91.html#%E9%80%92%E5%BD%92
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        if root is None: return 0
        # 左子树高度
        LD = self.maxDepth(root.left)
        # 右子树高度
        RD = self.maxDepth(root.right)
        return max(RD,LD)+1

    # 定义queue，层次队列
    def maxDepth2(self, root):
        if not root:return 0
        q, depth = [root], 0
        while q:
            cur_level, size = [],len(q)
            for i in range(size):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # 出当前层
            depth += 1
        return depth

# 真正求取二叉树的最大深度，代码应该写成如下：（前序遍历）
"""
class Solution {
public:
    int result;
    void getDepth(TreeNode* node, int depth) {
        result = depth > result ? depth : result; // 中

        if (node->left == NULL && node->right == NULL) return ;

        if (node->left) { // 左
            depth++;    // 深度+1
            getDepth(node->left, depth);
            depth--;    // 回溯，深度-1
        }
        if (node->right) { // 右
            depth++;    // 深度+1
            getDepth(node->right, depth);
            depth--;    // 回溯，深度-1
        }
        return ;
    }
    int maxDepth(TreeNode* root) {
        result = 0;
        if (root == NULL) return result;
        getDepth(root, 1);
        return result;
    }
};
"""

if __name__ == '__main__':
    a = TreeNode(3)
    b = TreeNode(9)
    c = TreeNode(20)
    d = TreeNode(15)
    e = TreeNode(7)
    a.right = c
    a.left = b
    c.right = e
    c.left = d
    print(Solution().maxDepth(a))
    print(Solution().maxDepth2(a))