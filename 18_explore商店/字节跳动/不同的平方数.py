"""
https://www.csdn.net/tags/MtTaEgysMTAyODM2LWJsb2cO0O0O.html
字节跳动面试题.有序数组每个数平方后，不同数字的个数？O(n)
给你一个有序整数数组，数组中的数可以是正数、负数、零，请实现一个函数，
这个函数返回一个整数：返回这个数组所有数的平方值中有多少种不同的取值。举例：
nums = {-1,1,1,1},
那么你应该返回的是：1。因为这个数组所有数的平方取值都是1，只有一种取值
nums = {-1,0,1,2,3}
你应该返回4，因为nums数组所有元素的平方值一共4种取值：1,0,4,9
"""
# 思路：使用双指针，从两边向中间扫描。将绝对值大的数字删掉，计数即可，
# 并记录刚才删除的数值的绝对值，以免出现多次相同的数据，重复计数的问题。
def func(nums):
    n=len(nums)
    i,j=0,n-1
    count=0
    pre=float('inf')
    while i<=j:
        if abs(nums[i])>abs(nums[j]):
            if pre!=abs(nums[i]):
                count+=1
                pre=abs(nums[i])
            i+=1
        else:
            if pre!=abs(nums[j]):
                count+=1
                pre=abs(nums[j])
            j-=1
    return count

if __name__ == '__main__':
    # nums=[-1,1,1,1] # 升序
    nums= [-5,-3,-1,1,1,2]
    print(func(nums))

