"""
hard 2021-10-14 bfs最短路径
20210825--20211014 一个无向图，需要用标记位，标记着节点是否走过，否则就会死循环！
（需要看该连接的无向图，好理解）
https://leetcode-cn.com/problems/word-ladder/solution/yan-du-you-xian-bian-li-shuang-xiang-yan-du-you-2/
# https://www.acwing.com/solution/content/221/
思路：
1、将单词看做点，如果两个单词可以相互转化，则在相应的点之间连一条无向边。那问题就变成了求从起点到终点的最短路。
2、枚举每个单词，然后枚举该单词的每一位字母，再枚举这一位的所有备选字母，然后再判断改变后的字符串是否存在，时间复杂度 O(26*wordlen)。
# A* 只有 终点第一次出队时才保证距离最短，其余点第一次出队不保证最小的原则
"""
# hit-hot-dot-dog-cog
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if len(wordList)==0 or endWord not in wordList:return 0
        # 先将 wordList 放到哈希表里，便于判断某个单词是否在 wordList 里
        word_set = set(wordList)
        # print("word_set", word_set) # {'dog', 'lot', 'log', 'cog', 'hot', 'dot'}
        # 这一步的目的：
        if beginWord in word_set: word_set.remove(beginWord)

        # 图的广度优先遍历，必须使用队列和表示是否访问过的 visited 哈希表
        queue = []
        queue.append(beginWord)
        visited = set(beginWord)

        word_len=len(beginWord)
        #开始广度优先遍历，包含起点，因此初始化的时候步数为 1
        step = 1
        while queue:
            current_size = len(queue) # 当前层有多少元素（竖着看）
            # 遍历当前层的所有单词（依次遍历当前队列中的单词
            for i in range(current_size):
                # 依次遍历当前队列中的单词
                word = queue.pop(0)
                word_list = list(word) # 换为list好替换每一位的字母
                #  开始替换每一位的字母
                for j in range(word_len):
                    origin_char = word_list[j]
                    # 26个字母开始替换
                    for k in range(26):
                        word_list[j] = chr(ord('a') + k)
                        next_word = ''.join(word_list) # 替换后的单词
                        if next_word in word_set:
                            # 如果 currentWord 能够修改 1 个字符与 endWord 相同，则返回 step + 1
                            if next_word==endWord:return step+1
                            if next_word not in visited:
                                queue.append(next_word) # hot添加到队列里，则下一层就可以从hot开始
                                visited.add(next_word) # 注意：添加到队列以后，必须马上标记为已经访问
                    word_list[j] = origin_char # 恢复原单词

            step += 1 # 在该层的所有单词都每一位枚举过了，则步数+1
        return 0

if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    # 5
    print(Solution().ladderLength(beginWord,endWord,wordList))