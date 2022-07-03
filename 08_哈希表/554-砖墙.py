"""
思路：
将所有行压到一条线上，
每个缝隙看做一个点，要尽可能的穿过这些点，
出现次数最多的点，总的行数-出现次数最多的点=最少穿过砖块的数量
记录每个点出现多少次——>哈希的问题
"""
class Solution:
    def leastBricks(self, wall):
        hash_map = {}
        res = 0
        for blocks in wall:
            s = 0
            for i in range(len(blocks)-1): # 这里-1是因为不可以从边界处通过
                s += blocks[i]
                # s这个点每出现1次，就+1:
                hash_map[s] = hash_map.get(s,0)+1
                # print(hash_map)
                res = max(res, hash_map[s])
        return len(wall)-res




if __name__ == '__main__':
    wall = [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]] # 2
    # wall = [[1],[1],[1]] # 3
    res = Solution()
    print(res.leastBricks(wall))