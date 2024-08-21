# LCS 문제인데, 연속적인 경우만 카운트.

import sys
input = sys.stdin.readline

str1 = input()
str2 = input()

str1_len = len(str1)
str2_len = len(str2)

dp = [[0] * (str2_len+1) for _ in range(str1_len + 1)]
max_len = 0

for i in range(1, str1_len):
  for j in range(1, str2_len):
    if str1[i-1] == str2[j-1]:
      dp[i][j] = dp[i-1][j-1] + 1
      max_len = max(max_len, dp[i][j])

print(max_len)