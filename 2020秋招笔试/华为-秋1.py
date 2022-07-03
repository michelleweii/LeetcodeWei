"""
def minRuelStops(target, startFuel, stations):
    m = len(stations)
    if not m:
        return 0 if target <= startFuel else -1

    dp = [[-1] * (m + 1) for _ in range(m + 1)]
    dp[0][0] = startFuel

    for i in range(m + 1):
        for j in range(m - i + 1):
            if i + j != 0:
                dist = stations[i + j - 1][0] - stations[i + j - 2][0] if i + j != 1 else stations[0][0]
            if i > 0:
                if dp[i - 1][j] >= dist:
                    dp[i][j] = max(dp[i - 1][j] + stations[i + j - 1][1] - dist, dp[i][j])
            if j > 0:
                if dp[i][j - 1] >= dist:
                    dp[i][j] = max(dp[i][j - 1] - dist, dp[i][j])
    for i in range(m + 1):
        if dp[i][m - i] >= target - stations[-1][0]:
            return i
    return -1
"""
#include <iostream>
#include <stdio.h>
#include <queue>

using namespace std;
struct node{
    int i;
    int num;
};
#define MAXN 105
int stride[MAXN];
queue<node> q;
int main()
{
    int tmp;
    int num=0;
    while(cin>>tmp){
        stride[num++]=tmp;
    }
    int i;
    for(i=1;i<num/2;i++){
        node tmp;
        tmp.i=i;
        tmp.num=1;
        q.push(tmp);
    }
    while(!q.empty()){
        node tmp = q.front();
        q.pop();
        if(tmp.i==num-1){
            cout<<tmp.num<<endl;
            return 0;
        }else if(tmp.i>num-1)
            continue;
        else{
            node tmp0;
            tmp0.i=tmp.i+stride[tmp.i];
            tmp0.num=tmp.num+1;
            q.push(tmp0);
        }
    }
    cout<<-1<<endl;
    return 0;
}


if __name__ == '__main__':
    # s = input().strip().split(' ')
    # nums = [int(ch) for ch in s]
    # print(nums)
    # n = int(s[0])
    # m = int(s[1])
    # matrix = []
    # while n:
    #    tmp = input().strip()
    #    tmp = [int(x) for x in tmp]
    #    matrix.append(tmp)
    #    n-=1

    nums = [7, 5, 9, 4, 2, 6, 8, 3, 5, 4, 3, 9]
    stations = []
    n = len(nums)
    for i in range(n):
        stations.append([i,nums[i]])
    res = minRuelStops(n,nums[0],stations)
    print(res)

