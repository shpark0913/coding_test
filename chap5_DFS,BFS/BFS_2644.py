# 백준 2644 (실버 2)
# https://www.acmicpc.net/problem/2644
# Python3 / 메모리 : KB / 시간 : ms
# PyPy3 / 메모리 : KB / 시간 : ms
from collections import deque
import sys

input = sys.stdin.readline

# 사람의 수
n = int(input())

# 촌수를 계산해야 하는 두 사람의 번호
a, b = map(int, input().split())

# 부모 자식 관계의 개수
m = int(input())

# 부모, 자식 관계를 담는 리스트
relations = [[] for _ in range(101)]

# 방문 기록
visited = [False for _ in range(101)]

# 촌수 기록하는 object
relations_object = {}

for _ in range(m):
    x, y = map(int, input().split())
    relations[x].append(y)
    relations[y].append(x)

def bfs(V, S):
    queue = deque([V])
    relation = 1
    while queue:
        q = queue.popleft()
        visited[q] = True
        for i in relations[q]:
            if not visited[i]:
                queue.append(i)
                if i in relations_object.keys():
                    relations_object[i].append(relation)
                else:
                    relations_object[i] = [relation]
        relation += 1

bfs(a, b)
print(relations_object)
if b in relations_object.keys():
    print(min(relations_object[b]))
else:
    print(-1)