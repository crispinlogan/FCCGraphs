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

graph = {
    'a':['b','c'],
    'b':['d'],
    'c':[],
    'd':['c','e','f'],
    'e':[],
    'f':[],
}

from collections import deque
def bfs(root: str):
    """
    Just to traverse graph
    """
    node = root
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
