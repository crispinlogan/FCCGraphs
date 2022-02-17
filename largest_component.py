"""From https://structy.net/problems/largest-component and minute 73 in video"""

from collections import deque

from sympy import comp

def largest_component(graph):
    # have a unvisited nodes set
    unvisited_nodes = set(graph.keys())

    # while there are elements in the unvisited nodes set we make sure to pick a random
    # start point from it and do a trraversal, removing visited nodes from the unvisited
    # nodes set
    # the traversal has to return a count of the visited nodes in that traversal (could
    # be len(visited))
    def dfs(start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        unvisited_nodes.remove(start)
        for neighbour in graph[start]:
            if neighbour not in visited:
                dfs(neighbour, visited)
        return len(visited)

    def dfs(start):
        s = [start]
        visited = set()
        while s:
            c = s.pop()
            visited.add(c)
            # print(c, unvisited_nodes)
            if c in unvisited_nodes:
                unvisited_nodes.remove(c)
            for neighbour in graph[c]:
                if neighbour not in visited:
                    s.append(neighbour)
        return len(visited)

    def bfs(start):
        q = deque()
        q.append(start)
        visited = set()
        while q:
            c = q.popleft()
            visited.add(c)
            # print(c, unvisited_nodes)
            if c in unvisited_nodes:
                unvisited_nodes.remove(c)
            for neighbour in graph[c]:
                if neighbour not in visited:
                    q.append(neighbour)
        return len(visited)


    largest_component_num_nodes = 0
    while unvisited_nodes:
        # choose a random node that is unvisited to start
        start = unvisited_nodes.pop()
        unvisited_nodes.add(start)
        # do traversal
        # component_size = dfs(start)
        # component_size = dfs(start)
        component_size = bfs(start)
        if component_size > largest_component_num_nodes:
            largest_component_num_nodes = component_size

    return largest_component_num_nodes



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

print(largest_component(graph)) # -> 4




########
# Can also do one that actually counts more directly like in the vid
########
def largest_component(graph):
    def dfs_counter(start, graph):
        if start in visited:
            return 0

        visited.add(start)
        unvisited.remove(start)

        size = 1

        for neighbour in graph[start]:
            size += dfs_counter(neighbour, graph)

        return size

    visited = set()
    unvisited = set(graph.keys())

    largest_component_num_nodes = 0

    while unvisited:
        # get a starting point (and need to re-add to set! only way to get something from a set!)
        start = unvisited.pop()
        unvisited.add(start)
        # get num nodes in the component that has the start point in it
        component_num_nodes = dfs_counter(start, graph)
        if component_num_nodes > largest_component_num_nodes:
            largest_component_num_nodes = component_num_nodes

    return largest_component_num_nodes


print(largest_component(graph)) # -> 4
