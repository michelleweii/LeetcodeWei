class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        B = set()
        for string in A:
            # print(string)
            C = list(string)
            a = C[::2] # abc->ac
            # print(a)
            # print(''.join((sorted(a))))
            b = C[1::2]
            # print(b) # abc->b
            # {('b', 'b'), ('b', 'a'), ('a', 'a'), ('a', 'b')}
            B.add((''.join(sorted(a)), ''.join(sorted(b))))  # 多加了元组
            # B.add((''.join(sorted(a)))) # {'a', 'b'}
        # print(B)
        return len(B)



if __name__ == "__main__":
    A = ["aa","bb","ab","ba"]
    myResult = Solution()
    print(myResult.numSpecialEquivGroups(A))


"""
fruits = {"apple", "banana", "cherry"}
fruits.add("orange") 
print(fruits) # {'apple', 'banana', 'orange', 'cherry'}


fruits = {"apple", "banana", "cherry"}
fruits.add("apple")
print(fruits) # {'apple', 'banana', 'cherry'}
"""