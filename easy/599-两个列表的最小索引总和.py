class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        pos1 = []
        pos2 = []
        tmp = []
        res = []
        summin = []
        for i,val_i in enumerate(list1):
            for j,val_j in enumerate(list2):
                if val_i==val_j:
                    pos1.append(i)
                    pos2.append(j)
                    tmp.append(val_i)
                    break
        # print(res)
        min_pos = 0
        min_val = 2001
        for i in range(len(pos1)):
            sum = pos1[i]+pos2[i]
            if(sum<=min_val):
                min_val=sum
                res.append(tmp[i])
        return res



def main():
    list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
    list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
    myResult = Solution()
    print(myResult.findRestaurant(list1,list2))

if __name__ == '__main__':
    main()
