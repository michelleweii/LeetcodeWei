class Solution:
    def InversePairs(self, data):
        # 采用归并排序的思想,时间复杂度为O（nlogn）
        global count
        count = 0
        def merge(array):
            global count
            if len(array) <= 1:
                return array
            k = len(array)//2
            left = merge(array[:k])
            right = merge(array[k:])
            l = 0
            r = 0
            result = []
            while l<len(left) and r<len(right):
                if left[l]<=right[r]:
                    result.append(left[l])
                    l+=1
                else:
                    result.append(right[r])
                    r += 1
                    count += len(left)+1
            result += left[l:]
            result += right[r:]
            return result
        merge(data)
        return count%1000000007


if __name__ == '__main__':
    data = [1,2,3,4,5,6,7,0]
    print(Solution().InversePairs(data))
