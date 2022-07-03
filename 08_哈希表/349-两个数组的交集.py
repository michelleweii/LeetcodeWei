from collections import Counter
class Solution(object):
    def intersection(self, nums1, nums2):
        hash_map = Counter(nums1)
        # print(hash_map) # Counter({1: 2, 2: 2})
        res = []
        for x in nums2:
            if x in hash_map:
                res.append(x)
                if hash_map[x]:
                    hash_map.pop(x)
        return res

if __name__ == "__main__":
    a = [4,9,5]
    b = [9,4,9,8,4]
    myresult = Solution()
    print(myresult.intersection(a,b))