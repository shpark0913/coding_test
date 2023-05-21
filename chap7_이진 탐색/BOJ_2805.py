import sys
input = sys.stdin.readline

# 나무의 수, 집으로 가져 가려고 하는 나무의 길이
N, M = map(int, input().split())

# 나무의 높이들
trees = sorted(list(map(int, input().split())))

cancut = []

def binary_search(graph, target, start, end):

    while start <= end:
        mid = (start + end) // 2

        trees_sum = sum(graph[mid:]) - len(graph[mid:]) * graph[mid]

        if trees_sum > target:
            cancut.append([graph[mid], mid])
            start = mid + 1

        elif trees_sum < target:
            end = mid - 1

        else:
            cancut.append([graph[mid], mid])
            return cancut

binary_search(trees, M, 0, len(trees) - 1)

cancut = sorted(cancut, key=lambda x : x[1])

idx = cancut[-1][1]
max_height = cancut[-1][0]
print(max_height)
while 1:
    val = sum(trees[idx + 1:]) - max_height * (len(trees[idx + 1:]))
    if val > M:
        max_height += 1
    else:
        break

print(max_height)