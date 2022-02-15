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

####
# some really simple dfs - most similar to those in the vid
####
def dfs(root:str):
    # base case
    print(root)
    # recursive case
    for neighbour in graph[root]:
        dfs(neighbour)

dfs('a')

def dfs(root:str):
    visited = set()
    def dfs_helper(root:str):
        # base case
        print(root)
        visited.add(root)
        # recursive case
        for neighbour in graph[root]:
            if neighbour not in visited:
                dfs_helper(neighbour)
    dfs_helper(root)

dfs('a')

####
# My own attempts at dfs (they do work)
####
def dfs(root: str):
    """
    Just to traverse graph
    """
    visited = set()
    #
    def dfs_helper(root: str):
        # base case - if already visited
        if root in visited:
            return
        # recursive case
        print(f'Visiting {root}')
        visited.add(root)
        neighbours = graph[root]
        for neighbour in neighbours:
            if neighbour in visited:
                continue
            dfs_helper(neighbour)
        return
    dfs_helper(root)
    print('We have now visited all nodes using dfs')

dfs('a')
dfs('d')
dfs('f')



def dfs(root: str, target: str):
    """
    To find a target
    """
    visited = set()
    #
    def dfs_helper(root: str, target: str):
        # base case - if already visited
        if root in visited:
            return
        # recursive case
        print(f'Visiting {root}')
        if root == target:
            print(f'We found {target}')
            return True
        visited.add(root)
        neighbours = graph[root]
        for neighbour in neighbours:
            if neighbour in visited:
                continue
            if dfs_helper(neighbour, target):
                return True
        return
    return dfs_helper(root, target)

dfs('a', 'f')
dfs('a', 'c')
dfs('a', 'd')
dfs('a', 'b')
dfs('d', 'f')
dfs('d', 'a')
dfs('f','f')
dfs('f','g')




################################################################################
# Iterative
################################################################################
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

# same graph just listing node neighbours in different order
graph = {
    'a':['c','b'],
    'b':['d'],
    'c':[],
    'd':['f','e','c'],
    'e':[],
    'f':[],
}

def dfs(root:str):
    s = [root] # stack
    visited = set()
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
