import re

def part1():
    with open("puzzle-input.txt") as file:
        # Read it as one big string
        data = file.read()
        
        # Define patterns
        do_pattern = r"do\(\)"
        dont_pattern = r"don't\(\)"
        mul_pattern = r"mul\((\d+),(\d+)\)"

        total = 0
        
        # Split data by "do()" and "don't()"
        parts = re.split(f"({do_pattern}|{dont_pattern})", data)
        
        execute = True
        for part in parts:
            if part == "do()":
                execute = True
            elif part == "don't()":
                execute = False
            elif execute:
                # Find all the valid mul instructions and extract numbers
                matches = re.findall(mul_pattern, part)
                # Calculate the sum of all multiplications
                total += sum(int(x) * int(y) for x, y in matches)
        
        print(total)

if __name__ == "__main__":
    part1()