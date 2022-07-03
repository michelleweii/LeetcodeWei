"""
middle 2021-01-19 DFS四周扩散模板题（回溯）
向每个方向去尝试。
https://leetcode-cn.com/problems/word-search/solution/hui-su-suan-fa-zui-tong-su-yi-dong-de-ji-h2ny/
# 将访问过的元素重置为*， 从搜索过的位置继续搜索下一层时，需要对当前位置进行标识，表示已经搜索。
"""
class Solution:
    # 往上下左右四个方向进行DFS。
    # 需要注意的就是访问一个字母后visited标识1，
    # 当DFS调用返回后，如果还没有找完，应该让visited置0，并返回false
    def exist(self, board, word):
        if len(word) == 0:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, 0, i, j): 
                    # i,j是一开始遍历的位置
                    return True
        return False

    def dfs(self, board, word, u, x, y):
        # 如果不是要找的元素
        if board[x][y] != word[u]: return False

        # word遍历到结束
        if u==len(word)-1:return True

        m, n = len(board), len(board[0])
        # visited = [[False for _ in range(n)] for _ in range(m)]

        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        tmp = board[x][y]
        board[x][y] = '*'

        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]

            if a>=0 and a<m and b>=0 and b<n:
                if self.dfs(board, word, u+1, a, b):
                    return True

        board[x][y] = tmp
        return False


    def dfs2(self, board, word, index, x, y):
        # 递归的出口
        if not board or index == len(word):
            return True
        # 是否越界
        if x < 0 or x == len(board) or y < 0 or y == len(board[0]):
            return False
        # 不是要找的元素
        if board[x][y] != word[index]:
            return False
        # 这几句什么意思？？ 
        source = board[x][y]
        board[x][y] = '*' # 表示此位置已经访问过，‘1’也可以，访问过的元素不再访问
        # 递归变成了四个方向的递归判断 
        exist = self.dfs(board, word, index + 1, x, y + 1) or \
                self.dfs(board, word, index + 1, x, y - 1) or \
                self.dfs(board, word, index + 1, x + 1, y) or \
                self.dfs(board, word, index + 1, x - 1, y)
        board[x][y] = source  
        return exist

"""
这实际上还是一个回溯法解决的问题。例如，对于word = 'ABCCED'，
我们从第一个元素开始，首先匹配到A，然后向后面寻找。
我们规定好寻找的顺序为：⬆️,➡️,⬇️,⬅️。我们接着找B，上面越界，右边找到了。
我们接着找C，上面越界，右边找到了。我们接着找C，上面越界了，右边不对，下面找到了。
接着找E，我们发现上面访问过，不再访问。接着向右查找，发现不匹配，接着向下查找，
发现越界了，接着想做查找，OK!我们所有元素匹配成功。
"""

if __name__ == "__main__":
    board =[['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
    word = "ABCCED"
    res = Solution()
    print(res.exist(board,word))
        