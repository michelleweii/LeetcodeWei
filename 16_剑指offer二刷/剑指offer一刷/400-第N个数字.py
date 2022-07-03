# 这里首先分析一下位数和规律
# 个位数：1-9，一共9个,共计9个数字
# 2位数：10-99,一共90个，共计180个数字
# 3位数：100-999，一共900个，共计270个数字
# 4位数，1000-9999，一共9000个，共计36000个数字
# 以此类推，
# 这样我们就可以首先定位到是哪个数，再找到其对应的数字
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        length = 1
        base = 1
        while(n>9*length*base):
            n -= 9*length*base
            length+=1
            base*=10
        # print(n) # 2
        # e.g. 二位数的第一个数字，是10
        curNum = (n-1)//length+base # 将数字还原，11(th)指向的是10,还原10；
        # print(curNum) # 10
        # 判断是11(th)指向的是数10的第几位，即指向的是0还是1；
        # 如果指向的是第0位，则是1；指向第1位，则是0；
        point = (n-1)%length # 指向第0位，还是第1位
        # print(point)
        digit = 0
        while (point<length):
            # print(i) # 0,1 (如果是2位数)
            digit =  curNum%10 # 个位数
            curNum //= 10 # 十位数
            point += 1
            # print(digit)
            # print(curNum)
        return digit
"""
n = int(input("Please input a number "))
#  li=[]
# for i in range(1,2**31):
#     str_i=str(i)
#     for j in range(len(str_i)):
#         li.append(str_i[j])
# print("The n-th digit is ", li(n-1))
for i in range(1, 10):
    if n - 9 * 10 ** (i - 1) * i <= 0:
        k = i
        break
    else:
        n -= 9 * 10 ** (i - 1) * i
base = 10 ** (k - 1)
str_n = str(base + (n - 1) // k)
print("The n-th digit is ", str_n[(n-1) % k])
"""


def main():
    n = 35867
    myResult = Solution()
    print(myResult.findNthDigit(n))

if __name__ == '__main__':
    main()