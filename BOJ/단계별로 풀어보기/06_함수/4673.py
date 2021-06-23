def d(n):
  number = n
  while n != 0:
    number += (n % 10)
    n //= 10
  return number

result = []
numbers = list(range(1, 10001))

for i in numbers:
  result.append(d(i))
  if i not in result:
    print(i)