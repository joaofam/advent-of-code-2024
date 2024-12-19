def parse_input():
    with open("puzzle_input.txt") as file:
        return [list(line) for line in file.read().strip().splitlines()]

def get_start_position(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "^":
                return (row, col)
    return None

def move_forward(position, direction):
    row, col = position
    drow, dcol = direction
    return (row + drow, col + dcol)

def turn_right(direction):
    # In grid coordinates: Up(^) -> Right(>) -> Down(v) -> Left(<)
    # Up: (-1,0), Right: (0,1), Down: (1,0), Left: (0,-1)
    directions = {
        (-1, 0): (0, 1),   # Up to Right
        (0, 1): (1, 0),    # Right to Down
        (1, 0): (0, -1),   # Down to Left
        (0, -1): (-1, 0)   # Left to Up
    }
    return directions[direction]

def is_within_bounds(position, grid):
    row, col = position
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])

def simulate_guard_path(grid):
    start_pos = get_start_position(grid)
    direction = (-1, 0)  # Starting facing up (^)
    position = start_pos
    visited = set([start_pos])

    while True:
        next_pos = move_forward(position, direction)
        
        # Check if guard has left the grid
        if not is_within_bounds(next_pos, grid):
            break
            
        # Check if there's an obstacle ahead
        row, col = next_pos
        if grid[row][col] == '#':
            direction = turn_right(direction)
        else:
            position = next_pos
            visited.add(position)

    return len(visited)

def visualize_path(grid, visited):
    # Create a copy of the grid
    viz = [row[:] for row in grid]
    for row, col in visited:
        if viz[row][col] not in ['#', '^']:
            viz[row][col] = 'X'
    return [''.join(row) for row in viz]

if __name__ == "__main__":
    grid = parse_input()
    result = simulate_guard_path(grid)
    # Visualize the path
    print(f"The guard visits {result} distinct positions")