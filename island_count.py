"""From https://structy.net/problems/island-count and minute 99 in video"""

from collections import defaultdict

from connected_components_count import connected_components_count

def island_count(grid):
    """
    Convert grid into a adj_list (just for Ls).
    Then do count components.
    """
    # convert into adj_list
    adj_list = defaultdict(set)
    min_row = 0
    min_col = 0
    max_row = len(grid) - 1
    max_col = len(grid[0]) - 1
    def check_valid_neighbour(row, col):
        if row > max_row or row < min_row or col > max_col or col < min_col:
            return False
        return True
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'L':
                neighbours = []
                if check_valid_neighbour(row+1, col) and grid[row+1][col] == 'L':
                    neighbours.append((row+1, col))
                if check_valid_neighbour(row, col+1) and grid[row][col+1] == 'L':
                    neighbours.append((row, col+1))
                if check_valid_neighbour(row-1, col) and grid[row-1][col] == 'L':
                    neighbours.append((row-1, col))
                if check_valid_neighbour(row, col-1) and grid[row][col-1] == 'L':
                    neighbours.append((row, col-1))
                if neighbours:
                    adj_list[(row, col)].update(neighbours)
                else:
                    adj_list[(row,col)] = set()
    print(adj_list)

    # count components
    return connected_components_count(adj_list)





grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(island_count(grid)) # -> 3

grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]

print(island_count(grid)) # -> 4





def island_count(grid):
    """
    Now take approach in video - no need to convert to adj_list can do directly
    on grid using same principle as in first attempt.
    """
    visited = set()

    def explore(position):
        visited.add(position)
        row, col = position
        up = (row, col-1)
        down = (row, col+1)
        left = (row-1, col)
        right = (row+1, col)
        if valid_position(up):
            explore(up)
        if valid_position(down):
            explore(down)
        if valid_position(left):
            explore(left)
        if valid_position(right):
            explore(right)

    def valid_position(position):
        row, col = position
        min_row = 0
        min_col = 0
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        if row > max_row or row < min_row or col > max_col or col < min_col:
            return False
        if grid[row][col] == 'W':
            return False
        if position in visited:
            return False
        return True

    def valid_to_explore(position):
        if position in visited or not valid_position(position):
            return False
        return True

    total_islands = 0
    for row in range(len(grid)):
        for col in range(len(grid)):
            position = (row, col)
            if valid_to_explore(position):
                explore((row, col))
                total_islands += 1

    return total_islands


grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(island_count(grid)) # -> 3

grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]

print(island_count(grid)) # -> 4



def island_count(grid):
    """This is another variant - we can mark the waters as visited and then just do
    count connected components"""
    visited = set()
    total_islands = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            position = (row, col)
            if grid[row][col] == 'W':
                visited.add(position)

    def valid_position(position):
        row, col = position
        min_row = 0
        min_col = 0
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        if row > max_row or row < min_row or col > max_col or col < min_col:
            return False
        # if grid[row][col] == 'W':
        #     return False
        if position in visited:
            return False
        return True

    def explore(position):
        visited.add(position)
        row, col = position
        up = (row, col-1)
        down = (row, col+1)
        left = (row-1, col)
        right = (row+1, col)
        if valid_position(up):
            explore(up)
        if valid_position(down):
            explore(down)
        if valid_position(left):
            explore(left)
        if valid_position(right):
            explore(right)

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            position = (row, col)
            if grid[row][col] == 'L' and position not in visited:
                explore(position)
                total_islands += 1

    return total_islands



grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(island_count(grid)) # -> 3

grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]

print(island_count(grid)) # -> 4



def island_count(grid):
    """Try to make as simple as possible in terms of lines written and code"""
    def explore(row, col):
        # this line takes care of 'valid position' question
        if row > len(grid) - 1 or row < 0 or col > len(grid[0]) - 1 or col < 0 or grid[row][col] != 'L':
            return
        grid[row][col] = 'V' # mark visited like this, much easier
        explore(row+1, col)
        explore(row-1, col)
        explore(row, col+1)
        explore(row, col-1)
    num_islands = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'L':
                explore(row, col)
                num_islands += 1
    return num_islands

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(island_count(grid)) # -> 3

grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]

print(island_count(grid)) # -> 4


from collections import deque
def island_count(grid):
    """Try to make as simple as possible in terms of lines written and code
    AND ALSO TRY WITH BFS - JUST HAD TO CHANGE EXPLORE FUNCTION"""
    def explore(row, col):
        q = deque([(row, col)])
        while q:
            c = q.popleft()
            row, col = c
            # this line takes care of 'valid position' question
            if row > len(grid) - 1 or row < 0 or col > len(grid[0]) - 1 or col < 0 or grid[row][col] != 'L':
                continue
            grid[row][col] = 'V'
            q.append((row+1, col))
            q.append((row-1, col))
            q.append((row, col+1))
            q.append((row, col-1))
    num_islands = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'L':
                explore(row, col)
                num_islands += 1
    return num_islands

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(island_count(grid)) # -> 3

grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]

print(island_count(grid)) # -> 4




def island_count(grid):
    """Try to make as simple as possible in terms of lines written and code
    AND ALSO TRY WITH STACK-BASED DFS - JUST HAD TO CHANGE EXPLORE FUNCTION"""
    def explore(row, col):
        s = [(row, col)]
        while s:
            c = s.pop()
            row, col = c
            # this line takes care of 'valid position' question
            if row > len(grid) - 1 or row < 0 or col > len(grid[0]) - 1 or col < 0 or grid[row][col] != 'L':
                continue
            grid[row][col] = 'V'
            s.append((row+1, col))
            s.append((row-1, col))
            s.append((row, col+1))
            s.append((row, col-1))
    num_islands = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'L':
                explore(row, col)
                num_islands += 1
    return num_islands

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(island_count(grid)) # -> 3

grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]

print(island_count(grid)) # -> 4




####
# A LEARNING FROM THE VIDEO - THE GUY SAYS 'DON'T LOOK BEFORE YOU LEAP' WITH RECURSION
# AND WHAT HE MEANS IS THAT YOU CAN CATCH AN INVALID POSITION IN THE BASE CASE OF EXPLORE
# WHICH SAVES YOU WRITING A LOT OF DUPLICATE CODE (MIN 115.40 IN VID)
####

# DO LOOK BEFORE YOU LEAP (LESS REPEATED CODE - BETTER)
def island_count(grid):
    """Try to make as simple as possible in terms of lines written and code"""
    def explore(row, col):
        # this line takes care of 'valid position' question
        if row > len(grid) - 1 or row < 0 or col > len(grid[0]) - 1 or col < 0 or grid[row][col] != 'L':
            return
        grid[row][col] = 'V' # mark visited like this, much easier
        explore(row+1, col)
        explore(row-1, col)
        explore(row, col+1)
        explore(row, col-1)
    num_islands = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'L':
                explore(row, col)
                num_islands += 1
    return num_islands

grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]

print(island_count(grid)) # -> 4


# DO LOOK BEFORE YOU LEAP (MORE REPEATED CODE - WORSE)
def island_count(grid):
    """Try to make as simple as possible in terms of lines written and code"""
    def explore(row, col):
        """
        # this line takes care of 'valid position' question
        if row > len(grid) - 1 or row < 0 or col > len(grid[0]) - 1 or col < 0 or grid[row][col] != 'L':
            return
        """
        print(row, col)
        grid[row][col] = 'V' # mark visited like this, much easier
        """Lots of extra look before you leap repeated type code below"""
        if row + 1 <= len(grid) - 1 and grid[row+1][col] == 'L':
            explore(row+1, col)
        if row - 1 >= 0 and grid[row-1][col] == 'L':
            explore(row-1, col)
        if col + 1 <= len(grid[0]) - 1 and grid[row][col+1] == 'L':
            explore(row, col+1)
        if col - 1 >= 0 and grid[row][col-1] == 'L':
            explore(row, col-1)
    num_islands = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            print(row, col)
            if grid[row][col] == 'L':
                explore(row, col)
                num_islands += 1
    return num_islands

grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]

print(island_count(grid)) # -> 4







grid = [['L','L','L','L','L','W','L','L','L','L','L','L','L','L','L','W','L','W','L','L'],['W','L','L','L','L','L','L','L','L','L','L','L','L','W','L','L','L','L','L','W'],['L','W','L','L','L','W','W','L','L','W','L','L','L','L','L','L','L','L','L','L'],['L','L','L','L','W','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L'],['L','W','W','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L'],['L','W','L','L','L','L','L','L','W','L','L','L','W','L','L','L','W','L','L','L'],['W','L','L','L','L','L','L','L','L','L','L','L','W','L','L','W','L','L','L','L'],['L','L','L','L','L','L','L','L','L','L','L','L','W','L','L','L','L','W','L','L'],['L','L','L','L','L','L','L','L','L','L','W','L','L','L','L','L','L','L','L','L'],['L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L'],['W','L','L','L','L','L','L','L','W','L','L','L','L','L','L','L','L','L','L','L'],['L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L'],['L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L'],['L','L','L','L','L','W','L','L','L','L','L','L','L','W','L','L','L','L','L','L'],['L','W','L','L','L','L','L','W','L','L','L','W','L','L','L','L','W','L','L','L'],['L','L','L','L','L','L','L','L','L','L','L','L','W','L','L','L','L','L','L','W'],['L','L','L','L','L','L','L','L','L','L','L','L','L','W','L','L','L','L','W','W'],['L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L'],['L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L'],['L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L']]
print(island_count(grid)) # -> 1
