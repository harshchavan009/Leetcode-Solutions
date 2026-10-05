class Solution:
    def isValidSerialization(self, preorder):
        slots = 1

        for node in preorder.split(','):
            # One slot is used by the current node
            slots -= 1

            if slots < 0:
                return False

            # Non-null node creates two new slots
            if node != '#':
                slots += 2

        return slots == 0