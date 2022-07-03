"""
二分 middle
2021-07-13
"""
class Solution:
    def findNumberIn2DArray(self, matrix, target):
        if not matrix or not matrix[0]:return False
        n = len(matrix)
        m = len(matrix[0])
        i = 0
        j = m-1
        while i<n and j>=0:
            if matrix[i][j]==target:return True
            elif matrix[i][j]>target:j-=1
            else: i+=1
        return False


if __name__ == '__main__':
    matrix = [
              [1,   4,  7, 11, 15],
              [2,   5,  8, 12, 19],
              [3,   6,  9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]
            ]
    # target = 5
    target = 20
    print(Solution().findNumberIn2DArray(matrix, target))
