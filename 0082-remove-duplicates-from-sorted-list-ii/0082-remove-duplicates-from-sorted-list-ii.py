class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:
            # Check if current value is duplicated
            if curr.next and curr.val == curr.next.val:
                duplicate_value = curr.val

                # Skip all nodes with the duplicate value
                while curr and curr.val == duplicate_value:
                    curr = curr.next

                prev.next = curr
            else:
                prev = curr
                curr = curr.next

        return dummy.next