import sys

def find(target):
  start, end = 1, len(stack)-1
  while (start < end):
    mid = (start + end) // 2
    if stack[mid] < target:
      start = mid + 1
    elif stack[mid] > target:
      end = mid
    else:
      start = end = mid

  return end

l = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stack = [0]

for a in arr:
  if stack[-1] < a:
    stack.append(a)
  else:
    stack[find(a)] = a

print(len(stack)-1)