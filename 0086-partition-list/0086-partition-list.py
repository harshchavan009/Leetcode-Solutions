class Solution:
    def partition(self, head, x):
        # Two dummy nodes for the two partitions
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)

        less = less_dummy
        greater = greater_dummy

        current = head

        while current:
            if current.val < x:
                less.next = current
                less = less.next
            else:
                greater.next = current
                greater = greater.next

            current = current.next

        # Connect the two partitions
        greater.next = None
        less.next = greater_dummy.next

        return less_dummy.next