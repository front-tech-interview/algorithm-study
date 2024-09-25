import sys

input = sys.stdin.readline
# https://www.acmicpc.net/problem/2504

brace = input().rstrip()

'''
닫히는 괄호는 반드시 직전 괄호와 매칭되어야 한다.
'''

def solve():    
    stack = []
    answer = 0
    acc = 1

    for i, b in enumerate(brace):
        if b == '(':
            stack.append(b)
            acc *= 2
        elif b == '[':
            stack.append(b)
            acc *= 3
        elif b == ')':
            if not stack or stack[-1] != '(':
                return 0
            if brace[i - 1] == '(':
                answer += acc
            acc //= 2
            stack.pop()
        elif b == ']':
            if not stack or stack[-1] != '[':
                return 0
            if brace[i - 1] == '[':
                answer += acc
            acc //= 3
            stack.pop()

    if stack: return 0
    else: return answer
    
print(solve())