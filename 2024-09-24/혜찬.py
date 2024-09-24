import sys

input = sys.stdin.readline
# https://www.acmicpc.net/problem/14500

N, M = [int(_) for _ in input().rstrip().split()]

map = []

for _ in range(N):
    map.append([int(a) for a in input().rstrip().split()])

'''
시작점으로부터 어떤 방향으로는 겹치지 않게 4칸을 선택하게 한다.
선택된 칸의 합을 구해서 최대인 경우 갱신
'''
DIR = ((0, 1), (1, 0), (0, -1), (-1, 0))

def selectBlocks(r, c, pr, pc, count, total):
    global answer
    
    if count == 4:
        answer = max(answer, total)
        return

    for dr, dc in DIR:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
        if nr == pr and nc == pc: continue
        selectBlocks(nr, nc, r, c, count + 1, total + map[nr][nc])

'''
T 블록은 연속된 이동으로 갈 수 없으니 예외처리
'''
def checkT(r, c):
    global answer

    locations = (((r, c), (r + 1, c), (r + 2, c), (r + 1, c + 1)),
        ((r, c), (r + 1, c), (r + 2, c), (r + 1, c - 1)),
        ((r, c), (r - 1, c), (r - 2, c), (r - 1, c + 1)),
        ((r, c), (r - 1, c), (r - 2, c), (r - 1, c - 1)),
        ((r, c), (r, c + 1), (r, c + 2), (r + 1, c + 1)),
        ((r, c), (r, c + 1), (r, c + 2), (r - 1, c + 1)),
        ((r, c), (r, c - 1), (r, c - 2), (r + 1, c - 1)),
        ((r, c), (r, c - 1), (r, c - 2), (r - 1, c - 1)))
    
    for T in locations:
        total, count = 0, 0
        for row, col in T:
            if row < 0 or row >= N or col < 0 or col >= M: break
            total += map[row][col]
            count += 1
        if count == 4:
            answer = max(answer, total)
        

answer = -1
for r in range(N):
    for c in range(M):
        selectBlocks(r, c, -1, -1, 1, map[r][c])
        checkT(r, c)

print(answer)