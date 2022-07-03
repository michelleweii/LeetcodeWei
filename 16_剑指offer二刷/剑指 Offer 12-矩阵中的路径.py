"""
2_dfs-递归 middle
2_dfs-递归: 存不存在某一个值
2021-07-13
"""
class Solution:
    def exist(self, board, word):
        if not board or not board[0]:return False
        if not word: return False
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(word, board, 0, i, j):return True
        return False

    def dfs(self, word, board, u, x, y):
        """
        :param word: 原始target单词
        :param board: 原始matrix数组
        :param u: 定位target
        :param i: 定位matrix
        :param j: 定位matrix
        :return:
        """
        if board[x][y] != word[u]: return False
        if len(word)-1 == u: return True
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        tmp = board[x][y]
        board[x][y] = '*'
        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]
            if a>=0 and a<len(board) and b>=0 and b<len(board[0]):
                if self.dfs(word, board, u+1, a, b):return True
        board[x][y] = tmp
        return False

if __name__ == '__main__':
    board = [["a", "b"], ["c", "d"]]
    word = "abcd"
    print(Solution().exist(board, word))