def part1():
    count = 0

    def is_safe(levels):
        is_increasing = all(1 <= levels[i] - levels[i-1] <= 3 for i in range(1, len(levels)))
        is_decreasing = all(1 <= levels[i-1] - levels[i] <= 3 for i in range(1, len(levels)))
        return is_increasing or is_decreasing

    with open("puzzle-input.txt") as file:
        for line in file:
            levels = list(map(int, line.split()))
            
            if is_safe(levels):
                count += 1
            else:
                for i in range(len(levels)):
                    if is_safe(levels[:i] + levels[i+1:]):
                        count += 1
                        break

    print(f"Number of safe reports: {count}")

if __name__ == "__main__":
    part1()