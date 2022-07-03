"""
hard 2021-11-14 贪心
https://leetcode-cn.com/problems/candy/solution/candy-cong-zuo-zhi-you-cong-you-zhi-zuo-qu-zui-da-/
要求：1、每个孩子至少分配到 1 个糖果；2、评分更高的孩子必须比他两侧的邻位孩子获得更多的糖果。
如果孩子围成一个环
"""
class Solution:
    def candy(self, ratings) -> int:
        left = [1 for _ in range(len(ratings))]
        right = left[:]
        # 所有比其左边成绩好的孩子, 要比他左边孩子分多一个糖果
        for i in range(1, len(ratings)):
            if ratings[i]>ratings[i-1]: left[i] = left[i-1]+1
        count = left[-1] # 2 # 下面是跳过最后一位

        # 所有比其右边成绩好的孩子, 要比其右边孩子多分一个糖果
        for i in range(len(ratings)-2, -1,-1):
            if ratings[i]>ratings[i+1]: right[i] = right[i+1]+1

            count += max(left[i], right[i])
        return count

"""# 围成一个环
//贪心策略： 瞻前顾后
class Solution {
public:
    int candy(vector<int>& ratings) {
        const int n = ratings.size();
        vector<int> candys(n,1);
        //瞻前 ： 所有比其左边成绩好的孩子要比他左边孩子分多一个糖果
        for(int i = 0; i < n - 1; ++i){
            if(ratings[i+1] > ratings[i]){
                candys[i+1] = candys[i] + 1;
            }
        }
        //顾后 ： 所有比其右边成绩好的孩子要比其右边孩子多分一个糖果
        for(int i = n - 1; i > 0; --i){
            if(ratings[i-1] > ratings[i] && candys[i-1] <= candys[i]){
                candys[i-1] = candys[i]+1;
            }
        }
        //如果孩子围成一圈,只影响收尾两个 
        // if(ratings[0] != ratings[n-1]){
        //     if(ratings[n-1] > ratings[0]){
        //         candys[n-1] = max(candys[n-1],candys[0]+1);
        //     }
        //     else{
        //         candys[0] = max(candys[0],candys[n-1]+1);
        //     }
        // }
        int sum = 0;
        for(int &num : candys) sum += num;
        return sum;
    }
};
"""
if __name__ == '__main__':
    ratings = [1,0,2] # 5
    print(Solution().candy(ratings))