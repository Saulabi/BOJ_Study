N = int(input())
grade =list(map(int, input().split()))

M = max(grade)
sumGrade = 0

for i in range(N):
  grade[i] = grade[i] / M * 100
  sumGrade += grade[i]

result = sumGrade / N
print('%.2f' % result)