def middle_point_sum():
    valid_middle_items, invalid_updates = validate_page_updates(page_updates(), page_ordering_rules())
    return sum(map(int, valid_middle_items))

def validate_page_updates(updates, rules):
    valid_middle_items = []
    invalid_updates = []
    # Check if each update in updates matches the rules
    for update in updates:
        # Split update into separate parts
        update_parts = update.split(",")
        # Check if the order of update_parts matches the rules
        valid = True
        for i in range(len(update_parts)):
            for j in range(i + 1, len(update_parts)):
                current = update_parts[i]
                next_item = update_parts[j]
                mapping = f"{current}|{next_item}"
                if mapping not in rules:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            # If all mappings in update_parts are valid, add the middle item to valid_middle_items
            middle_index = len(update_parts) // 2
            valid_middle_items.append(update_parts[middle_index])
        else:
            invalid_updates.append(update)
        
    return valid_middle_items, invalid_updates

def identify_and_fix_invalid_update_parts(invalid_updates, rules):
    fixed_updates = []
    for update in invalid_updates:
        update_parts = update.split(",")
        # Sort update_parts according to the rules
        update_parts.sort(key=lambda x: [rules.index(f"{x}|{y}") if f"{x}|{y}" in rules else float('inf') for y in update_parts])
        fixed_updates.append(",".join(update_parts))
    return fixed_updates

def page_ordering_rules():
    lines = read_file()
    empty_space_i = lines.index('')
    rules = [line for line in lines[:empty_space_i] if "|" in line]
    
    # Store each rule as a set of mappings
    rules_set = set(rules)
    return rules_set

def page_updates():
    lines = read_file()
    empty_space_index = lines.index('')
    updates = lines[empty_space_index + 1:]
    return updates

def read_file():
    with open("puzzle-input.txt") as file:
        lines = file.read().strip().split("\n")
    return lines

if __name__ == "__main__":
    valid_middle_items, invalid_updates = validate_page_updates(page_updates(), page_ordering_rules())
    print("Sum of valid middle items:", middle_point_sum())
    print("Invalid updates:", invalid_updates)
    
    rules = page_ordering_rules()
    fixed_updates = identify_and_fix_invalid_update_parts(invalid_updates, rules)
    
    # Validate the fixed updates and calculate the sum of their middle points
    fixed_middle_items, _ = validate_page_updates(fixed_updates, rules)
    print("Sum of fixed middle items:", sum(map(int, fixed_middle_items)))