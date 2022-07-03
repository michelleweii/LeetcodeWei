"""
middle 2022-01-04 同向双指针
https://leetcode-cn.com/problems/maximize-distance-to-closest-person/solution/dao-zui-jin-de-ren-de-zui-da-ju-chi-by-leetcode/
思路：遍历所有座位 seats，找出每个空位左边最近的人和右边最近的人，更新当前空位到最近的人的距离。
使用 prev 记录 i 最左边第一个有人的位置，future 记录 i 最右边第一个有人的位置。
座位 i 到最近的人的距离为 min(i - prev, future - i)。
另外有一种特殊情况，如果座位 i 左边没有人，则认为到左边第一个人的距离是无限大，右边同理。
"""
class Solution(object):
    # 对每个空位置记录左右有人的位置，记录每个空位置的最近距离
    # 更新全局ans
    def maxDistToClosest(self, seats):
        # 左右指针指的是有人的位置。
        # 遍历的是无人的位置。
        N = len(seats)
        prev = -1
        future = 0
        ans = 0
        for i in range(N):
            if seats[i]==1:
                prev = i # 左边第一个有人的位置
            # 只更新空位的值
            else:
                while future<N and seats[future]==0 or future<i:
                    future+=1 # 记录 i 最右边第一个有人的位置
                left = N if prev==-1 else i-prev
                right = N if future==N else future-i
                ans = max(ans, min(left, right))
        return ans

        # people = (i for i, seat in enumerate(seats) if seat)
        # # print(people) # <generator object Solution.maxDistToClosest.<locals>.<genexpr> at 0x000001C8E3F2AC48>
        # prev, future = None, next(people)
        # ans = 0
        # for i, seat in enumerate(seats):
        #     if seat: # 如果该位置有人
        #         prev = i
        #     # 找该空位下一个有人的位置
        #     else:
        #         while future is not None and future < i:
        #             future = next(people, None)
        #
        #         left = float('inf') if prev is None else i - prev
        #         right = float('inf') if future is None else future - i
        #         ans = max(ans, min(left, right))
        #
        # return ans

if __name__ == '__main__':
    # seats = [1,0,0,0]#
    seats = [1,1,0,0,0,1,0]
    # seats = [1,1,0,0,0]
    myansult = Solution()
    print(myansult.maxDistToClosest(seats))
