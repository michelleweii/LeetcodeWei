#include <iostream>
#include <string>
using namespace std;
const long long MOD = 1000000007;
long long ans[2000];
void Egcd(long long a,long long b, long long &x,long long &y)
{
    if(b == 0)
    {
        x = 1;
        y = 0;
        return ;
    }
    Egcd(b, a%b, x, y);
    long long tmp=x;
    x = y;
    y = tmp-a/b*y;
}

int main()
{
    int n;
    ans[0] = 0,
    ans[1] = 1;
    for(int i = 2; i <= 1000; ++i)
    {
        long long  x,y;
        Egcd(i+1, MOD, x, y);
        ans[i] = ans[i-1]*(4*i-2)%MOD*(x%MOD+MOD)%MOD;
    }
    cin >> n;
    cout << ans[n/2] << endl;
    return 0;
}









