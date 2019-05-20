n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))
sumA = sum(A)

def solve(i, mm):
    if mm == 0:
        return True
    elif sumA < mm: 
        # sumA < mm が無い場合はTLEになる
        return False
    elif i >= n:
        return False
    res = solve(i+1, mm) or solve(i+1, mm - A[i])
    return res

def main():
    for mm in m:
        if solve(0, mm):
            print('yes')
        else:
            print('no')

if __name__ == "__main__":
    main()