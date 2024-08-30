from collections import defaultdict
import sys

input = sys.stdin.readline
# https://www.acmicpc.net/problem/2015

N, K = [int(_) for _ in input().rstrip().split()]
A = [int(_) for _ in input().rstrip().split()]

# A[0~i] 까지 누적합 저장한 배열
subSum = []

total = 0
for a in A:
    total += a
    subSum.append(total)

'''
0 ~ N 까지 순회하며 i번째 원소까지의 누적합에 대해 아래 로직을 반복한다.
1. 이전의 누적합을 뺐을 때 K 가 되는 값이 있는지 map 에서 개수를 체크하고 정답에 더해준다.
    sum(0~i) - sum(0~j) = K
    sum(0~i) - K = sum(0~j)
2. 이후 i번째 원소까지의 누적합이 K라면 정답 갯수에 포함시킨고, map 에 부분합 개수를 추가해준다.
3. i번째 원소까지의 누적합을 map 에 더해준다.
'''
# { 부분합: 부분합개수 } 를 저장할 map 을 생성한다.
subMap = defaultdict(int)
answer = 0
for i in range(N):
    answer += subMap[subSum[i] - K]
    if subSum[i] == K: answer += 1
    subMap[subSum[i]] += 1

print(answer)