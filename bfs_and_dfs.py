"""
One thing to note (see video at 28.50) that DFS and BFS iterative are
effectively identical code, with the only difference being stack vs queue
and then the removal and adding of elements to those aforementioned data
structures
"""

"""
     a----->b
     |      |
     |      |
     ↓      ↓
     c<---- d----->e
            |
            |
            ↓
            f
"""
from collections import deque

graph = {
    'a':['c','b'],
    'b':['d'],
    'c':[],
    'd':['c','e','f'],
    'e':[],
    'f':[],
}

graph = {
    'a':['b','c'],
    'b':['d'],
    'c':[],
    'd':['c','e','f'],
    'e':[],
    'f':[],
}

def dfs(node: str):
    s = [node]
    while s:
        curr = s.pop()
        print(curr)
        for neighbour in graph[curr]:
            s.append(neighbour)

def dfs(node: str):
    visited = set()
    s = [node]
    while s:
        curr = s.pop()
        print(curr)
        visited.add(curr)
        for neighbour in graph[curr]:
            if neighbour not in visited:
                s.append(neighbour)

dfs('a')
dfs('d')
dfs('f')

def bfs(node: str):
    q = deque()
    q.append(node)
    while q:
        curr = q.popleft()
        print(curr)
        for neighbour in graph[curr]:
            q.append(neighbour)

def bfs(node: str):
    visited = set()
    q = deque()
    q.append(node)
    while q:
        curr = q.popleft()
        print(curr)
        visited.add(curr)
        for neighbour in graph[curr]:
            if neighbour not in visited:
                q.append(neighbour)

bfs('a')
bfs('d')
bfs('f')
