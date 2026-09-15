class Solution:
    def copyRandomList(self, head):
        if head is None:
            return None

        # Map original nodes to their copies
        copied = {}

        current = head

        # Create a copy of every node
        while current:
            copied[current] = Node(current.val)
            current = current.next

        # Connect next and random pointers
        current = head

        while current:
            copied[current].next = copied.get(current.next)
            copied[current].random = copied.get(current.random)
            current = current.next

        return copied[head]