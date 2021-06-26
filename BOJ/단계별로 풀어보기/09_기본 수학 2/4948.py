def isPrime(num):
  if num == 1:
    return False
  else:
    for i in range(2, int(num**0.5)+1):
      if num % i == 0:
        return False
    return True

li = list(range(2, 246912))
prime_li = []
for i in li:
  if isPrime(i):
    prime_li.append(i)

while True:
  result = 0
  n = int(input())
  if n == 0:
    break
  else:
    for i in prime_li:
      if n < i <= 2*n:
        result += 1
    
    print(result)