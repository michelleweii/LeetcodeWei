"""
middle 2022-03-02 二分
[两次二分](https://leetcode-cn.com/problems/search-a-2d-matrix/solution/gong-shui-san-xie-yi-ti-shuang-jie-er-fe-l0pq/)
# [mid//m][mid%m] 求当前一维数组中元素mid的index,对应在二维数组中的index
题目要求：
1、每行中的整数从左到右按升序排列。
2、每行的第一个整数大于前一行的最后一个整数。==> 由于二维矩阵固定列的「从上到下」或者固定行的「从左到右」都是升序的。
解题思路：
第一次二分：从第 0 列中的「所有行」开始找，找到合适的行 row
第二次二分：从 row 中「所有列」开始找，找到合适的列 col
"""
class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]: return False
        m, n = len(matrix), len(matrix[0])

        # 第一次二分，确定哪一行
        l,r=0,m-1
        while l<r:
            mid=(l+r+1)//2
            if matrix[mid][0]>target:  # 这里出了点错
                r = mid-1
            else:
                l=mid

        row = r
        print(matrix[row])
        print("定位在 {} 行".format(row))
        if matrix[row][0]==target:return True
        if matrix[row][0]>target:return False

        # 第二次二分，确定哪一列
        l,r=0,n-1
        while l<r:
            mid=(l+r+1)//2
            if matrix[row][mid]>target:
                r=mid-1
            else:
                l=mid

        return matrix[row][l]==target


# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         m, n = len(matrix), len(matrix[0])
#         l, r = 0, m * n - 1
#         while l <= r:
#             mid = (l + r) >> 1
#             x, y = mid // n , mid % n
#             if matrix[x][y] > target:
#                 r = mid - 1
#             elif matrix[x][y] < target:
#                 l = mid + 1
#             else:
#                 return True
#         return False

if __name__ == '__main__':
    # matrix = [[1, 3, 5, 7],
    #           [10, 11, 16, 20],
    #           [23, 30, 34, 60]]
    # matrix = [[1,1]]
    # target = 3

    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    target=7
    solu = Solution()
    print(solu.searchMatrix(matrix, target))