T = int(input())

for i in range(T):
  R, S = input().split()
  result = ''
  for j in S:
    result += int(R) * j
  print(result)