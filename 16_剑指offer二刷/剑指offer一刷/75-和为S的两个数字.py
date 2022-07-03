# -*- coding:utf-8 -*-
class Solution:
    # 如果有多对数字的和等于S，输出两个数的乘积最小的
    def FindNumbersWithSum(self, array, tsum):
        hashmap = {}
        rs = []
        minval = 2**31
        if not array:return rs
        if len(array)<=1: return rs
        for i in range(len(array)):
            # 在hashmap中
            if array[i] in hashmap:
                if array[hashmap[array[i]]]*array[i]<minval:
                    minval = array[hashmap[array[i]]]*array[i]
                    rs.append([array[hashmap[array[i]]],array[i]])
            # 不在hashmap中
            else:
                hashmap[tsum-array[i]] = i
        print(rs)
        if rs:return rs[-1]
        return rs
        # print(hashmap)
        # print(rs) # [20, 18, 14],为什么列表这样添加值就不会被覆盖呢？
        # return min(rs)



if __name__ == '__main__':
    a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    t = 21
    print(Solution().FindNumbersWithSum(a,t))