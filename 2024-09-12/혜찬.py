import sys

input = sys.stdin.readline
# https://www.acmicpc.net/problem/1300

N = int(input())
K = int(input())

'''
B[K] 를 x 라고 할 때, x 이하의 값을 가지는 원소가 K 개여야 한다.
숫자 x 에 대해서 x 이하의 원소 개수를 구하는 로직이 있다면, x 값을 이분탐색으로 찾아낼 수 있다.

x 이하의 원소 개수를 찾는 법?
각각의 행에 저장된 값은 행 번호 * 열 번호 이므로,
즉, "x // 행번호" 의 값을 각 행에 대하여 수행하면 행별로 x 이하의 원소 갯수를 구할 수 있다.
따라서 시간복잡도는 O(N) 이고,

이분탐색의 각 스텝마다 반복되므로 총 시간복잡도는 N * log(N) 이 된다.
'''

def getLteCount(num):
    count = 0
    for n in range(1, N + 1):
        if n > num: break
        count += min(N, num // n)
    return count

def binarySearch():
    left, right = 1, 10 ** 10
    middle = (left + right) // 2
    count = getLteCount(middle)

    while left < right:
        middle = (left + right) // 2
        count = getLteCount(middle)

        if count >= K:
            right = middle
        else:
            left = middle + 1
    

    return left

print(binarySearch())