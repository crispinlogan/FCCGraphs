"""From https://structy.net/problems/largest-component and minute 84 in video"""


from collections import defaultdict, deque


def shortest_path(edges, node_A, node_B):
    # first convert edges into an adj_list
    adj_list = defaultdict(set)
    for edge in edges:
        adj_list[edge[0]].add(edge[1])
        adj_list[edge[1]].add(edge[0])

    # then find shortest path - we can do this using BFS, and counting the number of
    # times we need to go out one breadth further until we hit node_B
    visited = set()
    all_nodes = set(adj_list.keys())
    def bfs(start, end, graph):
        q = deque()
        q.append([start])
        num_iterations = 0
        while q:
            currs = q.popleft()
            nexts = []
            for c in currs:
                if c == end:
                    return num_iterations
                visited.add(c)
                for neighbour in graph[c]:
                    nexts.append(neighbour)
            if set(nexts).issubset(visited):
                return -1
            q.append(nexts)
            num_iterations += 1
        # return -1

    return bfs(node_A, node_B, adj_list)


edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

"""
x---y---z
|       |
|       |
w-------v
"""

print(shortest_path(edges, 'w', 'z')) # -> 2
print(shortest_path(edges, 'w', 'y')) # -> 2
print(shortest_path(edges, 'w', 'x')) # -> 1
print(shortest_path(edges, 'w', 'w')) # -> 0
print(shortest_path(edges, 'w', 'a')) # -> -1


edges = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
]

"""
a---c
|  /|
| / |
|/  |
b---d---e

g---f
"""

print(shortest_path(edges, 'e', 'c')) # -> 2


edges = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
]

"""
a---c
|  /|
| / |
|/  |
b---d---e

g---f
"""

print(shortest_path(edges, 'b', 'g')) # -> -1
print(shortest_path(edges, 'b', 'd')) # -> 1
print(shortest_path(edges, 'b', 'e')) # -> 2



########
# More like the solution in the video
########

def shortest_path(edges, node_A, node_B):
    # first convert edges into an adj_list
    adj_list = defaultdict(set)
    for edge in edges:
        adj_list[edge[0]].add(edge[1])
        adj_list[edge[1]].add(edge[0])

    # then find shortest path - we can do this using BFS, and counting the number of
    # times we need to go out one breadth further until we hit node_B
    visited = set()
    def bfs(start, end, graph):
        q = deque([[start, 0]])
        while q:
            c, distance = q.popleft()
            if c == end:
                return distance
            visited.add(c)
            for neighbour in graph[c]:
                if neighbour not in visited:
                    q.append([neighbour, distance+1])
        return -1

    return bfs(node_A, node_B, adj_list)

print(shortest_path(edges, 'b', 'g')) # -> -1
print(shortest_path(edges, 'b', 'd')) # -> 1
print(shortest_path(edges, 'b', 'e')) # -> 2
