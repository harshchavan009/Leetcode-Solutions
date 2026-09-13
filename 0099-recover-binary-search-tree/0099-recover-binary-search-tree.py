class Solution:
    def recoverTree(self, root):
        first = None
        second = None
        prev = None

        def inorder(node):
            nonlocal first, second, prev

            if node is None:
                return

            inorder(node.left)

            if prev is not None and prev.val > node.val:
                if first is None:
                    first = prev
                second = node

            prev = node

            inorder(node.right)

        inorder(root)

        # Swap the two incorrect values
        first.val, second.val = second.val, first.val