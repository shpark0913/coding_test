def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
        else:
            return mid
    return None

# 가게의 부품 수
N = int(input())

electronics = sorted(list(map(int, input().split())))

# 손님이 요청한 부품 수
M = int(input())

wonders = list(map(int, input().split()))

for wonder in wonders:
    ans =  binary_search(electronics, wonder, 0, len(electronics) - 1)
    if ans == None:
        print("no", end=' ')
    else:
        print('yes', end=' ')