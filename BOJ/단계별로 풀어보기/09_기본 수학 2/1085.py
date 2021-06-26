x, y, w, h = map(int, input().split())

xd = w - x
yd = h - y

print(min([x, y, xd, yd]))