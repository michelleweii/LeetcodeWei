# -*- coding:utf-8 -*-
import functools
# https://blog.csdn.net/u012436149/article/details/79952975
class Solution:
    def helper(self,a,b):
        # a<b一定有ab<ba
        ab = int(a + b)
        ba = int(b + a)
        return 1 if ab > ba else -1

    def PrintMinNumber(self, numbers):
        numbers = [str(num) for num in numbers]
        numbers = sorted(numbers,key=functools.cmp_to_key(self.helper))
        print(numbers)
        return "".join(numbers)

if __name__ == '__main__':
    n = [32,3,321]
    print(Solution().PrintMinNumber(n))
    # 321323