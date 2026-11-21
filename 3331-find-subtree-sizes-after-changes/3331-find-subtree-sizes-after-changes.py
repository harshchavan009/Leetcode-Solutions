
class Solution:
    def findSubtreeSizes(self, parent, s):
        n = len(parent)

        # Build the original tree
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        # Store the nearest ancestor with the same character
        last_seen = [-1] * 26

        # Build the modified tree
        new_children = [[] for _ in range(n)]
        new_parent = [-1] * n

        # Iterative DFS: (node, exiting, previous_node)
        stack = [(0, False, -1)]

        while stack:
            node, exiting, old = stack.pop()
            c = ord(s[node]) - ord('a')

            if not exiting:
                old = last_seen[c]

                p = old if old != -1 else parent[node]

                new_parent[node] = p

                if node != 0:
                    new_children[p].append(node)

                last_seen[c] = node

                stack.append((node, True, old))

                for child in reversed(children[node]):
                    stack.append((child, False, -1))

            else:
                last_seen[c] = old

        # Calculate subtree sizes in the modified tree
        ans = [1] * n
        order = [0]

        for node in order:
            for child in new_children[node]:
                order.append(child)

        for node in reversed(order):
            p = new_parent[node]

            if p != -1:
                ans[p] += ans[node]

        return ans
