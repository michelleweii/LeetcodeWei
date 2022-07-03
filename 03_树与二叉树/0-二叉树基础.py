
class TreeNode:
    def __init__(self, x=0):
        self.val = x
        self.left = None
        self.right = None
## 先序非递归



## 中序非递归
def inorder(root):
    # 左根右
    if not root: return []
    stk, res = [], []
    cur = root
    while stk or cur:
        while cur:  # 找到最左侧子树
            stk.append(cur)
            cur = cur.left
        cur = stk.pop()
        res.append(cur.val)
        cur = cur.right  # 当根弹出了，就进入右子树
    return res

## 后序非递归
##


## 层次遍历
def levelOrder(root):
    if not root:return root
    q=[root]
    res=[]
    while q:
        path,size=[],len(q)
        for i in range(size):
            node=q.pop(0)
            path.append(node.val)
            if node.left:
                path.append(node.left)
            if node.right:
                path.append(node.right)
        res.append(path[:])
    return res


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


