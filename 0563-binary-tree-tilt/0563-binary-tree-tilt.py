class Solution:
    def findTilt(self, root):
        total_tilt = [0]

        def dfs(node):
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            total_tilt[0] += abs(left_sum - right_sum)

            return node.val + left_sum + right_sum

        dfs(root)
        return total_tilt[0]