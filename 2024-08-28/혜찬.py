from collections import defaultdict
import sys

input = sys.stdin.readline
# https://www.acmicpc.net/problem/9251

'''
입력받은 infix 수식에 반복분을 통해 순서대로 접근하며 처리한다.

1. 문자열은 그냥 바로 정답에 누적시켜준다.
2. 괄호와 연산자 정보는 stack 으로 처리한다.
- 여는 괄호 : stack 에 push
- 닫는 괄호 : 최초로 여는 괄호가 등장할 때 까지 stack 에 pop 을 반복한다. 연산자가 등장하면 바로 정답에 누적한다.
- *, / 연산자 : stack 에 쌓인 최근 연산자 정보들 중 같은 우선순위의 연산자들까지만 pop 해 정답에 누적해주고, 현재 연산자를 stack 에 push 
- +, - 연산자 : stack 에 쌓인 최근 연산자들을 pop 해 모두 정답에 누적한고, 현재 연산자를 stack 에 push(여는 괄호 제외)
'''

infix = input().rstrip()

stack = []
answer = []
for x in infix:
    if x == '(':
        stack.append(x)
    elif x == ')':
        while stack and (stack[-1] != '('):
            answer.append(stack.pop()) # 연산자 pop 해서 정답에 추가.
        stack.pop() # 여는 괄호 pop
    elif x in '*/':
        while stack and (stack[-1] in '*/'):
            answer.append(stack.pop()) # 동일 우선순위 이전 연산자 정답에 추가.
        stack.append(x) # 현재 연산자 stack 에 추가.
    elif x in '+-':
        while stack and (stack[-1] != '('):
            answer.append(stack.pop()) # 모든 이전 연산자 정답에 추가.
        stack.append(x) # 현재 연산자 stack 에 추가.
    else:
        answer.append(x)
while stack:
    answer.append(stack.pop())

print(''.join(answer))