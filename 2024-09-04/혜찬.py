from heapq import *
from collections import defaultdict
import sys

input = sys.stdin.readline
# https://www.acmicpc.net/problem/1202

N, K = [int(_) for _ in input().split()]
JEWELS = defaultdict(list)

for _ in range(N):
    M, V = [int(a) for a in input().split()]
    JEWELS[M].append(V)

BAG = []

for _ in range(K):
    BAG.append(int(input()))
BAG.sort()

'''
용량이 가장 작은 가방 순으로 처리한다.
가방에 들어갈 수 있는 보석 중 가장 비싼것을 제거한다.
Max Heap 을 사용하자.
보석 정보는 보석 무게를 key 로 사용하여 무게별로 보석 가격을 저장해준다.
가방 무게를 오름차순으로 정렬한다. 이후 가방별로 반복문을 돌려가면서,
가능한 가장 비싼 보석을 Max Heap 에서 pop 해온다.
(반복문으로 가방의 무게가 변하는 경우, 새로운 가방 무게에 맞는 보석들을 Max Heap 에 push 해준다.)

엣지 케이스
- max heap 에서 pop 할 보석이 없는 경우.

시간복잡도: 가방 정렬 + 모든 보석 정보 heap 에 push / pop = 3 NlogN = 3 * 300000 * 18 = 16200000
'''

prevM = -1 # 이전가지 체크된 가방 용량
maxHeap = []
heapify(maxHeap)

answer = 0
for b in BAG:
    if b > prevM:
        # 커진 가방 용량을 고려하여 보석을 Max Heap 에 추가해준다.
        for m in range(prevM + 1, b + 1):
            for j in JEWELS[m]:
                heappush(maxHeap, -j)
        prevM = b
    if maxHeap: answer += heappop(maxHeap)

print(-answer)