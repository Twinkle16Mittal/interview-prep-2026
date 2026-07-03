'''
leetcode 112. Path Sum
Time = O(n) | Space = O(h)
'''


def path_sum(root, target_sum):
    if not root:
            return False

    def dfs(node, curr_sum):
        if not node:
            return False
        if node.left == None and node.right == None:
            if curr_sum + node.val == target_sum:
                return True
            return False
            
        return dfs(node.left , curr_sum + node.val) or dfs(node.right, curr_sum+node.val)

    return dfs(root, 0)