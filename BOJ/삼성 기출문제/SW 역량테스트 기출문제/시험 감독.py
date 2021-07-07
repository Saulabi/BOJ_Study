import sys

input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))
B, C = map(int, input().split())

result = 0
for a in A:
    a -= B
    count = 1

    if a > 0:
        count += (a // C)
        if a % C != 0:
            count += 1
    result += count

print(result)