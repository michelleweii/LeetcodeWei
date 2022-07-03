"""
easy 2022-02-21 位运算
https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/solution/mian-shi-ti-65-bu-yong-jia-jian-cheng-chu-zuo-ji-7/
最清晰的题解：https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/solution/jin-zhi-tao-wa-ru-he-yong-wei-yun-suan-wan-cheng-j/https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/solution/jin-zhi-tao-wa-ru-he-yong-wei-yun-suan-wan-cheng-j/
python 位运算 https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/solution/pythonjie-fa-xiang-xi-jie-du-wei-yun-sua-jrk8/
为什么无进位代表加法结束？因为2+7没有进位就计算完了。但是10+2有进位，说明还能计算加法。
"""
# Python 负数的存储：
# Python，Java 等语言中的数字都是以 补码 形式存储的。但 Python 没有 int , long 等不同长度变量，即在编程时无变量位数的概念。
# 获取负数的补码： 需要将数字与十六进制数 0xffffffff 相与。可理解为舍去此数字 32 位以上的数字（将 32 位以上都变为 0 ），从无限长度变为一个 32 位整数。
# 返回前数字还原： 若补码 a 为负数（ 0x7fffffff 是最大的正数的补码 ），需执行 ~(a ^ x) 操作，将补码还原至 Python 的存储格式。
# a ^ x 运算将 1 至 32 位按位取反； ~ 运算是将整个数字取反；因此， ~(a ^ x) 是将 32 位以上的位取反，1 至 32 位不变。
#
class Solution:
    # public int add(int a, int b) {
    # while (b!=0){
    #   int tempSum = a^b;
    #   int carrySum = (a&b)<<1;
    #   a = tempSum;
    #   b = carrySum;
    # }
    # return a;
    def add(self, a: int, b: int) -> int:
        while b: #当进位为 0 时跳出
            c = (a&b)<<1 # 进位
            a = a^b # a=非进位和
            b = c # b进位
        return a



if __name__ == '__main__':
    a = 1
    b = 1
    print(Solution().add(a, b))