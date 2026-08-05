from collections import defaultdict, deque

class Solution:
    def remainingMethods(self, n, k, invocations):
        graph = defaultdict(list)

        # Build graph
        for u, v in invocations:
            graph[u].append(v)

        # Find all suspicious methods
        suspicious = set()
        queue = deque([k])
        suspicious.add(k)

        while queue:
            node = queue.popleft()
            for nei in graph[node]:
                if nei not in suspicious:
                    suspicious.add(nei)
                    queue.append(nei)

        # Check if any non-suspicious method invokes a suspicious method
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                return list(range(n))

        # Return remaining methods
        result = []
        for i in range(n):
            if i not in suspicious:
                result.append(i)

        return result