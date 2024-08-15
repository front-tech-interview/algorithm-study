import sys
input = sys.stdin.readline

input_str = input().strip()
stack = []
res = ''
bracket = False

# < 만나면 <문자 이전의 내용들을 역순으로 저장
# > 만나면 괄호가 끝이니 그대로 저장
# 만약 괄호 안이라면 뒤집을필요 x, 그대로 저장
# 공백이고, 스택이 비어있지 않으면 역순으로 저장
# 일반 문자라면 그대로 스택에 저장
# 마지막 스택이 남아있다면 역순으로 저장

for s in input_str:
  if s == '<':
    while stack:
      res += stack.pop()
    bracket = True
    res += s
  elif s == '>':
    bracket = False
    res += s
  elif bracket:
    res += s
  elif s == ' ':
    while stack:
      res += stack.pop()
    res += s
  else:
    stack.append(s)

while stack:
  res += stack.pop()

print(res)