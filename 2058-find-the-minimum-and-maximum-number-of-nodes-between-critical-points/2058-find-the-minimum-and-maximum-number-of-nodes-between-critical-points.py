class Solution:
    def nodesBetweenCriticalPoints(self, head):
        # Need at least 3 nodes to have a critical point
        if head is None or head.next is None or head.next.next is None:
            return [-1, -1]

        prev = head
        curr = head.next
        index = 1

        first = -1
        last = -1
        min_distance = float('inf')

        while curr.next:
            next_node = curr.next

            # Check whether current node is a critical point
            is_max = curr.val > prev.val and curr.val > next_node.val
            is_min = curr.val < prev.val and curr.val < next_node.val

            if is_max or is_min:
                if first == -1:
                    # First critical point
                    first = index
                else:
                    # Distance from previous critical point
                    distance = index - last
                    min_distance = min(min_distance, distance)

                last = index

            prev = curr
            curr = next_node
            index += 1

        # Fewer than two critical points
        if first == -1 or first == last:
            return [-1, -1]

        # Maximum distance is between first and last critical points
        max_distance = last - first

        return [min_distance, max_distance]