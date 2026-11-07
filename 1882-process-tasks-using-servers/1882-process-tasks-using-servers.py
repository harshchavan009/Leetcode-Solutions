import heapq

class Solution:
    def assignTasks(self, servers, tasks):
        available = []
        busy = []
        for i, weight in enumerate(servers):
            heapq.heappush(available, (weight, i))

        ans = []
        time = 0

        for i, task in enumerate(tasks):
            time = max(time, i)
            while busy and busy[0][0] <= time:
                finish, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))
            if not available:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    finish, weight, index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, index))

            weight, index = heapq.heappop(available)

            ans.append(index)

            heapq.heappush(
                busy,
                (time + task, weight, index)
            )

        return ans