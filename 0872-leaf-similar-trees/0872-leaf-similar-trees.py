# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1, root2):
        def getLeaves(root):
            leaves = []
            stack = [root]

            while stack:
                node = stack.pop()

                if node.left is None and node.right is None:
                    leaves.append(node.val)
                else:
                    if node.right:
                        stack.append(node.right)

                    if node.left:
                        stack.append(node.left)

            return leaves

        return getLeaves(root1) == getLeaves(root2)
        