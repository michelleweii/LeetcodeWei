"""
middle 2022-03-04 数学概率
https://leetcode-cn.com/problems/implement-rand10-using-rand7/solution/xiang-xi-si-lu-ji-you-hua-si-lu-fen-xi-zhu-xing-ji/
https://www.bilibili.com/video/BV1VV411b7ge?from=search&seid=9169511433626257608&spm_id_from=333.337.0.0
# 1. 首先通过rand10()拿到rand7()，证明出“从 rand10 到 rand7 它是等概率的”。
# 2. 题目要求从rand7()得到rand10(), 只要将rand7成倍扩大，扩大到含有[1,10]的数字。
# 3. 如何扩大，又要满足等概率呢？ (randX() - 1)*Y + randY() 可以等概率的生成[1, X * Y]范围的随机数
"""

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

# 说明：
#  (randX() - 1)*Y + randY() 可以等概率的生成[1, X * Y]范围的随机数
# 首先考虑使用rand10()产生rand7()的逻辑，可以证明得到“从 rand10 到 rand7 它是等概率的”；
# 同理，用rand7产生rand10，只要将数据成倍扩大，>10的部分，不断调用，直到它落在[1,10]

class Solution:
    def rand10(self):
        # rand7()-1 产生[0,1,2,3,4,5,6]， 减1是因为"每个rand7()它能生成数的范围是 1～7，rand 两次，那么数的范围就变为 2～14，
        # 哦，你可能发现没有 1 了，想要再减去个 1 来弥补"
        # *7为了成倍扩大，(rand7()−1)∗7， A为[0，7，14，21，28，35，42]
        # rand7() 得到的集合B为[1,2,3,4,5,6,7]
        # 所以(rand7() - 1)*7 + rand7()，可以生成[0,49]的随机数。

        # 首先得到一个数
        num = (rand7()-1)*7+rand7() # 生成[1,49]的随机数
        while num>10:
            num = (rand7()-1)*7+rand7()
        return num

        # 优化
        # 1.随机初始化一个数
        num=(rand7()-1)*rand7()+rand7()  # 1-49
        while num>40:
            num=(rand7()-1)*rand7()+rand7()
        return 1+num%10

    # # 如果想要通过rand10()拿到rand7(),
    # # 给了rand10()去映射rand7()。
    # num = rand10()
    # while True:
    # 	if num<=7:return num
    # 	else:
    # 		# 对剩余3个数字，不断的再做映射
    # 		num = rand10()
    #
"""
“从 rand10 到 rand7 它是等概率的”， 证明如下：
如果给了rand10()如何产生rand7()?
rand7()
1,2,3,4,5,6,7
rand10()
1,2,3,4,5,6,7,8,9,10

如果调用rand10()产生的值落在[1,7]，那么可以直接返回rand7()
如果落在了[8,9,10]呢？
[8,10]的话，就重新映射。重新映射能够满足是等概率事件吗？
结论：落在[1,7]，p=1/10。
为什么命中的概率是1/10？
个人理解：因为可以选择的数字是7/10,选择特定的数字的概率是1/7,两者相乘1/10。
映射到[1,7]的概率是7/10，但是我们只要[1,7]中的一个数字，这是一个独立事件。p=1/7
所以最后的概率是 7/10 * 1/7 = 1/10。

[8,10]重新映射，第一次没有拿到这3个数字的概率是3/10。
落在[1,7]的概率是1/10
那么下一轮落在[1,7]的概率是3/10*1/10。

如果又没有拿到，下次的概率
p = (3/10)*(3/10)*(1/10)

如果一直继续下去，p=(3/10)^n*(1/10) = (10/7)*(1/10) = 1/7（中间用到了等比公式求和）
证明得到“从 rand10 到 rand7 它是等概率的”。
"""
if __name__ == '__main__':
    pass
