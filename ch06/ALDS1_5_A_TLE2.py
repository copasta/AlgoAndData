from operator import mul

n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))
len_a = len(A)
sum_a = sum(A)

def solve(A, m):
    for mm in m:
        flag = True
        for i in range(2 ** len_a):
            t = [0] * len_a
            if  sum_a < mm:
                break
            else:
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