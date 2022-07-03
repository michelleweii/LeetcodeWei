"""
middle 2021-01-17 dfs-回溯
与LC89相似，回溯2个状态。（求叶子节点，不需要start_index）
0向下一层时，可以走0，可以走1
a向下一层时，可以走a，可以走A

# 通过dfs遍历输入字符，对于dfs中的每一层（即操作某个字符）都有可能有两种选择：
# 1)不改变当前字符; 2)当期字符若为字母，则改变大小写状态
# 方法一：回溯
# 参数是s和指向s的下标cur_index数据, dfs(s, cur_index)
# 【回溯2次】https://leetcode-cn.com/problems/letter-case-permutation/solution/python-dfs-by-qinyu-c-2ln5/

# 参数是path和idx下标, dfs(idx + 1, path + [ss[i]])
# https://leetcode-cn.com/problems/letter-case-permutation/solution/dfs-shi-jian-chao-97-by-wongdaweeee-qifq/

# dfs一般传参都是(s,u)，字符串s和指向s的下标u。
"""
class Solution(object):
    def letterCasePermutation(self, s):
        if s.isdigit(): return [s]  # 如果是纯数字则直接return
        self.res, self.path = [], []
        self.backtrace(s, 0)
        return self.res

    def backtrace(self, s, idx): # idx当前s的下标
        if len(self.path) == len(s):
            self.res.append(''.join(self.path[:]))
            return # 没有return会越界

        ch = s[idx]
        if ch.isdigit():
            self.path.append(ch)
            self.backtrace(s, idx + 1)
            self.path.pop()
        else:
            self.path.append(ch.lower()) # 手动回溯选择a
            self.backtrace(s, idx + 1)
            self.path.pop()

            self.path.append(ch.upper()) # 手动回溯选择A
            self.backtrace(s, idx + 1)
            self.path.pop()

    ########  ##############
    # /**
    #  * @param {string} s
    #  * @return {string[]}
    #  */
    # var letterCasePermutation = function (s) {
    #   let res = [];
    #
    #   let dfs = function (i, str) {
    #     while (!isNaN(s[i])) {
    #       str += s[i++];
    #     }
    #
    #     if (i == s.length) {
    #       res.push(str);
    #       return;
    #     }
    #     dfs(i + 1, str + s[i].toLowerCase());
    #     dfs(i + 1, str + s[i].toUpperCase());
    #   };
    #
    #   dfs(0, "");
    #   return res;
    # };
    #

if __name__ == '__main__':
    S = "1ab2"
    # 第一个字符串的排列之一是第二个字符串的子串
    print(Solution().letterCasePermutation(S))
    # print(Solution().letterCasePermutation_dfs(S))
    # a = '12'
    # print(a.isdigit()) # True