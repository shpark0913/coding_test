# 백준 2805 (실버 2)
# https://www.acmicpc.net/problem/2805
# Python3 / 메모리 : 31732KB / 시간 : 308ms

import sys
input = sys.stdin.readline

# 나무의 수, 집으로 가져 가려고 하는 나무의 길이
N, M = map(int, input().split())

# 나무의 높이들
trees = sorted(list(map(int, input().split())))

start = 0
end = trees[-1]
result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for tree in trees:
        if tree > mid:
            total += (tree - mid)

    if total < M:
        end = mid - 1

    elif total >= M:
        result = mid
        start = mid + 1

print(result)