N = NN = int(input())

count = 0

while True:
  ten = N // 10
  one = N % 10
  temp = ten + one
  count += 1
  N = int(str(one) + str(temp % 10))
  
  
  if (NN == N):
    break

print(count)