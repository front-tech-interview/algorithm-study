from collections import defaultdict
import sys

input = sys.stdin.readline
# https://www.acmicpc.net/problem/9461

T = int(input())

'''
잘 모르겠지만 나선 내 규칙을 발견.
dy[i] = dy[i-1] + dy[i-5]
'''
dy = [1] * 101
dy[4] = 2
dy[5] = 2
for i in range(6, 101):
    dy[i] = dy[i-1] + dy[i-5]

for _ in range(T):
    N = int(input())
    print(dy[N])