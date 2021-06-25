A, B, C = map(int, input().split())

# n = A / (C - B)

if C <= B:
  print(-1)
else:
  n = A / (C - B)
  print(int(n+1))