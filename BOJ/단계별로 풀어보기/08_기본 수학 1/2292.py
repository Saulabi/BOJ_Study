n = int(input())

first = 1
cnt_six = 6
count = 1

while n > first:
  count += 1
  first += cnt_six
  cnt_six += 6

print(count)