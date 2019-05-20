from operator import mul

n = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
q = int(input())
m = list(map(int, input().split()))

def solve(A, m):
    len_a = len(A)
    for mm in m:
        flag = True
        for i in range(2 ** len_a):
            t = [0] * len_a
            for j in range(len_a):
                if (i >> j) & 1:
                    t[len_a - 1 - j] = 1
            comb = sum(map(mul, A, t))
            if mm == comb:
                print('yes')
                flag = False
                break
        if flag:
            print('no')
        
solve(A, m)