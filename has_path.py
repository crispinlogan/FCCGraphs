"""From https://structy.net/problems/has-path and also minute 29 in the vid"""


def has_path(graph, src, dst):
    """
    Do either a bfs or a dfs starting from the src and if we hit the dest at any point then we know the path exists...
    """
    # def dfs(graph, src, dst):
    #     s = [src]
    #     visited = set()
    #     while s:
    #         curr = s.pop()
    #         visited.add(curr)
    #         if curr == dst:
    #             return True
    #         for neighbour in graph[curr]:
    #             if neighbour not in visited:
    #                 s.append(neighbour)
    #     return False

    def dfs(graph, src, dst, visited = None):
        if visited is None:
            visited = set()
        print(src)
        visited.add(src)
        if src == dst:
            return True
        for neighbour in graph[src]:
            if neighbour not in visited:
                res = dfs(graph, neighbour, dst, visited)
                if res:
                    return True
        return False

    return dfs(graph, src, dst)

    # def bfs(graph, src, dst):
    #     """Does bfs of graph and if it gets the dst then returns True, once entire graph traversed it returns False if not found"""
    #     from collections import deque
    #     q = deque()
    #     q.append(src)
    #     visited = set()
    #     while q:
    #         curr = q.popleft()
    #         visited.add(curr)
    #         print(curr, dst)
    #         if curr == dst:
    #             return True
    #         for neighbour in graph[curr]:
    #             if neighbour not in visited:
    #                 q.append(neighbour)
    #     return False

    # return bfs(graph, src, dst)





graph = {
    'a':['c','b'],
    'b':['d'],
    'c':[],
    'd':['c','e','f'],
    'e':[],
    'f':[],
}

print(has_path(graph, 'a', 'f'))
