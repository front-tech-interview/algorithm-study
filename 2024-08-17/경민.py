import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

# 주어진 지점에 대한 dfs 처리.
def dfs(x, y, h):
  visit[x][y] = True

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < N and 0 <= ny < N:
      if zone[nx][ny] > h and not visit[nx][ny]:
        dfs(nx, ny, h)

N = int(input())

# 영역과 방문처리
zone = [list(map(int, input().split())) for _ in range(N)]
visit = [[False] * N for _ in range(N)]

# 가장 높은 곳 저장
max_num = []

for i in zone:
  max_num.append(max(i))

biggest = max(max_num)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

safe_zone = 0

# 안전 영역 구하기
for h in range(biggest+1):
  safe = 0
  visit = [[False] * N for _ in range(N)]

  for i in range(N):
    for j in range(N):
      if zone[i][j] > h and not visit[i][j]:
        dfs(i, j, h)
        safe += 1

  safe_zone = max(safe_zone, safe)

print(safe_zone)