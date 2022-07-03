"""
middle 2022-03-05 模拟题
这道题务必要掌握空间复杂度O(1)的算法
2020秋招：陌陌一个256*256的二维数组，逆时针旋转90度。
https://leetcode-cn.com/problems/rotate-image/solution/48-xuan-zhuan-tu-xiang-chao-jian-ji-yi-d-nuau/
思路：
顺时针90度应该是左上/右下对角线翻转+左右翻转，或者右上/左下对角线翻转+上下翻转。
过程如下：
1）先以左上-右下对角条线为轴做翻转；
2）再以中心的竖线为轴做翻转；
"""
class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        # 1.先沿斜对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        # print(matrix)
        # 2.再沿垂直竖线翻转
#       for(int i = 0;i < n; i++)
#           for(int j = 0, k = n - 1; j < k ; j++, k--) //类似于双指针，由两端向中心靠齐
#               swap(matrix[i][j],matrix[i][k]);
        for i in range(n):
            for j in range(n//2):
                matrix[i][j],matrix[i][n-1-j] = matrix[i][n-1-j],matrix[i][j]

        return matrix

if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(Solution().rotate(matrix))