import sys

input = sys.stdin.readline
# https://www.acmicpc.net/problem/17609

T = int(input())

def checkPalindrome(word, isSimilar = False):
    left, right = 0, len(word) - 1
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        elif isSimilar:
            return '2'
        else:
            similar1 = checkPalindrome(word[left+1:right + 1], True)
            similar2 = checkPalindrome(word[left:right], True)
            if similar1 != '2' or similar2 != '2': return '1'
            else: return '2'
    
    return '1' if isSimilar else '0'

answer = []
for _ in range(T):
    answer.append(checkPalindrome(input().rstrip()))
print("\n".join(answer))