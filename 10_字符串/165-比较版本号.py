"""
middle 2022-05-24 模拟题
https://leetcode.cn/problems/compare-version-numbers/solution/gong-shui-san-xie-jian-dan-zi-fu-chuan-m-xsod/
[python]https://leetcode-cn.com/problems/compare-version-numbers/solution/python3-bu-xu-yao-bu-0de-cao-zuo-jian-dan-cu-bao-c/
思路：
用.隔开的数先求出来，放到数组里面，要将version最后没有用的0全部删掉；
1.0与1是同一种
将str转为数字的数组，可以直接比较
# 重要：print(int('01')) # 1
"""
# 字符串转为数字
def str2num(s: str):
    sum = 0
    for i in range(len(s)):
        sum = sum * 10 + int(s[i])
    return sum

class Solution:
    def compareVersion(self, version1, version2):
        ver1 = version1.split('.')
        ver2 = version2.split('.')
        print(ver1,ver2) # ['1', '01'] ['1', '001']
        while ver1 or ver2:
            # 将字符转成数字就需不要补0了
            # 如果其中一个list为空的话,就将它令为0进行比较
            x = int(ver1.pop(0)) if ver1 else 0
            y = int(ver2.pop(0)) if ver2 else 0
            print('x,y',x,y)
            # print(int('01')) # 1
            if x==y: continue
            if x>y:return 1
            if x<y:return -1
        return 0


if __name__ == '__main__':
    # version1 = "1.01"
    # version2 = "1.001"
    version1, version2 = "1.0","1.0.0"
    myResult = Solution()
    print(myResult.compareVersion(version1, version2))