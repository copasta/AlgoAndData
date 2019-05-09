
n = int(input())
S = list(map(int, input().split(' ')))
q = int(input())
T = list(map(int, input().split(' ')))

C = 0

for tt in T:
    for ss in S:
        if tt == ss:
            C += 1
            break
print(C)