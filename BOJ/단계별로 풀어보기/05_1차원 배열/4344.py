C = int(input())

for i in range(C):
  testCase = list(map(int, input().split(' ')))
  N = testCase[0]
  avg = sum(testCase[1:]) / N
  cnt = 0
  for j in testCase[1:]:
    if j > avg:
      cnt += 1

  print('%.3f%%' % round((cnt / N) * 100, 3))