# 判断n个数字构成能否构成一个环
# 思路：一共n个数，我们只用考虑3个最大的数就行了，只要最大的比两个次大的小就OK
"""
#include <iostream>

using namespace std;
int main()
{
    int t;
    scanf("%d",&t);
    while(t--){
        int n;
        scanf("%d",&n);
        long long max1=0,max2=0,max3=0;
        while(n--){
            long long a;
            scanf("%lld",&a);
            if(a<max1)
                continue;
            max1=a;
            if(a<max2)
                continue;
            max1=max2;
            max2=a;
            if(a<max3)
                continue;
            max2=max3;
            max3=a;
        }
        if(max3<max2+max1)
            cout<<"YES"<<endl;
        else
            cout<<"NO"<<endl;
    }
    return 0;
}
"""