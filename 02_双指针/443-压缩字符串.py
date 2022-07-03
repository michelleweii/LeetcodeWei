"""
middle 2022-01-04 同向双指针|滑动窗口
https://leetcode-cn.com/problems/string-compression/solution/pythonjava-san-zhi-zhen-by-himymben-cbrd/
利用滑动窗口法，左右指针起点都为原数组的首位。
实现步骤如下：
1、不断右移右指针，使窗口不断增大；
2、当窗口内出现一个不同的元素时，就可以将元素及其数量（等于左右指针之差）更新在数组中，然后让左指针指向右指针；
3、遍历到最后一个字符时也需要结算，因此将右指针的终点设为数组之外一格。当右指针移到终点时也要更新数组。
"""
class Solution(object):
    def compress(self, chars):
        # for x in '98':
        #     print(x) # 9, 8
        left = 0 # 标记当前字符
        right = 0 # 找这个字符有连续多少个
        write = 0 # 标记当前在数组中的读写位置
        n = len(chars)

        while left < n:
            right = left
            # 更新右边界
            while right<n and chars[right]==chars[left]:
                right += 1 # 出界了

            # 更新数组，先写当前字符left
            # print(write)
            chars[write] = chars[left]
            write += 1 # 更新写入位置

            # 更新计数，当个数大于 1 时才更新，大于1的才有重复次数要写进数组里
            if (right - left > 1):
                i2str = str(right-left)
                # print('i2str', i2str) # 2,2,3
                for x in i2str:
                    # print(i2str, x)
                    chars[write] = x
                    # print(write)
                    write += 1

            left = right # a更新完成后，直接定位到b

        # print(chars, left, right) # ['a', '2', 'b', '2', 'c', '3', 'c']
        # 修改完输入数组后 ，返回该数组的新长度。
        return write # 6

if __name__ == '__main__':
    # chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    chars = ["a","a", "b","b","c","c","c"]
    myResult = Solution()
    print(myResult.compress(chars))

