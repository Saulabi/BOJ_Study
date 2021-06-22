numbers = []

for _ in range(9):
  numbers.append(int(input()))

a = max(numbers)
print(a)
print(numbers.index(a) + 1)