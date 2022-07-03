class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        listS = list(S)
        # print(listS)
        listT = list(T)
        listS.reverse()
        listT.reverse()
        # print(listS)
        # print(listT)
        tmpS = []
        tmpT = []
        count_s = 0
        count_t = 0
        for i,val_i in enumerate(listS):
            if i == len(listS) and len(tmpS)==0:
                return tmpS
            if val_i=='#':
                count_s += 1
            else:
                if count_s != 0:
                    count_s -= 1
                    continue
                else:
                    tmpS.append(val_i)

        # print(tmpS)

        for j,val_j in enumerate(listT):
            if j == len(listT) and len(tmpT)==0:
                return tmpT
            if val_j=='#':
                count_t += 1
            else:
                if count_t != 0:
                    count_t -= 1
                    continue
                else:
                    tmpT.append(val_j)
        # print(tmpT)

        return tmpS==tmpT


def main():
    S = "a#c"
    T = "b"
    myResult = Solution()
    print(myResult.backspaceCompare(S,T))

if __name__ == '__main__':
    main()