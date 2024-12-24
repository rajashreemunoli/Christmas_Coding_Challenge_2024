class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root):
    # Helper function to compare two subtrees
    def is_mirror(t1, t2):
        # Base cases
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        # Check if current nodes are equal and their children are mirrors
        return (t1.val == t2.val and
                is_mirror(t1.left, t2.right) and
                is_mirror(t1.right, t2.left))
    
    # Start comparison from the root's left and right subtrees
    return is_mirror(root.left, root.right)


# Helper function to construct a binary tree from a list
def build_tree(values):
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    for i in range(len(values)):
        if nodes[i]:
            if 2 * i + 1 < len(values):
                nodes[i].left = nodes[2 * i + 1]
            if 2 * i + 2 < len(values):
                nodes[i].right = nodes[2 * i + 2]
    return nodes[0]


# Construct the tree
root = build_tree([1, 2, 2, 3, 4, 4, 3])

# Test the function
print(isSymmetric(root))  # Output: True