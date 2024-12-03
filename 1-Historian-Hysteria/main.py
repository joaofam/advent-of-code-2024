def part1():

    # Define left and right lists
    left = []
    right = []
    diff_list = []

    with open("puzzle-input.txt") as file:
        for line in file:
            sides = line.split()
            left.append(sides[0])
            right.append(sides[1])
    
    # Sort the lists
    left.sort()
    right.sort()

    # Loop both arrays and compare each number at index and add to a list
    for i in range(len(left)):
        diff = 0

        # Convert string index to integer
        left[i] = int(left[i])
        right[i] = int(right[i])
        diff = abs(left[i] - right[i])
        
        # Add difference to list
        diff_list.append(diff)
    
    # Add all differences
    total = sum(diff_list)
    print(total)

def part2():
    # Define left and right lists
    left = []
    right = []

    with open("puzzle-input.txt") as file:
        for line in file:
            sides = line.split()
            left.append(int(sides[0]))
            right.append(int(sides[1]))
    
    # Dictionary to count occurences of each number in right list
    occurences = {}
    for num in right:
        if num in occurences:
            occurences[num] += 1
        else:
            occurences[num] = 1
    
    total = 0
    for num in left:
        count = occurences.get(num, 0)
        total += num * count

    print(total)
            

if __name__ == "__main__":
    part2()