"""From https://structy.net/problems/undirected-path and minute 42 in video"""

from collections import defaultdict

def undirected_path(edges, src, dst):
    """
    Change undirected graph / edges to an adjacency list as that is what our
    algorithms (bfs and dfs) work best on
    """
    # convert into adjacency list
    adj_list = defaultdict(set)

    for edge in edges:
        adj_list[edge[0]].add(edge[1])
        adj_list[edge[1]].add(edge[0])

    print(adj_list)

    # do dfs or bfs for the new adj_list
    def dfs_helper(adj_list, src, dst):
        s = [src]
        visited = set()
        while s:
            c = s.pop()
            visited.add(c)
            if c == dst:
                return True
            for neighbour in adj_list[c]:
                if neighbour not in visited:
                    s.append(neighbour)

        return False

    return dfs_helper(adj_list, src, dst)


edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

"""
i-----j     o-----n
|
|
|
k-----m
|
|
|
l
"""

print(undirected_path(edges, 'j', 'm')) # -> True
print(undirected_path(edges, 'k', 'o')) # -> False

edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'j'),
  ('k', 'l'),
  ('o', 'n')
]

"""
i----j     o----n
|  /
| /
|/
k----m
|
|
|
l
"""

print(undirected_path(edges, 'j', 'm')) # -> True
print(undirected_path(edges, 'k', 'o')) # -> False
