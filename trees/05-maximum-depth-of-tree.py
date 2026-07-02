'''
Leetcode 104. Maximum Depth of Binary Tree
approach: DFS recursive to check the depth on each node

Time : O(n) | space: O(h)
'''


def maxDepth(root):
    if root == None:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))