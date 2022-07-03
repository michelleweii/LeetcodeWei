"""
hard 2021-12-09
哈希表——原地哈希（哈希函数为：f(nums[i]) = nums[i] - 1）
题目：给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。只能使用常数级别的额外空间
https://leetcode-cn.com/problems/first-missing-positive/solution/tong-pai-xu-python-dai-ma-by-liweiwei1419/
"""
# - 映射关系  nums[i]=i+1
# - nums[nums[i]-1]≠nums[i] 如何理解？
# - nums[i] ≠ i+1 （现在的位置不满足，i是下标）
# - nums[i]-1 是应该要放置的index，要放置的位置也不满足nums[ num[i]-1 ] ≠ nums[i]-1+1 (nums[i]-1整体是index i )
# - 位置交换，nums[nums[i]-1] = nums[i] 防止nums[i]改变，
# *`nums*[*nums*[i]-1], *nums*[i] = *nums*[i], *nums*[*nums*[i]-1] # 左边的会比右边的先赋值`
class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        # 1、先过一遍hash函数，将所有的item都放在该放的位置；
        # 2、再次遍历，返回不在位置上的item
        for i in range(n):
            # 先判断这个数字是不是索引，然后判断这个数字是不是放在了正确的地方
            # 缺失的数字~[1,n+1]
            # 注意这里是while
            # case [1,1] nums[nums[i]-1]!=nums[i]
            while nums[i]>0 and nums[i]<=n and nums[i]!=i+1 and nums[nums[i]-1]!=nums[i]:
                # 交换到正确的位置上
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1] # 左边的会比右边的先赋值
                """
                说明：Python 里可以这样写 nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1] ，
                但是这里赋值有先后顺序，
                写成 nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i], 就会出错。
                建议封装成单独的函数，避免出错。
                def __swap(self, nums, index1, index2):
                    nums[index1], nums[index2] = nums[index2], nums[index1]
                """

        for i in range(len(nums)):
            if i+1!=nums[i]:
                return i+1

        return n+1

"""
【详细题解】
/*
思路③、使用座位交换法
      根据思路② 可知，缺失的第一个整数是 [1, len + 1] 之间，
      那么我们可以遍历数组，然后将对应的数据填充到对应的位置上去，比如 1 就填充到 nums[0] 的位置， 2 就填充到 nums[1]
      如果填充过程中， nums[i] < 1 && nums[i] > len，那么直接舍弃
      填充完成，我们再遍历一次数组，如果对应的 nums[i] != i + 1，那么这个 i + 1 就是缺失的第一个正数

      比如 nums = [7, 8, 9, 10, 11], len = 5
      我们发现数组中的元素都无法进行填充，直接舍弃跳过，
      那么最终遍历数组的时候，我们发现 nums[0] != 0 + 1，即第一个缺失的是 1 

      比如 nums = [3, 1, 2], len = 3
      填充过后，我们发现最终数组变成了 [1, 2, 3]，每个元素都对应了自己的位置，那么第一个缺失的就是 len + 1 == 4
*/
class Solution {
    public int firstMissingPositive(int[] nums) {

        int len = nums.length;
        for(int i = 0; i < len; i++){
        /*
        只有在 nums[i] 是 [1, len] 之间的数，并且不在自己应该呆的位置， nums[i] != i + 1 ，
        并且 它应该呆的位置没有被同伴占有（即存在重复值占有）	nums[nums[i] - 1] != nums[i] 的时候才进行交换
        	
        为什么使用 while ？ 因为交换后，原本 i 位置的 nums[i] 已经交换到了别的地方，
        交换后到这里的新值不一定是适合这个位置的，因此需要重新进行判断交换
        如果使用 if，那么进行一次交换后，i 就会 +1 进入下一个循环，那么【交换过来的新值就没有去找到它该有的位置】
         比如 nums = [3, 4, -1, 1] 当 3 进行交换后， nums 变成 [-1，4，3，1]，
         此时 i == 0，如果使用 if ，那么会进入下一个循环， 这个 -1 就没有进行处理
        */
            while(nums[i] > 0 && nums[i] <= len && nums[i] != i + 1 && nums[nums[i] - 1] != nums[i]){
                swap(nums, nums[i] - 1, i);
            }
        }
        for(int i = 0; i < len; i++){
            if(nums[i] != i + 1){
                return i + 1;
            }
        }
        return len + 1;
    }

    private void swap(int[] nums, int i, int j){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
"""

if __name__ == '__main__':
    nums = [1,1] # 2
    # nums = [1,2,0]  # 3
    # 输入：nums = [3, 4, -1, 1]，输出：2
    # 输入：nums = [7, 8, 9, 11, 12]，输出：1
    print(Solution().firstMissingPositive(nums))