import sys
sys.setrecursionlimit(10**3)
input = sys.stdin.readline
# https://www.acmicpc.net/problem/1987

R, C = [int(_) for _ in input().split()]

graph = []

for _ in range(R):
    graph.append([a for a in input().rstrip()])

DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
visit = [[False]*C for _ in range(R)]
alphaSet = set()

answer = 1

def dfs(r, c):
    visit[r][c] = True
    alphaSet.add(graph[r][c])
    global answer
    answer = max(answer, len(alphaSet))

    for dr, dc in DIR:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= R or nc < 0 or nc >= C or visit[nr][nc]:
            continue
        if graph[nr][nc] in alphaSet:
            continue
        dfs(nr, nc)
    
    visit[r][c] = False
    alphaSet.remove(graph[r][c])

dfs(0, 0)
print(answer)