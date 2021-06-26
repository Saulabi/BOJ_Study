N = int(input())
numbers = list(map(int, input().split(' ')))
result = 0

if len(numbers) == N:
  for i in numbers:
    cnt = 0
    for j in range(1, i+1):
      if i % j == 0:
        cnt += 1
    
    if cnt == 2:
      result += 1
  
print(result)