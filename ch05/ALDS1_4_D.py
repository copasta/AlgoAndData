
def check(P):
    i = 0
    for j in range(K):
        s = 0
        while (s + w[i]) <= P:
            s += w[i]
            i += 1
            if i == N:
                return N
    return i

def solve():
    left = 0
    right = 100000 * 100000
    while (right - left) > 1:
        mid = (right + left) // 2
        v = check(mid) # midが最小値だと仮定して可能積載数を算出
        if v >= N:
            right = mid
        else:
            left = mid
    return right

N, K = map(int, input().split(' '))
w = []

for _ in range(N):
    w.append(int(input()))

ans = solve()

print(ans)