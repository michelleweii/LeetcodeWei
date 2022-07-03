"""
middle 2021-12-22 贪心（pdd1面）
【不用拘泥于每次究竟跳几步，而是看覆盖范围，覆盖范围内一定是可以跳过来的，不用管是怎么跳的】
（看链接里的图更好理解）https://programmercarl.com/0055.%E8%B7%B3%E8%B7%83%E6%B8%B8%E6%88%8F.html
分析：
当前位置元素如果是3，我究竟是跳一步呢，还是两步呢，还是三步呢，究竟跳几步才是最优呢？
每次取最大的跳跃步数，这个就是可以跳跃的覆盖范围。
贪心算法局部最优解：每次取最大跳跃步数（取最大覆盖范围），整体最优解：最后得到整体最大覆盖范围，看是否能到终点。
"""
class Solution(object):
    """
    1、i每次移动只能在cover的范围内移动，每移动一个元素，cover得到该元素数值（新的覆盖范围）的补充，让 i 继续移动下去。
    2、而cover每次只取 max(该元素数值补充后的范围, cover本身范围)。
    3、如果cover >= 了终点下标，直接return true就可以了。
    """
    def canJump(self, nums):
        cover = 0
        if len(nums) <= 1:return True # 只有一个元素，就是能达到
        i = 0  # python不支持动态修改for循环中变量,使用while循环代替
        while i<= cover: # cover一直在变化
            cover = max(i+nums[i], cover) # i+nums[i] 当前位置最远能去的地方
            if cover>=len(nums)-1: return True
            i += 1
        return False

if __name__ == '__main__':
    nums = [2,3,1,1,4]
    print(Solution().canJump(nums))