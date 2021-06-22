N = int(input())

for i in range(N):
  testCase = input()
  score = 0
  cnt = 0
  for j in range(len(testCase)):
    if testCase[j] == 'O':
      cnt += 1
      score += cnt
    elif testCase[j] == 'X':
      score += 0
      cnt = 0
  print(score)