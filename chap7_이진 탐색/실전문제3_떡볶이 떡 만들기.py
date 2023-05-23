# 떡의 개수, 요청한 떡의 길이
N, M = map(int, input().split())

rice_cakes = list(map(int, input().split()))

start = 0
end = max(rice_cakes)

# 이진탐색 수행(반복적)
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in rice_cakes:
        if x > mid:
            total += (x - mid)
    if total < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)