import sys

input = sys.stdin.readline
# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def clean(x, y, d):
    global ans
    if arr[x][y] == 0:
        arr[x][y] = 2
        ans += 1
    for _ in range(4):
        nd = (d + 3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if arr[nx][ny] == 0:
            clean(nx, ny, nd)
            return
        d = nd
    nd = (d + 2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if arr[nx][ny] == 1:
        return
    clean(nx, ny, d)


n, m = map(int, input().split())
x, y, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0
clean(x, y, d)
print(ans)