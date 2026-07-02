"""
LeetCode 145 - Binary Tree Postorder Traversal
Approach: recursive, then iterative with explicit stack
Pattern: DFS tree traversal
Time: O(n) | Space: O(h) recursive, O(h) iterative
"""

# Recursive
def postorder_recursive(root):
    ans = []

    def dfs(root):
        nonlocal ans
        if not root:
            return
        
        dfs(root.left)
        dfs(root.right)
        ans.append(root.val)

    dfs(root)
    return ans

# Iterative
def postorder_iterative(root):
    ans = []
    stack = []
    curr = root

    while stack or curr:
        while curr:
            ans.append(curr.val)
            stack.append(curr)
            curr = curr.right

        x = stack.pop()
        curr = x.left
        

    return ans[::-1]




