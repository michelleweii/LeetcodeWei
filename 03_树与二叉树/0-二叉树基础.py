class TreeNode:
    def __init__(self, x=0):
        self.val = x
        self.left = None
        self.right = None
"""
树7种遍历 https://blog.csdn.net/weixin_31866177/article/details/88294296
先序非递归&递归
中序非递归&递归
后序非递归&递归
层次遍历
- tree非递归笔记
都是先出栈cur = stk.pop()，再记录节点res.append(cur.val)
先序（根左右）如果遍历树的顺序是右左根，那么弹栈出来的就是根左右。（结构类似层次遍历）
中序（左根右）拿到一个阶段就找它的所有左节点入栈。没有左节点就弹栈，弹出的节点去遍历它的右节点。再继续找左节点入栈。
后序（左右根）如果遍历树的顺序是左右根，那么弹栈出来的就是根右左。根右左再弹栈就是左右根。（结构类似层次遍历）
"""

## 先序非递归
def preorder2(root): # 根左右
    """
    利用栈，先将右子树压栈，再将左子树压栈
    先将右子树压栈，再将左子树压栈，这样左子树就位于栈顶，可以保证结点的左子树先与右子树被遍历。
    """
    if not root: return []
    stack = [root]
    res = []
    while stack:
        cur = stack.pop() # 先出栈
        res.append(cur.val) # 记录出栈节点
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
    return res
# def preorder1(root): # 根左右
#     if not root: return []
#     stack = [root]
#     res = []
#     while len(stack) > 0:
#         res.append(root.val) # 先记录栈内节点
#         if root.right is not None:
#             stack.append(root.right)
#         if root.left is not None:
#             stack.append(root.left)
#         root = stack.pop() # 再出栈
#     return res

## 中序非递归
def inorder(root): # 左根右
    """
    开始根节点入栈，循环执行如下操作：
    如果栈顶结点左孩子存在，则左孩子入栈；如果栈顶结点左孩子不存在，则出栈并输出栈顶结点，然后检查其右孩子是否存在，如果存在，则右孩子入栈。
    当栈空时算法结束。
    """
    if not root: return []
    stk, res = [], []
    cur = root
    while stk or cur:
        while cur:  # 找到最左侧子树
            stk.append(cur)
            cur = cur.left
        cur = stk.pop() # 先出栈
        res.append(cur.val) # 再记录节点
        cur = cur.right  # 当根弹出了，就进入右子树
    return res

## 后序非递归
def postorder(root): # 后序遍历
    """
    # 使用两个栈结构
    # 第一个栈进栈顺序：左节点->右节点->根节点
    # 第一个栈弹出顺序： 根节点->右节点->左节点(先序遍历栈弹出顺序：根->左->右)
    # 第二个栈存储为第一个栈的每个弹出依次进栈
    # 最后第二个栈依次出栈
    """
    if not root:return []
    stack = [root]
    stack2 = []
    res=[]
    while len(stack) > 0:
        node = stack.pop()
        stack2.append(node)
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
    while len(stack2) > 0:
        res.append(stack2.pop().val)
    return res


######  --------------------------------------------------------------------------------
def preorder_rec(root):
    res = []
    prehelper(root, res)
    return res
def prehelper(root,res):
    if not root: return
    res.append(root.val)
    prehelper(root.left, res)
    prehelper(root.right, res)

def inorder_rec(root):
    res = []
    inhelper(root, res)
    return res
def inhelper(root, res):
    if not root: return
    inhelper(root.left, res)
    res.append(root.val)
    inhelper(root.right, res)

def postorder_rec(root):
    if not root:return []
    res = []
    posthelper(root, res)
    return res
def posthelper(root,res):
    if not root: return
    posthelper(root.left,res)
    posthelper(root.right,res)
    res.append(root.val,res)
######  --------------------------------------------------------------------------------

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


