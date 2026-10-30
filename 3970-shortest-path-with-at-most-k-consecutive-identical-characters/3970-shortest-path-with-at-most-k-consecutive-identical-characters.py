import heapq

class Solution:
    def shortestPath(self, n, edges, labels, k):
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]

        dist[0][1] = 0
        pq = [(0, 0, 1)]

        while pq:
            cost, node, count = heapq.heappop(pq)

            if cost != dist[node][count]:
                continue

            if node == n - 1:
                return cost

            for neighbor, weight in graph[node]:
                if labels[neighbor] == labels[node]:
                    if count == k:
                        continue
                    new_count = count + 1
                else:
                    new_count = 1

                new_cost = cost + weight

                if new_cost < dist[neighbor][new_count]:
                    dist[neighbor][new_count] = new_cost
                    heapq.heappush(
                        pq,
                        (new_cost, neighbor, new_count)
                    )

        return -1