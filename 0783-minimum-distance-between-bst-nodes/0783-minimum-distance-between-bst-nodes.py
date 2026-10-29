class Solution:
    def minDiffInBST(self, root):
        stack = []
        curr = root
        prev = None
        min_diff = float('inf')

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            if prev is not None:
                min_diff = min(min_diff, curr.val - prev)

            prev = curr.val
            curr = curr.right

        return min_diff