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

def dfs(node):
    """Recursive"""
    visited = set()
    def dfs_helper(node):
        if node not in visited:
            print(node)
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs_helper(neighbour)
    dfs_helper(node)

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

def bfs(node: str):
    """Compare with above BFS and see where the nodes are being marked as visited - this can actually be better...
    you can also do the same with stack-based DFS - i.e. move where the nodes are being marked as visited
    For info see: https://stackoverflow.com/questions/63321640/when-do-you-add-a-node-to-visited-in-bfs-or-dfs"""
    visited = set()
    q = deque()
    q.append(node)
    visited.add(node)
    while q:
        curr = q.popleft()
        print(curr)
        for neighbour in graph[curr]:
            if neighbour not in visited:
                q.append(neighbour)
                visited.add(neighbour)

bfs('a')
bfs('d')
bfs('f')
