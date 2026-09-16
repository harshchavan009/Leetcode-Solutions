class Solution:
    def sortList(self, head):
        if head is None or head.next is None:
            return head

        # Find the middle of the linked list
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split into two halves
        mid = slow.next
        slow.next = None

        # Sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)

        # Merge the sorted halves
        return self.merge(left, right)

    def merge(self, left, right):
        dummy = ListNode(0)
        current = dummy

        while left and right:
            if left.val <= right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next

            current = current.next

        if left:
            current.next = left
        else:
            current.next = right

        return dummy.next