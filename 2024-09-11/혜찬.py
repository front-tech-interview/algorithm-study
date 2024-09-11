import sys

input = sys.stdin.readline
# https://www.acmicpc.net/problem/7453

n = int(input())

A, B, C, D = [], [], [], []
for _ in range(n):
    a,b,c,d = [int(a) for a in input().rstrip().split()]
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

'''
A, B 합 저장 = AB
C, D 합 저장 = CD 
AB, CD 생성 후 정렬
시간복잡도 = N^2 log(N^2) = 16000000 * 24 = 384000000
이후 투 포인터로 AB 처음, CD 끝부터 조합
합이 0보다 크면 CD 의 index - 1
0보다 작으면 AB 의 index + 1
만약 0인 경우 정답 1 누적 후 , AB 와 CD 의 같은 수 개수를 체크
두 배열의 같은 수 개수를 곱해서 정답에 누적 후 두 배열 각각 같은 수 개수만큼 다음 숫자로 이동.
'''
AB, CD = [], []

for a in A:
    for b in B:
        AB.append(a + b)
for c in C:
    for d in D:
        CD.append(c + d)
AB.sort()
CD.sort()

left, right = 0, n**2 - 1

answer = 0
while (left < n ** 2) and (right >= 0):
    abcd = AB[left] + CD[right]

    if abcd == 0:
        leftCount, rightCount = 1, 1
        while (left + leftCount) < (n**2):
            if AB[left] == AB[left + leftCount]: leftCount += 1
            else: break
        while (right - rightCount) >= 0:
            if CD[right] == CD[right - rightCount]: rightCount += 1
            else: break
        left += leftCount
        right -= rightCount
        answer += (leftCount * rightCount)
    elif abcd < 0:
        left += 1
    else:
        right -= 1

print(answer)