N = int(input())
K = int(input())

start = 0 
end = K
result = 0

while (start <= end):
  mid = (start + end) // 2
  total = 0
  for i in range(1, N+1):
    total += min(mid // i, N)

  if total < K:
    start = mid + 1
  else:
    result = mid
    end = mid - 1

print(result)