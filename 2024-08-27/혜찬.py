from collections import defaultdict
import sys

input = sys.stdin.readline
# https://www.acmicpc.net/problem/14503

N, M = [int(_) for _ in input().rstrip().split()]

r, c, d = [int(_) for _ in input().rstrip().split()]

DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

MAP = []
for _ in range(N):
    MAP.append([int(_) for _ in input().rstrip().split()])

answer = 0

def move():
    # 청소가 가능한 방향으로 이동
    for nd in [d-1, d-2, d-3, d]:
        nr = r + DIR[nd][0]
        nc = c + DIR[nd][1]
        if MAP[nr][nc] == 0:
            return nr, nc, (nd % 4)
    
    # 청소가 불가능하면 후진 가능한 경우 이동
    # 후진이 불가능하면 -1, -1, 0 return
    nr = r - DIR[d][0]
    nc = c - DIR[d][1]
    if MAP[nr][nc] != 1:
        return nr, nc, d
    else:
        return -1, -1, 0

answer = 1
MAP[r][c] = 2
while True:
    r, c, d = move()
    if r == -1:
        break
    else:
        if MAP[r][c] == 0:
            answer += 1
            MAP[r][c] = 2

print(answer)