X = int(input())

line = 0
max_X = 0

while X > max_X:
  line += 1
  max_X += line

gap = max_X - X

if line % 2 == 0:
  top = line - gap
  under = gap + 1

else:
  top = gap + 1
  under = line - gap

print(f'{top}/{under}')