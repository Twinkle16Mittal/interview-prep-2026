"""
LeetCode 98. Validate Binary Search Tree
Approach: Brute force approach using Inorder traversal and store each element in the array
and check it is sorted or not.
Optimized Approach
I will left and high range and check that particular node is in the range or not
Time: O(n) | Space: O(n) Brute force, O(h) optimized
"""

# Brute force approach
def is_valid_bst_brute(root):
    if not root:
            return True
    ans = []

    def dfs(node):
        nonlocal ans
        if not node:
            return 

        dfs(node.left)
        ans.append(node.val)
        dfs(node.right)

    dfs(root)
    x = ans [0]
    for i in range(1, len(ans)):
        if x >= ans[i]:
            return False
        x = ans[i]
    return True

# Optimized approach
def is_valid_bst_optimize(root):
    if not root:
        return True

    def dfs(node, low, high):
        if not node:
            return True

        if node.val <= low or node.val >= high:
            return False

        return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

    return dfs(root, float('-inf'), float('inf')) 






