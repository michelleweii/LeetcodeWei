# 小结：
# 由于列表res中append的是str类型，所有不会每次都改变内容。
# 当浅复制的值是不可变对象（数值，8_about_string，元组）时和“等于赋值”的情况一样，
# 对象的id值与浅复制原来的值相同。

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1,n+1):
            # ans = []
            if (i%3==0 and i%5==0):
                res.append("FizzBuzz")
            elif i%5==0:
                res.append("Buzz")
            elif i%3==0:
                res.append("Fizz")
            else:
                res.append(str(i))
            # res.append(ans[:])
        return res


if __name__ == '__main__':
    n = 15
    print(Solution().fizzBuzz(n))
    # ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz',
    # 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']