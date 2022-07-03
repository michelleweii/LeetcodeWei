class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        hash_map = {}
        res = 0
        for a in nums1:
            for b in nums2:
                hash_map[a+b] = hash_map.get(a + b,0) + 1
        for c in nums3:
            for d in nums4:
                res += hash_map.get(-c-d,0)
        return res


if __name__ == '__main__':
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    res = Solution()
    print(res.fourSumCount(A, B, C, D))