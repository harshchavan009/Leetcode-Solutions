class Solution:
    def buildTree(self, inorder, postorder):
        # Store the position of each value in inorder
        inorder_index = {}

        for i in range(len(inorder)):
            inorder_index[inorder[i]] = i

        # Last element of postorder is the root
        index = [len(postorder) - 1]

        def build(left, right):
            if left > right:
                return None

            # Current root value
            root_value = postorder[index[0]]
            index[0] -= 1

            root = TreeNode(root_value)

            # Find root in inorder
            mid = inorder_index[root_value]

            # Build right subtree first
            root.right = build(mid + 1, right)

            # Then build left subtree
            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1)