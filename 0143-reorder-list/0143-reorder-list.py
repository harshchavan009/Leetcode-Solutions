class Solution:
    def reorderList(self, head):
        if head is None or head.next is None:
            return

        # 1. Find the middle of the list
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse the second half
        second = slow.next
        slow.next = None

        prev = None

        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node

        second = prev

        # 3. Merge the two halves alternately
        first = head

        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next