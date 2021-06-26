# n 이하의 숫자들 중 소수 찾기
def prime_list(n):
  sieve = [True] * n
  for i in range(2, int(n**0.5)+1):
    if sieve[i] == True:
      for j in range(i+i, n, i):
        sieve[j] = False
  return [i for i in range(2, n) if sieve[i] == True]

# n 이하의 소수들 중 합이n
def sosu(n):
  li = prime_list(n)
  idx = max([i for i in range(len(li)) if li[i] <= n/2])
  for j in range(idx, -1, -1):
    for k in range(j, len(li)):
      if li[j] + li[k] == n:
        return [li[j], li[k]]

T = int(input())
for _ in range(T):
  n = int(input())
  print(' '.join(map(str, sosu(n))))