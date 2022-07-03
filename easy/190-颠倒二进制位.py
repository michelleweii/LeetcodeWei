class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = bin(n).replace('0b', '') # 10进制转为2进制，类型是str
        # print(type(n)) # <class 'str'>
        # print(n)
        n = n[::-1]
        len_n = len(n)
        num = list(n)
        # print(num)
        while len_n<32:
            num.append('0')
            len_n+=1
        # print(len(num))
        str1 = "".join(num)
        return (int(str1, 2))  # 2进制转为10进制


def main():
    n = 43261596
    myResult = Solution()
    print(myResult.reverseBits(n))

if __name__ == '__main__':
    main()

