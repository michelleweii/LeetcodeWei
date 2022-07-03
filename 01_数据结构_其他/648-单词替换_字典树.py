"""
middle
字典树
"""
class Solution(object):
    def replaceWords(self, dict, sentence):
        myDict = set(dict)
        res = []  # res由字符串变为列表就不内存溢出了
        for word in sentence.split(): # 字符串按空格划分
            cur_word = ""
            for i,ch in enumerate(word):
                cur_word += ch
                if cur_word in myDict:
                    res.append(cur_word)
                    break
                if i==len(word)-1:
                    res.append(word)
        return " ".join(res)

if __name__ == "__main__":
    dict = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    myresult = Solution()
    print(myresult.replaceWords(dict, sentence))
