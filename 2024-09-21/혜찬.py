import sys

input = sys.stdin.readline
# https://www.acmicpc.net/problem/2294

n, k = [int(_) for _ in input().rstrip().split()]

coins = []

for _ in range(n):
    coins.append(int(input()))

dy = [-1] * (k + 1)

for c in coins:
    if c <= k: dy[c] = 1

for price in range(1, k + 1):
    if dy[price] == 1:
        continue
    for c in coins:
        if price - c <= 0 or dy[price - c] <= 0: continue
        dy[price] = min(dy[price - c] + 1, dy[price]) if dy[price] > 0 else dy[price - c] + 1

print(dy[k])