"""From https://structy.net/problems/connected-components-count and minute 60 in video"""


from collections import deque

def connected_components_count(graph):
    # get a collection of all nodes in the graph -> set(graph.keys())
    unvisited_nodes = set(graph.keys())
    # pick a random starting point in that node set and do a traversal, removing
    # nodes that you visit from the node set
    # keep doing the above, picking a new unvisited node from the node set until
    # the node set is empty
    # count the number of times you have to do this and that is your number of
    # connected components
    def dfs():
        start = unvisited_nodes.pop()
        unvisited_nodes.add(start)
        s = [start]
        visited = set()
        while s:
            c = s.pop()
            visited.add(c)
            if c in unvisited_nodes:
                unvisited_nodes.remove(c)
            for neighbour in graph[c]:
                if neighbour not in visited:
                    s.append(neighbour)

    def dfs(start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        if start in unvisited_nodes:
            unvisited_nodes.remove(start)
        for neighbour in graph[start]:
            if neighbour not in visited:
                dfs(neighbour, visited)

    def bfs():
        start = unvisited_nodes.pop()
        unvisited_nodes.add(start)
        q = deque()
        q.append(start)
        visited = set()
        while q:
            c = q.popleft()
            visited.add(c)
            if c in unvisited_nodes:
                unvisited_nodes.remove(c)
            for neighbour in graph[c]:
                if neighbour not in visited:
                    q.append(neighbour)

    num_components = 0
    while unvisited_nodes:
        num_components += 1

        # dfs()

        start = unvisited_nodes.pop()
        unvisited_nodes.add(start)
        dfs(start)

        # bfs()

    return num_components



graph = {
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}

"""
5
| \
0--8
|
1

2--4
| /
3
"""

print(connected_components_count(graph)) # -> 2
