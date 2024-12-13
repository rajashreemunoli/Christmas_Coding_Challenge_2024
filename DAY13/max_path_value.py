def max_path_sum(tree):
    
    # Start from the second-to-last row and move upwards
    for row in range(len(tree) - 2, -1, -1):
        for col in range(len(tree[row])):
            # Add the maximum of the two possible downward paths to the current value
            tree[row][col] += max(tree[row + 1][col], tree[row + 1][col + 1])

    # The top element now contains the maximum path sum
    return tree[0][0]

# Example Christmas tree
christmas_tree = [
    [7],
    [3, 8],
    [8, 1, 0],
    [2, 7, 4, 4],
    [4, 5, 2, 6, 5]
]

# Find the maximum path sum
max_sum = max_path_sum(christmas_tree)
print(f"The maximum path sum in the Christmas tree is: {max_sum}")