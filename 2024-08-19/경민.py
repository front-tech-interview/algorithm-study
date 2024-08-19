import sys
input = sys.stdin.readline

N = int(input())
word = []

for _ in range(N):
  word.append(list(input().rstrip()))

dict = {}

# 각 알파벳 자릿수를 10의 거듭제곱 꼴로 딕셔너리에 저장

for i in word:
  x = len(i)-1
  for j in i:
    if j in dict:
      dict[j] += 10**x
    else:
      dict[j] = 10**x
    x -= 1

# 값이 제일 큰 순으로 정렬하고, 값에 따라 9부터 0까지 곱해서 더해주기

sort_dict = sorted(dict.values(), reverse=True)
num, res = 9, 0

for i in sort_dict:
  res += i * num
  num -= 1

print(res)