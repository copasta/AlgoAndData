
s = input()

area_all = 0
area_sub = 0

S1 = []
S2 = []
S_temp = []

for i, ss in enumerate(s):
    if ss == '\\':
        S1.append(i)
    elif ss == '/' and S1:
        # 水たまりの総面積
        p = S1.pop()
        area_sub = i - p
        area_all += area_sub

        # 各水たまりの面積
        while S_temp and S_temp[-1] > p:
            area_sub+=S2.pop()
            S_temp.pop()
        S_temp.append(p)
        S2.append(area_sub)

print(area_all)
# print(len(S2), " ".join(map(str, S2))) ->  Presentation Error
# Why?
print(len(S2), *(S2))