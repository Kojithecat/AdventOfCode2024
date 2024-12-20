from collections import deque

def is_valid_move(grid, visited, row, col):
    rows, cols = len(grid), len(grid[0])
    return 0 <= row < rows and 0 <= col < cols and grid[row][col] == '.' and not visited[row][col]

def shortest_path(grid, start, end):
    # Directions for moving up, down, left, and right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # Initialize queue for BFS
    queue = deque([(start[0], start[1], 0)])
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]
    visited[start[0]][start[1]] = True
    
    while queue:
        row, col, dist = queue.popleft()
        
        # Check if we have reached the end
        if (row, col) == end:
            return dist
        
        # Explore the neighbors
        for d in directions:
            new_row, new_col = row + d[0], col + d[1]
            if is_valid_move(grid, visited, new_row, new_col):
                visited[new_row][new_col] = True
                queue.append((new_row, new_col, dist + 1))
    
    # If no path is found, return -1
    return -1

# Example grid
coords = []
with open("input.txt") as file:
    input = file.read()
    coords = input.split('\n')[:-1]
    print(coords)
    coords = [(int(coord.split(',')[0]), int(coord.split(',')[1])) for coord in coords]
print(coords)
n = 71
grid = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if (j,i) in coords:
            grid[i][j] = '#'
        else:   
            grid[i][j] = '.'

for l in grid:
    print(l)

start = (0, 0) # Starting position (row, col)
end = (70, 70)   # Ending position (row, col)

# Call the function and print the result
result = shortest_path(grid, start, end)
print("The shortest path distance is:", result)