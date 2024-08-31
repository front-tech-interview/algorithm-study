from heapq import *
import sys

input = sys.stdin.readline
# https://www.acmicpc.net/problem/1700

N, K = [int(_) for _ in input().rstrip().split()]

count = [0] * (K + 1)
usage = [int(_) for _ in input().rstrip().split()]
for u in usage:
    count[u] += 1

currentTap = []

def findFarIndex(index):
    farIndexInUsage = -1
    farIndexInCurrentTap = -1
    for i, cur in enumerate(currentTap):
        if count[cur] == 0:
            return i
        for ui, u in enumerate(usage[index:]):
            if cur == u:
                if ui > farIndexInUsage:
                    farIndexInUsage = ui
                    farIndexInCurrentTap = i
                break

    return farIndexInCurrentTap

answer = 0
for i, u in enumerate(usage):
    if u not in currentTap:
        if len(currentTap) < N:
            currentTap.append(u)
        else:
            farIndex = findFarIndex(i)
            currentTap[farIndex] = u
            answer += 1
    count[u] -= 1

print(answer)