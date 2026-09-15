class Solution:
    def sortedListToBST(self, head):
        # Count the number of nodes
        n = 0
        curr = head

        while curr:
            n += 1
            curr = curr.next

        # Use an array so the pointer can be updated
        # inside the recursive function without nonlocal.
        current = [head]

        def build(size):
            if size <= 0:
                return None

            # Build left subtree
            left = build(size // 2)

            # Current linked-list node becomes root
            root = TreeNode(current[0].val)
            root.left = left

            # Move to next linked-list node
            current[0] = current[0].next

            # Build right subtree
            root.right = build(size - size // 2 - 1)

            return root

        return build(n)