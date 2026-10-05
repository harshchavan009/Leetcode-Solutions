class Solution:
    def rob(self, root):
        def dfs(node):
            if not node:
                return (0, 0)

            left = dfs(node.left)
            right = dfs(node.right)

            # Rob current node
            rob_current = node.val + left[1] + right[1]

            # Do not rob current node
            skip_current = max(left) + max(right)

            return (rob_current, skip_current)

        return max(dfs(root))