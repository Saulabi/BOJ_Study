N = int(input())

shape = [[' ' for _ in range(N)] for _ in range(N)]

def instar(size, x, y):
  if size == 1:
    shape[y][x] = '*'

  else:
    next_size = size // 3
    for dy in range(3):
      for dx in range(3):
        if dy != 1 or dx != 1:
          instar(next_size, x + dx * next_size, y + dy * next_size)

instar(N, 0, 0)
for k in shape:
  print(''.join(k))