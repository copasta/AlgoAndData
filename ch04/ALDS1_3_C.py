
# dequeの方が高速

from collections import deque

l = deque()

N = int(input())

for _ in range(N):
    d = input()
    if d == 'deleteFirst':
        l.popleft()
    elif d == 'deleteLast':
        l.pop()
    else:
        command, x = d.split(' ')
        if command == 'insert':
            l.appendleft(x)
        elif command == 'delete':
            try:
                l.remove(x)
            except:
                pass
print(' '.join(l))