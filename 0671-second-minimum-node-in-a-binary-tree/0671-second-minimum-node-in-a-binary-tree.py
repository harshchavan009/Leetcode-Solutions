class Solution:
    def findSecondMinimumValue(self, root):
        minimum = root.val
        values = set()
        stack = [root]

        while stack:
            node = stack.pop()

            if node.val > minimum:
                values.add(node.val)

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        if not values:
            return -1

        return min(values)