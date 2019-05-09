

def binarySearch(A, key):
    
    '''
    A:ソート済みリスト
    key:探索したいデータ
    '''

    # 応用
    # lower bound
    # upper bound

    # 標準モジュール
    # bisect https://docs.python.org/ja/3.7/library/bisect.html

    left = 0
    right = len(A)
    while left < right:
        mid = (left + right) // 2
        if A[mid] == key:
            return mid
        elif key < A[mid]:
            right = mid
        else:
            left = mid + 1
    return False

n = int(input())
S = list(map(int, input().split(' '))).sort()
q = int(input())
T = list(map(int, input().split(' ')))

C = 0

for tt in T:
    if binarySearch(S, tt):
        C += 1
print(C)