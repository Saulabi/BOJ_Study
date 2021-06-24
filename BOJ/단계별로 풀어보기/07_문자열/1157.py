word = input().upper()
countList = []

for i in set(word):
    countList.append(word.count(i))

idx = [i for i, x in enumerate(countList) if x == max(countList)]
if len(idx) > 1:
    print('?')
else:
    print(list(set(word))[countList.index(max(countList))])