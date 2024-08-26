import sys
input = sys.stdin.readline

T = int(input())
dp = [0] * 101
dp[1] = dp[2] = dp[3] = 1

for _ in range(T):
  N = int(input())
  for i in range(4, N+1):
    dp[i] = dp[i-2] + dp[i-3]
  print(dp[N])