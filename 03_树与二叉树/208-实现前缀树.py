"""
middle 2022-04-19 前缀树(26叉树)
https://leetcode-cn.com/problems/implement-trie-prefix-tree/solution/trie-tree-de-shi-xian-gua-he-chu-xue-zhe-by-huwt/
[python]https://leetcode-cn.com/problems/implement-trie-prefix-tree/solution/fu-xue-ming-zhu-cong-er-cha-shu-shuo-qi-628gs/
"""
# 一次建树，多次查询
# tree = tree[a]的解释
# lookup的key是字符，value是另一个字典，每一个字典就相当于树的节点，tree=tree[a]相当于把指针移到下一个字符所在的节点
class Node:
    # isWord 表示从根节点到当前节点为止，该路径是否形成了一个有效的字符串。
    # children 是该节点的所有子节点。
    def __init__(self):
        self.isword=False
        self.children={} # {字符：Node}

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for w in word:
            # 直接通过 children['a'] 来获取当前节点的 'a' 子树
            cur = cur.children[w] # 移到下个字符的位置
        cur.isword = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        # 断了、没找到、找到了
        cur = self.root
        for w in word:
            cur = cur.children.get(w)
            if cur == None:
                return False
        return cur.isword

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for w in prefix:
            cur = cur.children.get(w)
            if cur == None:
                return False
        return True


# if __name__ == '__main__':
#     # Your Trie object will be instantiated and called as such:
#     obj = Trie()
#     obj.insert(word)
#     param_2 = obj.search(word)
#     param_3 = obj.startsWith(prefix)