import sys
import heapq

n = int(sys.stdin.readline())

maxHeap = []
minHeap = []

for _ in range(n):
  num = int(sys.stdin.readline())

  if len(maxHeap) == 0:
    heapq.heappush(maxHeap, -1 * num)
  elif len(minHeap) == len(maxHeap):
    heapq.heappush(maxHeap, -1 * num)
  else:
    heapq.heappush(minHeap, num)

  if len(minHeap) != 0 and len(maxHeap) != 0 and minHeap[0] < (-1 * maxHeap[0]):
    tmp_min = heapq.heappop(minHeap)
    tmp_max = heapq.heappop(maxHeap)

    heapq.heappush(maxHeap, -1 * tmp_min)
    heapq.heappush(minHeap, -1 * tmp_max)

  print(-1 * maxHeap[0])