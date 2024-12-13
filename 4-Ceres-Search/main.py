# PART 1
# ------
# Word Search - all 'XMAS'
# Words can be found in the following directions:
# - Horizontal
# - Vertical
# - Diagonal
# - Reverse
# - Overlapping other words

def part1():
    # Read the puzzle input
    with open("puzzle-input.txt") as file:
        lines = file.read().strip().split("\n")

    n = len(lines)
    m = len(lines[0])

    # Generate all directions
    directions = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            directions.append((dx, dy))

    def has_xmas(i, j, d):
        dx, dy = d
        for k, x in enumerate("XMAS"):
            ni = i + k * dx
            nj = j + k * dy
            if not (0 <= ni < n and 0 <= nj < m):
                return False
            if lines[ni][nj] != x:
                return False
        return True

    # Count up every cell and every direction
    ans = 0
    for i in range(n):
        for j in range(m):
            for d in directions:
                if has_xmas(i, j, d):
                    ans += 1
    print(ans)

def part2():
    # Read the puzzle input
    with open("puzzle-input.txt") as file:
        lines = file.read().strip().split("\n")

    n = len(lines)
    m = len(lines[0])

    # Generate all directions
    directions = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            directions.append((dx, dy))

    def has_xmas(i, j):
        if not (1 <= i < n - 1 and 1 <= j < m - 1):
            return False
        if lines[i][j] != "A":
            return False
        
        # Check both diagonals
        diag_1 = f"{lines[i-1][j-1]}{lines[i+1][j+1]}"
        diag_2 = f"{lines[i-1][j+1]}{lines[i+1][j-1]}"


        if diag_1 in ["MS", "SM"] and diag_2 in ["MS", "SM"]:
            return True
        return False

    ans = 0
    for i in range(n):
        for j in range(m):    
            ans += has_xmas(i, j)

    print(ans)

# Call the function
part1()
part2()
