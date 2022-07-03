from itertools import permutations
def fn1(n,q):
    s = "".join([str(i) for i in range(1,n+1)])
    # l = list(permutations(s))
    # print(s)
    l = Permutation(s)
    # print(l)
    # l = [list(i) for i in l]
    q = "".join(q)
    idx = l.index(q)
    lens = len(l)
    res = l[lens-idx-1]
    # print(res)
    return " ".join(res)


def Permutation(ss):
    # write code here
    if len(ss) <= 0:
        return []
    res = list()
    perm(ss, res, '')
    uniq = list(set(res))
    return sorted(uniq)
# 从子串中挑一个字符，插入新的字符

def perm(ss, res, path):
    if ss == '':
        res.append(path)
    else:
        for i in range(len(ss)):
            perm(ss[:i]+ss[i+1:], res, path+ss[i])

if __name__ == '__main__':
    n = input().strip()
    n = int(n)
    q = input().strip().split()
    q = [i for i in q]
    # n = 3
    # q = ['1','2','3']
    # n = 5
    # q = [3,1,5,2,4]
    res = fn1(n,q)
    print(res)

"""
#include <iostream>
using namespace std;
 
int main()
{
    int n;
    int tmp;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        scanf("%d",&tmp);
        printf("%d ",n-tmp+1);
    }
    return 0;
}
"""