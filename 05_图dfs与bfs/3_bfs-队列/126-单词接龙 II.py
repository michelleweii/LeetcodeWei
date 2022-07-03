"""
hard 2021-12-09 最短路径
找出并返回所有从 beginWord 到 endWord 的 最短转换序列, 注意是“所有”&“最短路径”->BFS
基础题127（求最短转化序列的长度）
1、BFS找到所有最短路径(建图)+2、DFS找到所有解
https://leetcode-cn.com/problems/word-ladder-ii/solution/yan-du-you-xian-bian-li-shuang-xiang-yan-du-you--2/
https://leetcode-cn.com/problems/word-ladder-ii/solution/bfsdfs-by-snow-77-l8dh/
真是要命做了3天
"""
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList): #: List[str]) -> List[List[str]]:
        res = []
        if len(wordList) == 0 or endWord not in wordList: return res
        wordset = set(wordList)
        # 因为从 beginWord 开始扩展，因此 dict 里一定不可以有 beginWord
        if beginWord in wordset: wordset.remove(beginWord)
        # bfs
        # 图的广度优先遍历，必须使用队列和表示是否访问过的 visited 哈希表
        # // 第 1 步：广度优先遍历构建图
        # // 为了避免记录不需要的边，我们需要记录扩展出的单词是在第几次扩展的时候得到的，
        # key：单词，value：在广度优先遍历的第几层
        # // visited 记录了已经访问过的 word 集合，同时记录了在第几层访问到
        visited = {}
        visited[beginWord] = 0
        # // 记录了单词是从哪些单词扩展而来，key：单词，value：单词列表，这些单词可以变换到 key ，
        # 它们是一对多关系，dfs 的时候会用到
        froms = {}
        found = self.bfs(beginWord,endWord,wordset,visited,froms)
        print("froms", froms)
        # // 第 2 步：深度优先遍历找到所有解，从 endWord 恢复到 beginWord ，所以每次尝试操作 path 列表的头部
        if found:
            path = []
            path.append(endWord)
            self.dfs(froms, path, beginWord, endWord, res)

        return res

    # 建图
    def bfs(self, beginWord, endWord, wordset, visited, froms):
        word_len = len(beginWord)
        step = 0
        found = False
        # 开始bfs
        queue = []
        queue.append(beginWord)

        while queue:
            step += 1
            cur_level_size = len(queue)
            # 1、遍历当前层待替换单词
            for i in range(cur_level_size):
                # 2、依次遍历当前level队列中的单词[]
                cur_word = queue.pop(0) # 解
                wordlist = list(cur_word)
                # 2、遍历单词的每一个字符
                for j in range(word_len):
                    ori_ch = wordlist[j]
                    # 3、遍历26位字母
                    for k in range(26):
                        wordlist[j] = chr(ord('a') + k)  # for (char ch = 'a'; ch <= 'z'; ch++) {
                        next_word = ''.join(wordlist)
                        # // 注意：这几行代码的逻辑先后顺序
                        if next_word in visited and visited[next_word] == step:
                            if froms.get(next_word, -1)==-1:
                                froms[next_word] = []
                            else:
                                froms[next_word] = froms.get(next_word).append(cur_word)
                            # froms[next_word] = froms.get(next_word,[]).append(cur_word)
                        if next_word not in wordset:continue
                        # wordset 和 visited 承担了已经访问的功能
                        wordset.remove(next_word)
                        queue.append(next_word)
                        # // 维护 froms、visited、found 的定义
                        froms[next_word] = froms.get(next_word,[]).append(cur_word) #??
                        visited[next_word] = step # next_word在第几层
                        if next_word==endWord:
                            # // 注意：由于有多条路径到达 endWord 找到以后不能立即退出，只需要设置 found = true 即可
                            found = True
                    wordlist[j] = ori_ch
            if found:
                break
        return found

    def dfs(self, froms, path, beginWord, cur, res):
        if cur==beginWord:
            res.append(path)
            return


        for _ in froms[cur]:
            pre_word = froms[endWord]
            print('pre', pre_word)
            # cur当前单词可以由那些词 递推 得到(当前词的前驱)
            # path.append(pre_word)
            # print(path)
            self.dfs(froms,path,beginWord,pre_word,res)
            # path.pop()


    # def dfs(self, ):
if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    # [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
    print(Solution().findLadders(beginWord, endWord, wordList))