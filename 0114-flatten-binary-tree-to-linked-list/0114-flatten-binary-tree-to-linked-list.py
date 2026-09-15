class Solution:
    def flatten(self, root):
        current = root

        while current:
            if current.left:
                # Find the rightmost node of the left subtree
                predecessor = current.left

                while predecessor.right:
                    predecessor = predecessor.right

                # Connect the original right subtree
                # to the rightmost node of the left subtree
                predecessor.right = current.right

                # Move the left subtree to the right
                current.right = current.left
                current.left = None

            current = current.right