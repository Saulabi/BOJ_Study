import sys

sys.setrecursionlimit(10**9)  # 런타임 에러 보완

V, E = map(int, input().split())
visited = [0] * (V+1)  # visitied 초기화
graph = [[] for i in range(V + 1)]  # 빈 그래프 생성

# 주어진 간선에 따라 그래프 채워넣기
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)

# dfs 재귀 함수
def dfs(v, visited, stack):
    visited[v] = True

    for i in graph[v]:
        if visited[i] == False:
            stack.append(i)
            dfs(i, visited, stack)
    stack.append(v)  # 탐색을 마친 노드 stack에 저장.

# 역방향 그래프 생성
def reverseGraph():
    reverse_graph = [[] for i in range(V+1)]
    for i in range(1, V+1):
        for j in graph[i]:
            reverse_graph[j].append(i)
    return reverse_graph

# 역방향 그래프에 dfs 진행
def reverseDfs(v, visited,stack):
    visited[v] = True
    stack.append(v)
    for i in reverse_graph[v]:
        if visited[i] == False:
            reverseDfs(i, visited, stack)

stack = []
for i in range(1, V+1):
    if visited[i] == 0:
        dfs(i, visited, stack)  # stack에 탐색을 마친 정점 순으로 저장

reverse_graph = reverseGraph()  # 역방향 그래프 생성

visited = [0] * (V+1)  # visited 초기화
result = []  # scc를 담을 result 생성

while stack:
    scc = []
    node = stack.pop()  # stack에서 scc의 source 추출
    if visited[node] == 0:
        reverseDfs(node, visited, scc)  # dfs를 진행하면서, scc의 source부터 탐색을 진행한다. 탐색한 정점은 scc에 저장
        result.append(sorted(scc))  # 재귀가 끝난 정점이 scc의 sink

print(len(result))
result = sorted(result)

for i in result:
    for j in i:
        print(j, end=' ')
    print(-1)