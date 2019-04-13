#Time Limit Exceeded

n = int(input())
s = []
for i in range(n):
    s.append(int(input()))
max_s = -10**9
for i in range(n-1):
    for j in range(i+1,n):
        R = s[j] - s[i]
        if max_s < R:
            max_s = R

print(max_s)
