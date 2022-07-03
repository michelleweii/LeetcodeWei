class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        strs = [ord(ch)-97 for ch in letters]
        # print(strs) # [2, 5, 9]
        for ch in strs:
            if ord(target)-97 < ch:
                return chr(ch+97)
        else:
            return letters[0]


def main():
    letters = ["a", "b"]
    target = "z"
    myResult = Solution()
    print(myResult.nextGreatestLetter(letters, target))

if __name__ == '__main__':
    main()