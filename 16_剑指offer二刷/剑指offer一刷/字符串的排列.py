# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        if len(ss) <= 0:
            return []
        res = list()
        self.perm(ss, res, '')
        uniq = list(set(res))
        return sorted(uniq)

    # 从子串中挑一个字符，插入新的字符
    def perm(self, ss, res, path):
        if ss == '':
            res.append(path)
        else:
            for i in range(len(ss)):
                self.perm(ss[:i]+ss[i+1:], res, path+ss[i])


if __name__ == '__main__':
    ss = 'abc'
    ans = Solution()
    print(ans.Permutation(ss))
