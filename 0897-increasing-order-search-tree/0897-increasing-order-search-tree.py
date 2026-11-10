# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root):
        dummy = TreeNode(0)
        tail = dummy
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            curr.left = None
            tail.right = curr
            tail = curr

            curr = curr.right

        tail.right = None

        return dummy.right
        