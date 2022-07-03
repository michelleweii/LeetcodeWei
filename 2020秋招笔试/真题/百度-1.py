# 网易也考了
# 有这样一个数组A，大小为n，相邻元素差的绝对值都是1。
# 如：A={4,5,6,5,6,7,8,9,10,9}。现在，给定A和目标整数t，
# 请找到t在A中的位置。除了依次遍历，还有更好的方法么？

# 分析：数组第一个数为array[0], 要找的数为y，设diff = abs(y - array[0])。由于每个相邻的数字之差的绝对值为1。
# 故第diff个位置之前的数肯定都比y小。因此直接定位到array[diff]，重新计算diff，diff = abs(y – array[t])，
# 再重复上述步骤即可。这种算法主要利用了当前位置的数与查找数的差来实现跨越式搜索。
# 算法效率要比遍历数组的算法要高一些，并且易于实现。

# 有问题，如果改成3，则就越过7了。

def findT(nums,t):
    n = len(nums)
    next_index = abs(t-nums[0])
    while next_index<n:
        if nums[next_index]==t:
            return next_index
        next_index += abs(t-nums[next_index])
    return -1


def find(array, target):
    # write code here
    length = len(array)
    abs_length = abs(target - array[0])
    if length == 0 or abs_length >= length:
        return None

    i = 0
    while i < length:
        if array[i] == target:
            return i
        else:
            res = abs(target - array[i])
            i += res
            continue
    return None



if __name__ == '__main__':
    nums = [4,5,6,3,6,7,8,9,10,9]
    t = 7
    n = len(nums)
    print(find(nums,t))
