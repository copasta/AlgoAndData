#Accepted

n = int(input())
s = []
for i in range(n):
    s.append(int(input()))
max_s = -10**9
min_s = s[0]
for i in range(1, n):
    max_s = max(max_s, s[i] - min_s)
    min_s = min(min_s, s[i])

print(max_s)