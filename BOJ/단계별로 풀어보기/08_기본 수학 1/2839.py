N = int(input())

def sugarFactory(N):
  for y in range((N//3)+1):
    for x in range((N//5)+1):
      if ((5*x + 3*y) == N):
        return x+y

  return -1

print(sugarFactory(N))