import sys
import heapq

n = int(sys.stdin.readline())

heap_p = []
heap_m = []

for _ in range(n):
  num = int(sys.stdin.readline())

  if num == 0:
    if len(heap_p) == 0 and len(heap_m) == 0:
      print(0)
    elif len(heap_p) == 0 and len(heap_m) != 0:
      print(-1 * heapq.heappop(heap_m))
    elif len(heap_p) != 0 and len(heap_m) == 0:
      print(heapq.heappop(heap_p))
    else:
      p = heapq.heappop(heap_p)
      m = heapq.heappop(heap_m)

      if p < m:
        print(p)
        heapq.heappush(heap_m, m)
      else:
        print(-1 * m)
        heapq.heappush(heap_p, p)

  else:
    if num < 0:
      heapq.heappush(heap_m, (-1 * num))
    else:
      heapq.heappush(heap_p, num)