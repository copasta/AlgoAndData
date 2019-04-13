#Time Limit Exceeded

n = int(input())
s = []
for i in range(n):
    s.append(int(input()))
max_s = -10**9
for i in range(n-1):
    R_i = s[i]
    s[i] = 0
    R_j = max(s)
    R = R_j - R_i
    if R > max_s:
        max_s = R

print(max_s)
