from collections import deque

s = input().split(' ')
n = int(s[0])
q = int(s[1])

p = deque([])

for _ in range(n):
    s = input().split(' ')
    p_name = s[0]
    p_num = int(s[1])
    p.append([p_name,p_num])

time = 0

while len(p) > 0:
    top = p.popleft()
    time_use = min(q,top[1])
    top[1] -= time_use
    time += time_use
    if top[1] == 0:
        print(top[0], time)
    else:
        p.append(top)