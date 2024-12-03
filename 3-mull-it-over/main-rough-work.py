import re

def validate_parentheses(string):
    # Inside parentheses must contain two numbers separated by a comma
    pattern = r"^mul\(\d+,\d+\)$"
    # If valid return true
    if re.match(pattern, string):
        return True
    else:
        return False

def part1():
    with open("puzzle-input.txt") as file:
        # Read it as one big string
        data = file.read()
        pattern = r"mul\(\d+,\d+\)"
        total = 0

        # Find all the strings that contain pattern
        matches = re.findall(pattern, data)
        # For each match add to an array
        for match in matches:
            # Validate each match and keep valid matches
            if validate_parentheses(match):
                # Get the two numbers
                numbers = re.findall(r"\d+", match)
                # Multiply the two numbers
                mul = int(numbers[0]) * int(numbers[1])
                # Sum all the results
                total += mul
        print(total)

if __name__ == "__main__":
    part1()
