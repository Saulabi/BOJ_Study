import math

A, B, V = map(int, input().split())

result = math.ceil((V - A) / (A - B)) + 1

print(result)