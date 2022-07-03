class Solution:
    def getLeastNumbers(self, arr, k):
        if k>= len(arr):return arr
        return self.partition(arr, 0, len(arr)-1, k)

    def partition(self, arr, left, right, k):
        if left>=right:return
        pivot = arr[left]
        l,r = left,right
        while l<r:
            while l<r and arr[r]>=pivot:r-=1
            arr[l] = arr[r]
            while l<r and arr[l]<=pivot:l+=1
            arr[r] = arr[l]
        arr[l] = pivot
        # return l
        if k<l: self.partition(arr, left, l-1, len(arr)-k) # #把k换成len(arr)-k
        if k>l: self.partition(arr, l+1, right, len(arr)-k)
        # print(len(arr)-k)
        return arr[len(arr)-k:]



if __name__ == '__main__':
    arr = [3, 2, 1]
    k = 2
    # arr = [0, 1, 2, 1]
    # k = 1
    print(Solution().getLeastNumbers(arr, k))