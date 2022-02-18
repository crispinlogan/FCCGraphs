"""From https://structy.net/problems/minimum-island and minute 119 in video"""

from cgitb import small
from collections import deque

def minimum_island(grid):
    """
    Go over each island and count the number of pieces of land that it has and keep a
    running tally of which is the smallest.
    Don't even need to keep track of a global visited as can just recount the same island (less efficient but still fine)
    BFS (though perhaps not necessary!)
    """
    smallest_island_count = float('inf')

    def valid_next_visit(row, col, visited):
        if row >=0 and row < len(grid) and col >= 0 and col < len(grid[0]) and (row, col) not in visited and grid[row][col] == 'L':
            return True
        return False

    def count_nodes_in_island(row, col):
        visited = set()
        q = deque([(row, col)])
        while q:
            c = q.popleft()
            visited.add(c)
            row, col = c
            if valid_next_visit(row+1, col, visited):
                q.append((row+1, col))
            if valid_next_visit(row-1, col, visited):
                q.append((row-1, col))
            if valid_next_visit(row, col+1, visited):
                q.append((row, col+1))
            if valid_next_visit(row, col-1, visited):
                q.append((row, col-1))
        return len(visited)

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'L':
                current_island_count = count_nodes_in_island(row, col)
                if current_island_count < smallest_island_count:
                    smallest_island_count = current_island_count

    return smallest_island_count



grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(minimum_island(grid)) # -> 2



def minimum_island(grid):
    """
    Go over each island and count the number of pieces of land that it has and keep a
    running tally of which is the smallest.
    Don't even need to keep track of a global visited as can just recount the same island (less efficient but still fine)
    DFS and also use a global visited set for this
    """
    smallest_island_count = float('inf')
    visited = set()
    def count_nodes(row, col):
        if (row, col) in visited or row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != 'L':
            return 0
        visited.add((row, col))
        num_nodes = 1
        num_nodes += count_nodes(row+1, col)
        num_nodes += count_nodes(row-1, col)
        num_nodes += count_nodes(row, col+1)
        num_nodes += count_nodes(row, col-1)
        return num_nodes
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'L' and (row, col) not in visited:
                current_island_count = count_nodes(row, col)
                print(row, col, current_island_count)
                if current_island_count < smallest_island_count:
                    smallest_island_count = current_island_count
    return smallest_island_count



grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(minimum_island(grid)) # -> 2
