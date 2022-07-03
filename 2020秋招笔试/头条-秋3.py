"""
# 2048
#include <iostream>
#include <string>

using namespace std;
int a[5][5];

void r(int tr, int tc, int dr, int dc) {
    int times = dc - tc;
	int temp = 0;
	for (int i = 0; i < times; i++)
	{
		temp = a[tr][tc + i];
		a[tr][tc + i] = a[dr - i][tc];
		a[dr - i][tc] = a[dr][dc - i];
		a[dr][dc - i] = a[tr + i][dc];
		a[tr + i][dc] = temp;
	}
}

void R(int d) {
    int k = 0;
    if (d == 2) {
        k = 2;
    } else if (d == 4) {
        k = 3;
    } else if (d == 3) {
        k = 1;
    }
    while (k--) {
        int tr = 0, tc = 0, dr = 3, dc = 3;
        while (tr < dr)
        {
            r(tr++, tc++, dr--, dc--);
        }
    }
}

void L(int d) {
    int k = 0;
    if (d == 2) {
        k = 2;
    } else if (d == 4) {
        k = 1;
    } else if (d == 3) {
        k = 3;
    }
    while (k--) {
        int tr = 0, tc = 0, dr = 3, dc = 3;
        while (tr < dr)
        {
            r(tr++, tc++, dr--, dc--);
        }
    }
}

int main()
{
    int d;
    cin >> d;
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j)
            cin >> a[i][j];
    R(d);

    for (int i = 0; i < 3; ++i)
        for (int j = 0; j < 4; ++j)
            if (a[i][j] == a[i+1][j] && a[i][j]) {
                a[i][j] *= 2;
                a[i+1][j] = 0;
            }
    for (int i = 0; i < 3; ++i)
        for (int j = 0; j < 4; ++j)
            if (a[i][j] == 0) {
                int k = i+1;
                while (k < 4 && a[k][j] == 0)
                    ++k;
                if (k < 4) {
                    a[i][j] = a[k][j];
                    a[k][j] = 0;
                }
            }

    L(d);
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            if (j) cout << " ";
            cout << a[i][j];
        }
        cout << endl;
    }

    return 0;
}
"""