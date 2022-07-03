from collections import Counter
class Solution:
    def intersect(self, nums1, nums2):
        hash_map = Counter(nums1)
        # print(hash_map) # Counter({4: 1, 9: 1, 5: 1})
        res = []
        for x in nums2:
            if x in hash_map and hash_map[x]:
                res.append(x)
                hash_map[x]-=1
        return res


if __name__ == '__main__':
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    myresult = Solution()
    print(myresult.intersect(nums1,nums2))