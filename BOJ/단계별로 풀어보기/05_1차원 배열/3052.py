numbers = []

for _ in range(10):
  n = int(input())
  numbers.append(n % 42)

result = set(numbers)
print(len(result))