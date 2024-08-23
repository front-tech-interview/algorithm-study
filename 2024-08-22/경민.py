import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())
n = int(input())
arr_A = list(map(int, input().split()))
m = int(input())
arr_B = list(map(int, input().split()))
dic = defaultdict(int)

res = 0

for i in range(n):
  total = 0
  for j in range(i, n):
    total += arr_A[j]
    dic[total] += 1

for i in range(m):
  total = 0
  for j in range(i, m):
    total += arr_B[j]
    res += dic[T-total]

print(res)