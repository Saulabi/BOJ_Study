from sys import stdin

N = int(input())
n = list(map(int, stdin.readline().split()))
M = int(input())
m = list(map(int, stdin.readline().split()))

dic = dict()

for i in n:
  try:
    dic[i] += 1
  except:
    dic[i] = 1

for i in m:
  try:
    print(dic[i], end=" ")
  except:
    print(0, end=" ")