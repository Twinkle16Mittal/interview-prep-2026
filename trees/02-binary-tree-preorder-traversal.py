"""
LeetCode 144 - Binary Tree Preorder Traversal
Approach: recursive, then iterative with explicit stack
Pattern: DFS tree traversal
Time: O(n) | Space: O(h) recursive, O(h) iterative
"""

# Recursive
def preorder_recursive(root):
    ans = []

    def dfs(root):
        nonlocal ans
        if not root:
            return

        ans.append(root.val)
        dfs(root.left)
        dfs(root.right)
    
    dfs(root)
    return ans

# Iterative
def preorder_iterative(root):
    ans = []
    stack = []
    curr = root

    while stack or curr:
        while curr:
            ans.append(curr.val)
            stack.append(curr)
            curr = curr.left

        x = stack.pop()
        curr = x.right
    return ans



