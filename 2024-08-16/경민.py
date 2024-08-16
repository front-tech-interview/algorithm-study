# 입력 문자열 순회
# '(' 문자는 쇠막대기의 시작 또는 레이저의 시작을 의미
#  스택에 추가하여 현재 진행 중인 쇠막대기의 수 구하기
# ')' 문자면 스택의 마지막 '('를 제거. 쇠막대기의 끝이나 레이저의 끝을 의미
# 만약 순회하고 있는 바로 직전 문자가 '('면 레이저라는 의미. 스택에 쌓여있는 막대기 길이만큼 추가
# 그게 아니라면 쇠막대기의 끝부분이니까 +1

import sys
input = sys.stdin.readline

stick = input().strip()
stack = []
res = 0

for i in range(len(stick)):
  if stick[i] == '(':
    stack.append('(')
  else:
    stack.pop()
    if stick[i-1] == '(':
      res += len(stack)
    else:
      res += 1

print(res)
