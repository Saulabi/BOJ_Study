N = int(input())

numbers = list(map(int, input().split()))
numbers.sort()
print('{} {}'.format(min(numbers), max(numbers)))