def fn1(array,n,m):
    print("Yes")


if __name__ == '__main__':
    N = input().strip()
    N = int(N)
    while N:
        tmp = input().strip().split(" ")
        n = int(tmp[0])
        m = int(tmp[1])
        array = []
        while n:
            tmp = input().strip()
            tmp = [ch for ch in tmp]
            array.append(tmp)
            n-=1
        # print(array)
        fn1(array,n,m)
        N-=1


"""
import queue

def Solution():
    input_x = [int(x) for x in input().split()]
    n, m = input_x[0], input_x[1]
    M = []
    for i in range(n):
        strline = input().strip()
        M.append(strline)
    flag = []
    for i in range(n):
        tmp = [False] * m
        flag.append(tmp)

    start, end = 0, 0
    for i in range(n):
        for j in range(m):
            if M[i][j] == 'S':
                start, end = i, j
                break

    flag[start][end] = True

    q = queue.Queue()

    q.put([start, end])
    direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while not q.empty():
        tmp = q.get()
        for i in range(4):
            new_i = tmp[0] + direct[i][0]
            new_j = tmp[1] + direct[i][1]
            if new_i < 0:
                new_i = n - 1
            if new_i >= n:
                new_i = 0
            if new_j < 0:
                new_j= m - 1
            if new_j >= m:
                new_j = 0

            if M[new_i][new_j] == '#':
                continue
            
            if flag[new_i][new_j]:
                return True
            else:
                flag[new_i][new_j] = True
            q.put([new_i, new_j])

    return False

# tmp = input()
T = int(input())

while T:
    res = Solution()
    if res:
        print("Yes")
    else:
        print("No")
    #print("No")
    T -= 1
"""
