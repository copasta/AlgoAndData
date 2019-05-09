
N =int(input())

dic = {}

for _ in range(N):
    S = input().split()
    if S[0] == 'insert':
        dic[S[1]] = True
    else:
        if S[1] in dic: # -> dic.__contains__(S[1])
            print('yes')
        else:
            print('no')