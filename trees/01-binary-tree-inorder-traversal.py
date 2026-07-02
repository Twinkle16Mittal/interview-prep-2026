"""
LeetCode 94 - Binary Tree Inorder Traversal
Approach: recursive, then iterative with explicit stack
Pattern: DFS tree traversal
Time: O(n) | Space: O(h) recursive, O(h) iterative
"""

# Recursive
def inorder_recursive(root):
    ans = []

    def dfs(root):
        nonlocal ans
        if root:
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)
    dfs(root)
    return ans

# Iterative
def inorder_iterative(root):
    stack =[]
    ans = []
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr= curr.left

        x = stack.pop()
        ans.append(x.val)
        curr = x.right

    return ans



