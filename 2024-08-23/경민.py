import sys
input = sys.stdin.readline

def get_prime(N):
  is_prime = [True] * (N+1)
  is_prime[0] = is_prime[1] = False
  
  for i in range(2, int(N**0.5) +1):
    if is_prime[i]:
      for j in range(i*i, N+1, i):
        is_prime[j] = False
  
  prime = [i for i in range(2, N + 1) if is_prime[i]]
  cnt = cur_sum = 0
  start, end = 0, 0

  while True:
    if cur_sum < N:
      if end >= len(prime):
        break
      cur_sum += prime[end]
      end += 1
    elif cur_sum > N:
      cur_sum -= prime[start]
      start += 1
    else:
      cnt += 1
      cur_sum -= prime[start]
      start += 1

  return cnt

N = int(input())
print(get_prime(N))