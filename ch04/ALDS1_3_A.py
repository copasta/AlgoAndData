
A = list(map(str, input().split()))
B = []

for A_sub in A:
    if A_sub in ['+', '-', '*']:
        b = int(B.pop())
        a = int(B.pop())
        if A_sub == '+':
            B.append(a+b)
        elif A_sub == '-':
            B.append(a-b)
        elif A_sub == '*':
            B.append(a*b)
    else:
        B.append(A_sub)

print(B[0])