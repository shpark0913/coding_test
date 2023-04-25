N = int(input())

# 초, 분, 시
s, m, h = 0, 0, 0

# 3이 하나 라도 포함된 경우의 수를 셀 변수
cnt3 = 0

while 1:
    s += 1
    if s == 60:
        s = 0
        m += 1
    if m == 60:
        m = 0
        h += 1
    if h == N + 1:
        break
    if "3" in str(s) or "3" in str(m) or "3" in str(h):
        cnt3 += 1

print(cnt3)