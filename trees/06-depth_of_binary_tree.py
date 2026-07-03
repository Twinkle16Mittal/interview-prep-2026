'''
543. Diameter of Binary Tree
brute force it will tke O(n^2) time complexity as for each node we are calculating the height of the tree
O(h) space complexity for recursive stack
optimize time O(n) and space O(h) for recursive stack


'''
def diameterOfBinaryTree_brute(root) -> int:
        if not root:
            return 0
        ans = 0

        def height(node):
            if not node:
                return 0
            return 1+ max(height(node.left), height(node.right))

        def dfs(node):
            if not node:
                return 0
            nonlocal ans
            lh = height(node.left)
            rh = height(node.right)
            ans = max(ans, lh+rh)
            dfs(node.left)
            dfs(node.right)
        dfs(root)

        return ans

def diameterOfBinaryTree_optimized(root) -> int:
    ans = 0
    def dfs(node):
        nonlocal ans
        if not node:
            return 0
        lh = dfs(node.left)
        rh = dfs(node.right)

        ans = max(ans, lh+rh)
        return 1+max(lh, rh)

    dfs(root)
    return ans