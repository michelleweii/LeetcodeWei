"""
middle 2022-05-21 模拟题
1~9     9位
10~99   180位=90*2
100~999 2700位=900*3
1、首先确定n落于哪个区间
2、确定哪个数字
3、确定是数字的哪一位？
举例490，因为>180and<2700，所以落入100~999这个区间；该区间
490-9-180=301, 301/3=100,所以n是100~999中第100个数字。则起始位置是100，所以100+100=200,所以数字是200
因为301%3=1, 所以落在第一位上，那么是200的第一位，ans=2
https://leetcode.cn/problems/nth-digit/solution/zi-jie-ti-ku-400-zhong-deng-di-nge-shu-zi-1shua-by/
https://www.bilibili.com/video/BV13i4y1P7pX?spm_id_from=333.337.search-card.all.click
"""
class Solution:
    def findNthDigit(self, n: int) -> int:
        if n<10:return n
        digit=1 # 数位（个位/十位/百位/...，就是1/2/3/...）
        start=1 # 属于该数位的所有数的起始点数（个位是1，十位是10，百位是100）
        index_count=digit*9*start # 该数位的数一共的索引个数（不是数字个数）

        while n>index_count:
            n-=index_count # 490-9-180=301 # n是第n个ch
            digit+=1
            start*=10
            index_count=digit*9*start
        # print(n,digit,start,index_count) # 301 3 100 2700

#         // 上面的循环结束后：
#         // digit 等于原始的 n 所属的数位；start 等于原始的 n 所属数位的数的起始点
#         // index_count 等于原始的 n 所属数位的索引总个数（不重要了，下面不用）
#         // n 等于在当前数位里的第 n - 1 个索引（索引从 0 开始算起）

        # 找是第几个数
        # n-1是因为，第1个数字的下标是0.
        # start是digit位的第一个数。while循环之后，n的值是当前digit位从start开始的第n-1个索引。
        num=start+(n-1)//digit # 算出原始的 n 到底对应那个数字（所指向的真实数字）
        offset=(n-1)%digit # 余数就是原始的 n 是这个数字中的第几位
        # print(num,offset)
        return int(str(num)[offset])


if __name__ == '__main__':
    n=490
    print(Solution().findNthDigit(n))