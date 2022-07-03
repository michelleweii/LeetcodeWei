"""
easy 2021-08-25 dfs模板题
https://www.acwing.com/solution/content/545/
"""
class Solution:
    # 把这个方法就定义为dfs
    def floodFill(self, image, sr, sc, newColor):
        if not image or not image[0]:return image
        n = len(image) # n行
        m = len(image[0]) # m列
        # 定义递归出口
        if image[sr][sc] == newColor:
            return image
        # 定义枚举
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]

        oldColor = image[sr][sc]
        image[sr][sc] = newColor

        # 4个方向开始遍历
        for i in range(4):
            a = sr+dx[i]
            b = sc+dy[i]
            if a>=0 and a<n and b>=0 and b<m and image[a][b]==oldColor:
                self.floodFill(image,a,b,newColor)
        return image

if __name__ == '__main__':
    # 因为它不是在上下左右四个方向上与初始点相连的像素点。
    # [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    image = [[1, 1, 1],
             [1, 1, 0],
             [1, 0, 1]]
    sr = 1
    sc = 1
    newColor = 2
    print(Solution().floodFill(image,sr,sc,newColor))