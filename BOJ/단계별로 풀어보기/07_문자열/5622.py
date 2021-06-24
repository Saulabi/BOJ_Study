dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
result = 0

for i in range(len(word)):
  for j in dial:
    if word[i] in j:
      result += dial.index(j) + 3

print(result)