def binary_search(array, target, start, end):
  if start > end:
    return False
  mid = (start + end) // 2
  if array[mid] > target:
    return binary_search(array, target, start, mid - 1)
  elif array[mid] < target:
    return binary_search(array, target, mid + 1, end)
  else:
    return True

N = int(input())
n = list(map(int, input().split()))
M = int(input())
m = list(map(int, input().split()))
A = sorted(n)

for i in m:
  if binary_search(A, i, 0, N-1):
    print(1)
  else:
    print(0)