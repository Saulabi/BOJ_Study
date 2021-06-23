N = int(input())
result = 0

for i in range(1, N + 1):
  if i < 100:
    result += 1

  else:
    a = str(i)
    if (int(a[0]) - int(a[1])) == (int(a[1]) - int(a[2])):
      result += 1
    else:
      result += 0

print(result)