#include <cstdio>
#include <cstring>
#include <cmath>
#include <queue>
#include <iostream>
#include <algorithm>
using namespace std;
#define LL long long
const LL mod=1e9+7;
LL gcd(LL a,LL b)//求最大公约数
{
    return b==0?a:gcd(b,a%b);
}
LL pow_mod(LL a,LL b)//快速幂求a^b
{
    LL s=1;
    while(b)
    {
        if(b&1)
            s=(s*a)%mod;
        a=(a*a)%mod;
        b=b>>1;
    }
    return s;
}
LL polya(LL m,LL n)//polya定理
{
    LL i,ans=0;
    for(i=1;i<=n;i++)
        ans+=pow_mod(m,gcd(i,n));//旋转的情况，循环数gcd(i,n)，其中i为顺时针旋转i格
    if(n&1)ans+=n*pow_mod(m,n/2+1);//奇数的翻转情况。共n条对称轴，每条的循环数均为n/2+1
    else ans+=n/2*pow_mod(m,n/2)+n/2*pow_mod(m,n/2+1);//偶数的翻转情况。对称轴共n条，n/2条通过2个点，其余n/2条通过两点之间的中心。
    ans=ans%mod*pow_mod(2*n,mod-2)%mod;
    return ans;
}
int main()
{
    LL T,m,n,tt=0;
    cin>>m>>n;
    cout<<polya(m,n)<<endl;
    return 0;
}

/*#include <iostream>
#include <stdio.h>
#include <map>

using namespace std;

#define MAXN 100000

map<string,int> m;

int main()
{
    freopen("data.in","r",stdin);
    string s;
    cin>>s;
    string gs="";
    int len=s.length();
    int i;
    int index=0;
    for(i=0;i<len;i++){
        if(s[i]!=';')
            gs+=s[i];
        else{
            break;
            index=i+1;
        }
    }
    for(i=index;i<len;i++){
        if(s[i]!=';'){

        }
    }
    cout<<gs;
    char s1[MAXN];
    char s2[MAXN];
    char s3[MAXN];
    scanf("%s;%s;%s",s1,s2,s3);
    printf("%s\n",s1);
    printf("%s\n",s2);
    printf("%s\n",s3);
    return 0;
}
*/



"""
def fn():

if __name__ == '__main__':
    # s = input().strip().split('')
    # n = int(s[0])
    # m = int(s[1])
    # matrix = []
    # while n:
    #    tmp = input().strip()
    #    tmp = [int(x) for x in tmp]
    #    matrix.append(tmp)
    #    n-=1
    res = fn(n, m, matrix)
"""
